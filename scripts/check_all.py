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
    data=(R/'textbook/assets/figures'/f['file']).read_bytes()
    require(hashlib.sha256(data).hexdigest()==f['sha256'] and len(data)==f['bytes'],'Figure integrity differs: '+f['id'])
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
kit3_root=R/'practice/ch03'
with zipfile.ZipFile(out/'downloads/ch03-reuse-kit.zip') as z:
    expected={'ch03/'+f.relative_to(kit3_root).as_posix():f.read_bytes() for f in kit3_root.rglob('*') if f.is_file()}
    require(len(expected)==8 and set(z.namelist())==set(expected) and z.testzip() is None,'Chapter 3 archive is invalid')
    require(all(z.read(name)==data for name,data in expected.items()),'Chapter 3 archive content differs')
kit4_root=R/'practice/ch04'
with zipfile.ZipFile(out/'downloads/ch04-learning-kit.zip') as z:
    expected={'ch04/'+f.relative_to(kit4_root).as_posix():f.read_bytes() for f in kit4_root.rglob('*') if f.is_file()}
    require(set(z.namelist())==set(expected) and z.testzip() is None,'Chapter 4 archive is invalid')
    require(all(z.read(name)==data for name,data in expected.items()),'Chapter 4 archive content differs')
# Independently recompute the chapter's explicitly synthetic arithmetic.
training=[(100,30),(200,60),(300,90)]
errors={a:sum(abs(a*n/100-t) for n,t in training)/len(training) for a in (20,30,40)}
require(errors=={20:20,30:0,40:20},'Training example arithmetic differs')
require([30*n/100 for n in (150,250)]==[45,75],'Held-out predictions differ')
require((abs(45-48)+abs(75-72))/2==3 and abs(60-150)==90,'Held-out errors differ')
require({a:sum(abs(a*n/100-t) for n,t in [(100,28),(200,63),(300,84)]) for a in (20,30,40)}=={20:55,30:11,40:65}, 'New training arithmetic differs')
kit5_root=R/'practice/ch05'
with zipfile.ZipFile(out/'downloads/ch05-evidence-kit.zip') as z:
    expected={'ch05/'+f.relative_to(kit5_root).as_posix():f.read_bytes() for f in kit5_root.rglob('*') if f.is_file()}
    require(set(z.namelist())==set(expected) and z.testzip() is None,'Chapter 5 archive is invalid')
    require(all(z.read(name)==data for name,data in expected.items()),'Chapter 5 archive content differs')
# Prevent drift that would change instructions as well as the comparison material.
template=(kit5_root/'prompt-template.txt').read_text()
require(template.count('{{MATERIALS}}')==1,'Chapter 5 prompt must have exactly one material slot')
a=(kit5_root/'materials/brief.md').read_text().strip()
b=(kit5_root/'materials/guide.md').read_text().strip()
require((kit5_root/'prompt-a.txt').read_text()==template.replace('{{MATERIALS}}',a),'Chapter 5 A prompt differs from canonical material')
require((kit5_root/'prompt-b.txt').read_text()==template.replace('{{MATERIALS}}',a+'\n\n'+b),'Chapter 5 B prompt changes more than material')
kit6_root=R/'practice/ch06'
with zipfile.ZipFile(out/'downloads/ch06-task-kit.zip') as z:
    expected={'ch06/'+f.relative_to(kit6_root).as_posix():f.read_bytes() for f in kit6_root.rglob('*') if f.is_file()}
    require(set(z.namelist())==set(expected) and z.testzip() is None,'Chapter 6 archive is invalid')
    require(all(z.read(name)==data for name,data in expected.items()),'Chapter 6 archive content differs')
    require('ch06/work/guide-candidate.md' not in z.namelist(),'Chapter 6 kit must not impersonate learner output')
ch6=(R/'textbook/chapters/CH06.md').read_text()
require(bool(re.search(r'^## 6\.1 ',ch6,re.M)), 'Chapter 6 needs readable numbered sections')
chapter6_figures=[f for f in figures if f['id'].startswith('AG-06-')]
require(chapter6_figures, 'Chapter 6 figure metadata missing')
for f in chapter6_figures:
    data=(R/'textbook/assets/figures'/f['file']).read_bytes()
    require(hashlib.sha256(data).hexdigest()==f['sha256'] and len(data)==f['bytes'],'Chapter 6 figure integrity differs')
    require(ch6.count('../assets/figures/'+f['file'])==1,'Chapter 6 figure reference differs')
# Practice archives are validated against their actual source files, not a file-count quota.
for chapter, required in {'ch04':['work/experiment-record.md','materials/check-values.md'], 'ch05':['prompt-a.txt','prompt-b.txt','work/comparison-record.md'], 'ch06':['prompt.txt','materials/guide-before.md','work/task-record.md']}.items():
    require(all((R/'practice'/chapter/name).is_file() for name in required), 'Missing learning task input: '+chapter)
creation_kits={'ch07':'design-kit','ch08':'creation-kit','ch09':'review-kit'}
active=[key for key in creation_kits if (R/'practice'/key/'README.md').exists()]
for key in active:
    with zipfile.ZipFile(out/'downloads'/f'{key}-{creation_kits[key]}.zip') as z:
        root=R/'practice'/key
        expected={key+'/'+f.relative_to(root).as_posix():f.read_bytes() for f in root.rglob('*') if f.is_file()}
        require(z.testzip() is None and set(z.namelist())==set(expected),'Creation archive file set differs: '+key)
        require(all(z.read(name)==data for name,data in expected.items()),'Creation archive bytes differ: '+key)
        require(not any(name.endswith(('work/artifact-v1.md','work/artifact-v2.md','work/artifact-revised.md')) for name in z.namelist()),'Creation kit impersonates learner output: '+key)
for key in active:
    raw=(R/'textbook/chapters'/f'{key.upper()}.md').read_text()
    own_figures=[f for f in figures if f['id'].startswith('AG-'+key[2:]+'-')]
    for fig in own_figures:
        require(raw.count('../assets/figures/'+fig['file'])==1,'Figure reference missing or duplicated: '+fig['id'])
# Instructions must point at included inputs; learner outputs remain absent.
if 'ch08' in active:
    for name in ['plan-prompt.txt','create-prompt.txt']:
        prompt=(R/'practice/ch08'/name).read_text()
        for target in re.findall(r'materials/[a-z-]+\.md',prompt):
            require((R/'practice/ch08'/target).is_file(),'Chapter 8 prompt input missing: '+target)
if 'ch09' in active:
    require(not (R/'practice/ch09/materials/candidate.md').exists(),'Chapter 9 must receive the learner candidate')
require(len(parsed)==25+len(active),'Unexpected page count')
print(f'PASS: {len(parsed)} HTML pages; canonical specs, local links/anchors, brand integrity, content states, all practice archives, Chapter 4 arithmetic, Chapter 1 and Chapter 5 prompts and JavaScript syntax')
