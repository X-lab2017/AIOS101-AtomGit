#!/usr/bin/env python3
"""Static course website. Content and navigation have one canonical source."""
import hashlib, html, json, os, re, shutil, zipfile
from pathlib import Path
from urllib.parse import quote, urlsplit
import course_markdown as md

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist'
C=json.loads((ROOT/'specs/course.json').read_text())
REPO=C['repository']
COMMIT=os.getenv('GITHUB_SHA','local-preview')
if not re.fullmatch(r'[a-f0-9]{40}|local-preview',COMMIT): raise SystemExit('Invalid build commit')
REF='main' if COMMIT=='local-preview' else COMMIT
STATUS={'outline':('章节提纲','Outline'),'draft':('正文草稿','Draft'),'review':('内容待评审','In review'),'published':('已审定正文','Reviewed')}
ROUTES={'textbook/preface.md':'preface/','textbook/about.md':'about/','practice/README.md':'practice/','practice/demo/README.md':'practice/demo/','practice/template/README.md':'practice/template/','practice/ch01/README.md':'practice/ch01/'}
ROUTES.update({c['source']:f"chapters/{c['number']:02d}/" for c in C['chapters']})
def esc(s): return html.escape(str(s),quote=True)
def bi(zh,en,tag='span',attrs=''): return f'<{tag} data-zh="{esc(zh)}" data-en="{esc(en)}" {attrs}>{esc(zh)}</{tag}>'
def status(source):
    text=(ROOT/source).read_text();m=re.search(r'^> 状态：(outline|draft|review|published)$',text,re.M)
    if not m: raise ValueError('Missing content status: '+source)
    return m[1]
def portable_markdown(source):
    """Keep downloaded prose and illustrations usable outside the checkout."""
    def rewrite(m):
        target=m[3]; parsed=urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path: return m[0]
        resolved=(ROOT/source).parent.joinpath(parsed.path).resolve().relative_to(ROOT).as_posix()
        base=REPO.replace('https://github.com/','https://raw.githubusercontent.com/')+'/'+REF+'/' if m[1] else REPO+'/blob/'+REF+'/'
        return m[1]+'['+m[2]+']('+base+quote(resolved)+('#'+parsed.fragment if parsed.fragment else '')+')'
    chunks=re.split(r'(```.*?```|`[^`]+`)',(ROOT/source).read_text(),flags=re.S)
    return ''.join(chunk if i%2 else re.sub(r'(!?)\[([^\]]+)\]\(([^)]+)\)',rewrite,chunk) for i,chunk in enumerate(chunks))
def chip(s): return bi(*STATUS[s],attrs=f'class="status {s}"')
def prefix(route): return '../'*len(Path(route).parts) if route else './'
def icon(name): return f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="{name}"/></svg>'

