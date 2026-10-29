#!/usr/bin/env python3
"""Publication checks: canonical specs, evidence states, assets and built links."""
import hashlib, json, re, subprocess, sys, zipfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

R=Path(__file__).resolve().parents[1]
def require(ok,message):
    if not ok: raise SystemExit(message)
def run(*args): subprocess.run(args,cwd=R,check=True)

C=json.loads((R/'specs/course.json').read_text())
require([c['id'] for c in C['chapters']]==[f'CH{i:02d}' for i in range(1,13)],'Chapter IDs or order are inconsistent')
require([p['id'] for p in C['parts']]==['P1','P2','P3','P4'],'Four parts are required')
for i,c in enumerate(C['chapters'],1):
    require(c['number']==i and c['part']==f'P{(i-1)//3+1}' and c['milestone']==f'M{i:02d}','Chapter mapping mismatch')
    require(all(o in C['outcomes'] for o in c['outcomes']) and c['outcomes'],'Invalid learning outcomes')
    require(all(c.get(k) for k in ['topics','goals','task','evidence','question','prerequisite','boundary']),'Missing teaching specification')
    require((R/c['spec']).is_file() and (R/c['source']).is_file(),'Missing chapter specification or prose')
    raw=(R/c['source']).read_text()
    require(raw.startswith('# '+c['title']+'：'+c['subtitle']+'\n'),'Chapter title differs from course.json: '+c['id'])
    state=re.search(r'^> 状态：(outline|draft|review|published)$',raw,re.M)
    require(state,'Missing chapter status: '+c['id'])
    require(re.search(r'^> 版本：\d+\.\d+\.\d+$',raw,re.M),'Missing content version')
    if state[1]=='published':
        require(not re.search(r'TODO|待补|在此填写|在此记录|完整教材正文将在',raw),'Unresolved placeholder in reviewed chapter')

run(sys.executable,'scripts/sync_specs.py','--check')
for a in json.loads((R/'brand/reuse-manifest.json').read_text())['reused']:
    if a['mode']=='unchanged': require(hashlib.sha256((R/a['path']).read_bytes()).hexdigest()==a['sha256'],'Brand baseline modified: '+a['path'])
figures=json.loads((R/'textbook/assets/figures/manifest.json').read_text())
require(len({f['id'] for f in figures})==len(figures),'Duplicate figure ID')
require(len({f['file'] for f in figures})==len(figures),'Duplicate figure path')
for f in figures:
    require(all(f.get(k) for k in ['id','file','title','alt','width','height','source','license','date']),'Missing figure metadata')
    require(re.fullmatch(r'AG-\d{2}-\d{2}',f['id']),'Invalid edition figure ID')
    require(Path(f['file']).name==f['file'] and (R/'textbook/assets/figures'/f['file']).is_file(),'Invalid figure file')
    require(isinstance(f['width'],int) and isinstance(f['height'],int) and f['width']>0 and f['height']>0,'Invalid figure dimensions')
for p in R.rglob('*.md'):
    if any(x in p.relative_to(R).parts for x in ['dist','.git']): continue
    raw=re.sub(r'```.*?```|`[^`]+`', '', p.read_text(), flags=re.S)
    for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',raw):
        u=urlsplit(target)
        if u.scheme or u.netloc or not u.path: continue
        dest=(p.parent/unquote(u.path)).resolve()
        require(dest.is_relative_to(R) and dest.exists(),f'Missing repository link: {p.relative_to(R)} -> {target}')
run('node','--check','site/app.js')
run(sys.executable,'scripts/build_site.py')

class Page(HTMLParser):
    def __init__(self): super().__init__();self.links=[];self.ids=set();self.duplicates=[];self.h1=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:
            if a['id'] in self.ids:self.duplicates.append(a['id'])
            self.ids.add(a['id'])
        if tag=='h1':self.h1+=1
        for key in ('href','src'):
            if a.get(key):self.links.append(a[key])
        if tag=='img':require(bool(a.get('alt')),'Missing image alternative text')

out=R/'dist';parsed={}
for f in out.rglob('*.html'):
    raw=f.read_text();page=Page();page.feed(raw);parsed[f.resolve()]=page
    require(page.h1==1 and not page.duplicates,'Invalid headings or duplicate IDs: '+str(f))
    require('AIOS101-AtomGit' in raw,'Missing repository link')
    require(not any(x in raw for x in ['页边手账','标记为已读','记下一个想法','AUTHORING:']),'Retired or author-only UI leaked')
for f,p in parsed.items():
    for link in p.links:
        u=urlsplit(link)
        if u.scheme or u.netloc:continue
        dest=(f.parent/unquote(u.path)).resolve() if u.path else f
        if dest.is_dir():dest=dest/'index.html'
        require(dest.is_relative_to(out) and dest.exists(),f'Broken built link: {f.relative_to(out)} -> {link}')
        if u.fragment and dest in parsed:require(unquote(u.fragment) in parsed[dest].ids,f'Broken anchor: {link}')
for f in (out/'assets').rglob('*.css'):
    for url in re.findall(r'url\([\"\']?([^\"\')]+)',f.read_text()):
        if not url.startswith(('data:','https:')):require((f.parent/url).exists(),'Missing CSS asset')
for f in [out/'styles.css']:
    for url in re.findall(r'url\([\"\']?([^\"\')]+)',f.read_text()):require((f.parent/url).exists(),'Missing font file')
with zipfile.ZipFile(out/'downloads/ai-project-observatory-template.zip') as z:
    require(len(z.namelist())==7 and z.testzip() is None,'Template archive is invalid')
kit_root=R/'practice/ch01'
with zipfile.ZipFile(out/'downloads/ch01-starter.zip') as z:
    expected={'my-ai-observatory/'+f.relative_to(kit_root).as_posix():f.read_bytes() for f in kit_root.rglob('*') if f.is_file()}
    require(len(expected)==8 and set(z.namelist())==set(expected) and z.testzip() is None,'Chapter 1 archive is invalid')
    require(all(z.read(name)==data for name,data in expected.items()),'Chapter 1 archive content differs')
    require('my-ai-observatory/work/guide-v1.md' not in z.namelist(),'Starter must not impersonate learner output')
prompt=re.search(r'```text\n(.*?)\n```',(R/'textbook/chapters/CH01.md').read_text(),re.S)
require(prompt and prompt[1]+'\n'==(kit_root/'prompt.txt').read_text(),'Chapter 1 prompt differs from kit')
kit2_root=R/'practice/ch02'
with zipfile.ZipFile(out/'downloads/ch02-observation-kit.zip') as z:
    expected={'ch02/'+f.relative_to(kit2_root).as_posix():f.read_bytes() for f in kit2_root.rglob('*') if f.is_file()}
    require(len(expected)==7 and set(z.namelist())==set(expected) and z.testzip() is None,'Chapter 2 archive is invalid')
    require(all(z.read(name)==data for name,data in expected.items()),'Chapter 2 archive content differs')
require(len(parsed)==21,'Unexpected page count')
print(f'PASS: {len(parsed)} HTML pages; canonical specs, local links/anchors, brand integrity, content states, all three practice archives, Chapter 1 prompt and JavaScript syntax')
