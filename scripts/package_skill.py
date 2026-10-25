#!/usr/bin/env python3
"""Build an immutable, reproducible full skill ZIP with per-file hashes; no upload."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import zipfile

REQUIRED=['SKILL.md','README.md','CHANGELOG.md','agents/openai.yaml','assets/icon.svg','LICENSE','CONTRIBUTING.md','CITATION.cff','references/FULL_PRODUCTION_PACK.md','references/PLATFORM_ROUTES.md','references/ATTACHMENT_AND_IDENTITY_GATE.md','references/CASE14_PRODUCTION_REFERENCE.md']
EXCLUDE={'.git','__pycache__','.pytest_cache','.DS_Store','node_modules','dist'}

def declaration(text,pattern,label):
    m=re.search(pattern,text,re.M)
    if not m:raise ValueError('Version declaration missing: '+label)
    return m.group(1)

def inspect(root):
    root=Path(root).resolve()
    for name in REQUIRED:
        if not (root/name).is_file():raise ValueError('Required file missing: '+name)
    skill=(root/'SKILL.md').read_text(encoding='utf-8')
    slug=declaration(skill,r'^name:\s*([a-z0-9-]+)\s*$','name')
    semver=r'(\d+\.\d+\.\d+)'
    versions={
        'skill_heading':declaration(skill,r'^# .+\(v'+semver+r'\)\s*$','heading'),
        'skill_metadata':declaration(skill,r'^  version:\s*[\"\']?'+semver+r'[\"\']?\s*$','metadata'),
        'agent':declaration((root/'agents/openai.yaml').read_text(),r'^version:\s*[\"\']?'+semver+r'[\"\']?\s*$','agent'),
        'readme':declaration((root/'README.md').read_text(),r'^\*\*Version:\*\*\s*'+semver+r'\s*$','readme'),
        'changelog':declaration((root/'CHANGELOG.md').read_text(),r'^## \[?'+semver,'changelog')}
    if len(set(versions.values()))!=1:raise ValueError('Current version drift: '+json.dumps(versions))
    files=[]
    for f in sorted(root.rglob('*')):
        rel=f.relative_to(root)
        if set(rel.parts)&EXCLUDE or f.suffix in ('.pyc','.zip') or f.name=='PACKAGE_MANIFEST.json':continue
        if f.is_symlink():raise ValueError('Symlink not permitted: '+str(rel))
        if f.is_file():
            # Importable source package: do not accidentally export private media or binaries.
            if f.name not in ('LICENSE','.gitignore','.gitattributes') and f.suffix not in ('.md','.txt','.py','.json','.yaml','.yml','.svg','.csv','.cff'):raise ValueError('Unreviewed export file type: '+str(rel))
            f.read_bytes().decode('utf-8');files.append(f)
    return root,slug,next(iter(versions.values())),files,versions

def build(root,output):
    root,slug,version,files,versions=inspect(root);output=Path(output).resolve()
    if output==root or root in output.parents:raise ValueError('Output ZIP must be outside skill root')
    if output.exists():raise FileExistsError('Existing release preserved; choose a new path')
    entries={str(f.relative_to(root)).replace('\\','/'):f.read_bytes() for f in files}
    if sum(map(len,entries.values()))>100*1024*1024:raise ValueError('Skill exceeds Gemini100MiB import limit')
    source_commit=None;dirty=None
    try:
        source_commit=subprocess.check_output(['git','-C',str(root),'rev-parse','HEAD'],text=True,stderr=subprocess.DEVNULL).strip()
        dirty=bool(subprocess.check_output(['git','-C',str(root),'status','--porcelain','--','.'],text=True,stderr=subprocess.DEVNULL).strip())
    except (OSError,subprocess.CalledProcessError):pass
    manifest={'skill_name':slug,'skill_version':version,'source_git_commit':source_commit,'skill_worktree_dirty':dirty,'version_declarations':versions,'files':{n:{'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)} for n,b in entries.items()},'boundary':'Package integrity only; installation, app access, clinical/media QA and GitHub merge are not verified.'}
    entries['PACKAGE_MANIFEST.json']=(json.dumps(manifest,ensure_ascii=False,indent=2,sort_keys=True)+'\n').encode()
    output.parent.mkdir(parents=True,exist_ok=True)
    try:
        with output.open('xb') as stream:
            with zipfile.ZipFile(stream,'w',compression=zipfile.ZIP_DEFLATED) as z:
                for name,b in sorted(entries.items()):
                    info=zipfile.ZipInfo(slug+'/'+name,date_time=(1980,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16;z.writestr(info,b)
    except Exception:
        output.unlink(missing_ok=True);raise
    with zipfile.ZipFile(output) as z:
        if z.testzip():raise ValueError('ZIP CRC verification failed')
        for n,item in manifest['files'].items():
            if hashlib.sha256(z.read(slug+'/'+n)).hexdigest()!=item['sha256']:raise ValueError('ZIP payload hash mismatch')
    return {'zip':str(output),'version':version,'files':len(entries),'bytes':output.stat().st_size,'sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'source_git_commit':source_commit,'skill_worktree_dirty':dirty,'installation':'NOT_TESTED'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    try:r=build(a.root,a.output)
    except (OSError,ValueError) as e:print(json.dumps({'package_status':'BLOCKED','error':str(e)}));return 2
    print(json.dumps(r,indent=2));return 0

if __name__=='__main__':raise SystemExit(main())