def shell(route,title,body,active='learn',description=None):
    p=prefix(route)
    nav=''.join(f'<a href="{p}{r}"'+(' aria-current="page"' if active==key else '')+'>'+bi(zh,en)+'</a>' for key,r,zh,en in [('learn','learn/','学习路径','Learning path'),('practice','practice/','项目实践','Practice'),('about','about/','关于课程','About')])
    checksum=hashlib.sha256(((ROOT/'site/styles.css').read_text()+(ROOT/'site/app.js').read_text()).encode()).hexdigest()[:12]
    result=f'''<!doctype html>
<html lang="zh-CN" data-aios-theme="light"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)} · AI 开源通识（AtomGit 版）</title><meta name="description" content="{esc(description or C['principle']+' '+C['goal'])}"><meta name="theme-color" content="#F6F3EB"><link rel="icon" href="{p}assets/course/favicon.svg"><link rel="stylesheet" href="{p}assets/tokens.css?v={checksum}"><link rel="stylesheet" href="{p}styles.css?v={checksum}"><script src="{p}app.js?v={checksum}" defer></script></head>
<body><a class="skip-link" href="#main">跳转到正文 / Skip to content</a>
<header class="topbar"><div class="topbar-inner"><a class="brand" href="{p}" aria-label="AI 开源通识 首页"><img data-logo="course" src="{p}assets/course/logo-light.svg" alt="AIOS101 · AI 开源通识" width="228" height="57"></a><span class="edition">AtomGit 版</span><nav id="main-nav" aria-label="主要导航">{nav}<a class="repo-link" href="{REPO}" target="_blank" rel="noopener">GitHub ↗</a></nav><div class="tools"><button id="language-toggle" class="tool" aria-label="Switch interface to English">EN</button><button id="theme-toggle" class="tool theme-toggle" aria-label="切换深色主题"><span aria-hidden="true">◐</span></button><button id="menu-toggle" class="tool menu-toggle" aria-label="展开导航" aria-controls="main-nav" aria-expanded="false">☰</button></div></div></header>
<p class="translation-note" hidden>Interface in English · The textbook and practice materials are currently in Chinese.</p>
<main id="main" tabindex="-1">{body}</main>
<footer class="footer"><div class="footer-inner"><div class="producer"><img data-logo="xlab" src="{p}assets/logo-light.svg" alt="X-lab AI" width="128" height="40"><span>{bi('X-lab 出品','A course by X-lab')}<br><small>Learn in the open.</small></span></div><div class="footer-copy"><p>{esc(C['goal'])}</p><a href="{REPO}">GitHub</a><span> · </span><a href="{p}about/">{bi('关于课程','About')}</a><small class="build-label">{bi('课程评审版','Course review')} · v{C['version']} · {esc(COMMIT[:7])}</small></div></div></footer></body></html>'''
    target=OUT/route/'index.html';target.parent.mkdir(parents=True,exist_ok=True);target.write_text(result)

def chapter_rows(p, part=None):
    rows=[]
    for c in C['chapters']:
        if part and c['part']!=part: continue
        rows.append(f'''<a class="chapter-row" data-search="{esc(c['title']+c['subtitle']+c['question']+' '.join(c['topics']))}" href="{p}chapters/{c['number']:02d}/"><span class="chapter-number">{c['number']:02d}</span><span class="chapter-info"><strong>{esc(c['title'])}</strong><span>{esc(c['subtitle'])}</span></span>{chip(status(c['source']))}<span class="row-arrow" aria-hidden="true">↗</span></a>''')
    return ''.join(rows)

def home():
    p='./'
    pathways=''.join(f'''<a class="pathway p{i+1}" href="learn/#part-{part['id']}"><span class="part-index">0{i+1} / {part['en'].upper()}</span><h3>{part['name']}</h3><p>{part['intro']}</p><span class="pathway-end">{bi('第 '+str(i*3+1)+'—'+str(i*3+3)+' 章','Chapters '+str(i*3+1)+'–'+str(i*3+3))} <span aria-hidden="true">↗</span></span></a>''' for i,part in enumerate(C['parts']))
    body=f'''<div class="wrap"><section class="hero"><div class="hero-copy"><div class="eyebrow"><span class="live-dot"></span> AIOS101 / ATOMGIT EDITION</div><h1>用开源来理解 AI，<br>用 AI 来<span class="highlight">贡献开源。</span></h1><p class="hero-goal">{C['goal']}</p><p class="hero-intro">打开真实的 AI 项目，把一个小问题变成有用的作品。<br class="desktop-break">在共同创造中，建立自己的技能集与作品集。</p><div class="hero-actions"><a class="button primary" href="learn/">{bi('查看学习路径','Explore the course')} <span aria-hidden="true">→</span></a><a class="text-link" href="practice/">{bi('认识项目实践','Meet the project')} ↗</a></div><p class="hero-note">{bi('面向所有专业 · 无需编程基础','For every discipline · No coding prerequisite')}</p></div>
<div class="folio-scene" aria-label="AI 开源项目观察站：观察、理解、创作、贡献"><div class="folio-back"></div><div class="folio-page"><div class="folio-top"><span>FIELD NOTES / 001</span><span class="folio-stamp">OPEN</span></div><img class="folio-mark" src="assets/course/mark-light.svg" data-logo="mark" alt="开卷标志" width="160" height="160"><p class="folio-kicker">贯穿式项目实践</p><h2>AI 开源项目<br>观察站</h2><div class="folio-rule"></div><p class="folio-caption">观察一个项目<br>理解一种机制<br>创造一份有用的成果</p><div class="folio-bottom"><span>DeepSeek × DSH</span><span>AtomGit ↗</span></div></div><span class="folio-label label-one">从真实项目开始</span><span class="folio-label label-two">让成果帮助别人</span></div></section>
<div class="review-note"><span class="note-marker">i</span><p><strong>{bi('序言与第一章图文已开放评审','Preface and Chapter 1 ready for review')}</strong><span>{bi('从第一件小作品开始，配套材料包已就绪；其余十一章可预览学习提纲。','Start with a small creation and the Chapter 1 kit. The remaining eleven chapters offer outlines.')}</span></p></div>
<section class="section"><div class="section-heading"><div><span class="eyebrow">A JOURNEY IN FOUR PARTS</span><h2>从第一次创作，到第一份贡献</h2></div><a class="text-link" href="preface/">{bi('先读序言','Read the preface')} →</a></div><div class="pathways">{pathways}</div></section>
<section class="project-feature"><div><span class="eyebrow">ONE PROJECT, MANY POSSIBILITIES</span><h2>边学边建，<br>让观察站持续生长。</h2><p>师生都围绕 AI 开源项目开展观察、实验与创作。你的成果可以是一份指南、一幅图解、一个交互演示，也可以是一件小工具。</p><a class="text-link" href="practice/">{bi('查看贯穿实践与模板','Explore practice and templates')} →</a></div><div class="station-list"><div><b>01</b><span><strong>项目档案</strong><small>对象、材料、来源与问题</small></span></div><div><b>02</b><span><strong>理解与创作</strong><small>观察、核验与可用作品</small></span></div><div><b>03</b><span><strong>协作与积累</strong><small>反馈、修订与个人成长</small></span></div></div></section>
<section class="roles"><p><b>DeepSeek · DSH</b><span>既是学习对象，也是创作工具</span></p><span class="roles-cross">×</span><p><b>AtomGit</b><span>保存版本，分享成果，共同改进</span></p><span class="roles-cross">→</span><p><b>你的技能集与作品集</b><span>让每一次学习有迹可循</span></p></section></div>'''
    shell('', '用开源来理解 AI，用 AI 来贡献开源',body,active='home')

def learn():
    intro=f'''<section class="page-intro"><span class="eyebrow">LEARNING PATH</span><h1>四篇十二章，<br>一步步参与创造。</h1><p>认识开源、理解 AI、开展创作、进入社区。每一章都推进同一个项目实践。</p></section><div class="learn-tools"><a class="preface-link" href="../preface/"><span>00</span><strong>{bi('序言 · 从这里开始','Preface · Start here')}</strong><span aria-hidden="true">→</span></a><label class="search-box">{bi('查找章节','Find a chapter')}<input id="chapter-search" type="search" placeholder="标题、主题或问题" autocomplete="off"></label></div>'''
    groups=''.join(f'''<section class="chapter-group" id="part-{part['id']}"><div class="group-heading"><span class="part-index">0{i+1} / {part['en'].upper()}</span><h2>{part['name']}<span>{part['title']}</span></h2><p>{part['intro']}</p></div><div class="chapter-list">{chapter_rows('../',part['id'])}</div></section>''' for i,part in enumerate(C['parts']))
    shell('learn/','学习路径',f'<div class="wrap narrow-wrap">{intro}<p class="catalog-note">{bi("序言与第一章为图文评审稿，其余十一章为提纲。每章标记实际状态，可按顺序阅读。","Preface and Chapter 1 are in review. The remaining eleven chapters are outlines.")}</p>{groups}<p id="search-empty" class="empty-state" hidden>没有找到相关章节，请尝试“模型”“创作”或“协作”。</p><p id="search-status" class="sr-only" aria-live="polite"></p></div>')

def reader(route,key,source,title,subtitle='',chapter=None,active='learn',extra=''):
    p=prefix(route);md.PAGE_PREFIX=p
    u=md.unit(ROOT/source,ROOT,REF,ROUTES,key)
    if key=='PREFACE': title=u['title'].replace('，','，\n',1)
    section_links=''.join(f'<a href="#{esc(s["id"])}">{esc(s["title"])}</a>' for s in u['sections'])
    section_html=''.join(f'<section class="reading-section" id="{esc(s["id"])}"><h2>{esc(s["title"])}</h2>{s["html"]}</section>' for s in u['sections'])
    sidemenu=''.join(f'<a href="{p}chapters/{c["number"]:02d}/"'+(' aria-current="page"' if chapter and chapter['id']==c['id'] else '')+f'><span>{c["number"]:02d}</span>{esc(c["title"])}</a>' for c in C['chapters'])
    sidebar=f'<a class="sidebar-back" href="{p}learn/">← {bi("学习路径","Learning path")}</a><details class="chapter-menu"><summary>{bi("全书目录","All chapters")}</summary><nav aria-label="全书目录">{sidemenu}</nav></details><nav class="section-nav" aria-label="本页目录"><b>{bi("本页内容","On this page")}</b>{section_links}</nav>'
    st=status(source)
    st_note= '<div class="outline-note"><strong>本章当前为学习提纲</strong><p>这里先呈现学习路线、实践任务和完成证据，完整教材正文将在后续创作中补充。</p></div>' if st=='outline' else ''
    goals=''
    if chapter:
        goals='<div class="learning-goals"><span class="eyebrow">'+chapter['id']+' / '+next(x['name'] for x in C['parts'] if x['id']==chapter['part'])+'</span><p class="core-question">'+esc(chapter['question'])+'</p><ul>'+''.join('<li>'+esc(g)+'</li>' for g in chapter['goals'])+'</ul></div>'
    neighbours=''
    if chapter:
        n=chapter['number'];prev=('preface/','序言') if n==1 else (f'chapters/{n-1:02d}/',C['chapters'][n-2]['title']);nxt=('practice/','项目实践') if n==12 else (f'chapters/{n+1:02d}/',C['chapters'][n]['title'])
        neighbours=f'<nav class="chapter-pagination" aria-label="章节切换"><a href="{p}{prev[0]}"><small>← {bi("上一章","Previous")}</small><strong>{esc(prev[1])}</strong></a><a href="{p}{nxt[0]}"><small>{bi("下一步","Next")} →</small><strong>{esc(nxt[1])}</strong></a></nav>'
    elif key=='PREFACE': neighbours=f'<div class="next-step"><a class="button primary" href="{p}chapters/01/">进入第 1 章 →</a></div>'
    elif active=='practice': neighbours=f'<div class="next-step"><a class="text-link" href="{p}learn/">← 返回学习路径</a></div>'
    source_url=REPO+'/blob/'+REF+'/'+source
    source_records=json.loads((ROOT/'specs/sources.json').read_text())
    references=[r for r in source_records if key in r.get('locations',[])]
    reference_html=('<p>本页事实核对来源（访问日期见链接项）：</p><ul>'+''.join('<li><a href="'+esc(r['url'])+'" target="_blank" rel="noopener">'+esc(r['title'])+'</a> · '+esc(r['accessed'])+'</li>' for r in references)+'</ul>') if references else ''
    body=f'''<div class="wrap reader-layout"><aside class="reader-sidebar">{sidebar}</aside><div class="reader-main"><header class="reader-heading"><div class="reader-meta">{chip(st)}<span>v{esc(u['version'])}</span></div><h1>{esc(title)}</h1>{'<p class="reader-subtitle">'+esc(subtitle)+'</p>' if subtitle else ''}<div class="reading-controls"><span>{bi('正文字号','Text size')}</span><button data-font="-1" aria-label="减小正文字号">A−</button><button data-font="1" aria-label="增大正文字号">A＋</button></div></header>{st_note}{goals}{extra}<article class="prose">{section_html}</article>{neighbours}<details class="source-details"><summary>{bi('来源与版本','Source and version')}</summary><p>正文版本 {esc(u['version'])} · {STATUS[st][0]}</p><a href="{source_url}">查看 Markdown 正本 ↗</a><span> · </span><a href="{p}downloads/{key}.md">下载本页 Markdown</a>{reference_html}</details></div></div>'''
    shell(route,title,body,active)
    (OUT/'downloads'/f'{key}.md').write_text(portable_markdown(source))

def main():
    OUT.mkdir(exist_ok=True)
    for old in OUT.iterdir():
        if old.is_dir(): shutil.rmtree(old)
        else: old.unlink()
    shutil.copytree(ROOT/'site',OUT,dirs_exist_ok=True,ignore=shutil.ignore_patterns('README.md','NOTICE.md'))
    shutil.copyfile(ROOT/'brand/tokens.css',OUT/'assets/tokens.css')
    (OUT/'downloads').mkdir(exist_ok=True)
    figures=json.loads((ROOT/'textbook/assets/figures/manifest.json').read_text())
    for f in figures:
        target=OUT/'assets/figures'/f['file'];target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(ROOT/'textbook/assets/figures'/f['file'],target)
    with zipfile.ZipFile(OUT/'downloads/ai-project-observatory-template.zip','w',zipfile.ZIP_DEFLATED) as z:
        for f in sorted((ROOT/'practice/template').glob('*.md')):
            zi=zipfile.ZipInfo('ai-project-observatory/'+f.name,date_time=(2026,10,29,0,0,0));zi.compress_type=zipfile.ZIP_DEFLATED;zi.external_attr=0o644<<16;z.writestr(zi,f.read_bytes())
    with zipfile.ZipFile(OUT/'downloads/ch01-starter.zip','w',zipfile.ZIP_DEFLATED) as z:
        for f in sorted((ROOT/'practice/ch01').rglob('*')):
            if not f.is_file(): continue
            name='my-ai-observatory/'+f.relative_to(ROOT/'practice/ch01').as_posix()
            zi=zipfile.ZipInfo(name,date_time=(2026,10,29,0,0,0));zi.compress_type=zipfile.ZIP_DEFLATED;zi.external_attr=0o644<<16;z.writestr(zi,f.read_bytes())
    home();learn()
    reader('preface/','PREFACE','textbook/preface.md','从使用 AI，\n到共同创造。','序言 · 打开，才能理解')
    for c in C['chapters']:reader(f"chapters/{c['number']:02d}/",c['id'],c['source'],c['title'],c['subtitle'],c)
    reader('about/','ABOUT','textbook/about.md','关于这门课程',active='about')
    downloads='<div class="practice-actions"><a class="button primary" href="../downloads/ai-project-observatory-template.zip" download>下载观察站模板 ↓</a><a class="text-link" href="demo/">查看示范结构 →</a></div>'
    reader('practice/','PRACTICE','practice/README.md','AI 开源项目观察站','贯穿全课的项目实践载体',active='practice',extra=downloads)
    reader('practice/demo/','DEMO','practice/demo/README.md','示范观察站：认识 DSH','资料阅读与结构示例 · 实际任务待验证',active='practice')
    extra='<div class="practice-actions"><a class="button primary" href="../../downloads/ai-project-observatory-template.zip" download>下载全部模板 ↓</a><a class="text-link" href="https://atomgit.com/" target="_blank" rel="noopener">前往 AtomGit ↗</a></div>'
    reader('practice/template/','TEMPLATE','practice/template/README.md','从一份模板开始','复制、填写、观察，再逐步完善。',active='practice',extra=extra)
    kit='<div class="practice-actions"><a class="button primary" href="../../downloads/ch01-starter.zip" download>下载第一章材料包 ↓</a><a class="text-link" href="../../chapters/01/">返回第一章 →</a></div>'
    reader('practice/ch01/','CH01-KIT','practice/ch01/README.md','第一章材料包','做一页有依据、能打开的 DSH 项目导览',active='practice',extra=kit)
    (OUT/'.nojekyll').write_text('')
    (OUT/'build.json').write_text(json.dumps({'version':C['version'],'commit':COMMIT,'chapters':[{ 'id':c['id'],'status':status(c['source']),'source':c['source']} for c in C['chapters']]},ensure_ascii=False,indent=2))
    print('Built 20 static pages, chapter status labels and two downloadable practice kits')

if __name__=='__main__': main()
