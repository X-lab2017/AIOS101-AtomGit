#!/usr/bin/env python3
"""Print the canonical introduction and proposed contents for curriculum review.

Supply Noto Serif SC / Noto Sans SC font files via --serif, --sans and --bold.
The PDF and renamed font subsets are separate deliverables, never Pages assets.
"""
import argparse
import base64
import hashlib
import html
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup
from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import course_markdown as md

ROOT = Path(__file__).resolve().parents[1]
PRINT = ROOT / 'textbook/print/introduction'
SOURCES = ['textbook/preface.md', 'textbook/contents-review.md']
PUBLIC = 'https://www.x-lab.info/AIOS101-AtomGit/'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare_fonts(args, visible):
    folder = PRINT/'fonts'
    folder.mkdir(parents=True, exist_ok=True)
    inputs = {}
    for source, name, weight in [(args.serif,'IntroBookSerif',400),
                                  (args.sans,'IntroBookSans',400),
                                  (args.bold,'IntroBookSansBold',700)]:
        font = TTFont(source)
        options = subset.Options()
        options.name_IDs = ['*']
        options.name_legacy = True
        options.name_languages = ['*']
        options.recalc_timestamp = False
        worker = subset.Subsetter(options=options)
        worker.populate(text=visible+''.join(chr(n) for n in range(32,127))+'•')
        worker.subset(font)
        if 'fvar' in font:
            font = instantiateVariableFont(font, {'wght':weight}, inplace=True)
        for record in font['name'].names:
            if record.nameID in (1,4,6,16):
                record.string = name.encode(record.getEncoding())
        output = folder/(name+'.ttf')
        font.save(output)
        needed = {ord(c) for c in visible if '\u3400' <= c <= '\u9fff'}
        missing = needed - set(font.getBestCmap())
        if missing:
            raise ValueError('Missing glyphs: '+''.join(map(chr,sorted(missing))))
        inputs[name] = {'source':source.name,'sha256':digest(source)}
    return inputs


def clean_figures(soup, figures):
    for figure in soup.select('figure'):
        record = next(f for f in figures if 'figure-'+f['id'].lower()==figure['id'])
        path = ROOT/'textbook/assets/figures'/record['file']
        if path.suffix=='.svg':
            svg = re.sub(r'font-family="[^"]+"','font-family="IntroBookSans"',path.read_text())
            figure.img['src']='data:image/svg+xml;base64,'+base64.b64encode(svg.encode()).decode()
        else:
            figure.img['src']=path.as_uri()
        for key in ('loading','decoding','width','height'):
            figure.img.attrs.pop(key,None)
        figure.a.unwrap()
        for link in figure.figcaption.select('a'):
            link.decompose()
        for item in list(figure.figcaption.children):
            if isinstance(item,str): item.replace_with(str(item).rstrip(' ·'))


def main():
    parser=argparse.ArgumentParser()
    for name in ('serif','sans','bold'):
        parser.add_argument('--'+name,type=Path,required=True)
    args=parser.parse_args()
    PRINT.mkdir(parents=True,exist_ok=True)
    figures=[f for f in json.loads((ROOT/'textbook/assets/figures/manifest.json').read_text()) if f['id'].startswith('AG-00-')]
    routes={'textbook/contents-review.md':'outline/','textbook/preface.md':'preface/'}
    md.PAGE_PREFIX=PUBLIC
    intro=md.unit(ROOT/SOURCES[0],ROOT,'main',routes,'PREFACE')
    contents=md.unit(ROOT/SOURCES[1],ROOT,'main',routes,'OUTLINE')
    blocks=[]
    for section in intro['sections']:
        heading='' if section['id']=='opening' else '<h2>'+html.escape(section['title'])+'</h2>'
        blocks.append('<section>'+heading+section['html']+'</section>')
    intro_soup=BeautifulSoup(''.join(blocks),'html.parser')
    clean_figures(intro_soup,figures)
    for table in intro_soup.select('table'):
        if table.th.get_text()=='维度': table['class']=['goals-matrix']
        else: table['class']=['course-matrix']

    toc=[]
    for section in contents['sections']:
        fragment=BeautifulSoup(section['html'],'html.parser')
        if section['id']=='opening':
            toc.append('<section class="contents-opening"><div class="eyebrow">教材目录 · 结构评审稿</div><h1>全书目录</h1>'+str(fragment)+'</section>')
        elif section['title'].startswith('第一部分'):
            groups=[]; current=[]; lead=[]
            for node in list(fragment.children):
                if getattr(node,'name',None)=='h3':
                    if current: groups.append(''.join(current))
                    current=[str(node)]
                elif current: current.append(str(node))
                else: lead.append(str(node))
            if current: groups.append(''.join(current))
            for index,group in enumerate(groups):
                lead_in='<h2>'+html.escape(section['title'])+'</h2>'+''.join(lead) if index==0 else '<div class="eyebrow">第一部分　认识开源</div>'
                toc.append('<section class="contents-page detailed">'+lead_in+group+'</section>')
        else:
            css='appendices' if section['title'].startswith('附录') else 'contents-page'
            toc.append('<section class="'+css+'"><h2>'+html.escape(section['title'])+'</h2>'+str(fragment)+'</section>')
    doc='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><title>AI 开源通识：引言与全书目录评审稿</title><meta name="author" content="X-lab"></head><body>
    <article id="introduction"><div class="book-brand"><img src="'''+(ROOT/'site/assets/course/logo-light.svg').as_uri()+'''" alt="AI 开源通识"><img class="producer" src="'''+(ROOT/'site/assets/logo-light.svg').as_uri()+'''" alt="X-lab AI"></div>
    <div class="eyebrow">引言</div><h1>在开源中学习，<br>与 AI 共同创造</h1>'''+str(intro_soup)+'''</article><article id="contents">'''+''.join(toc)+'''</article></body></html>'''
    visible=BeautifulSoup(doc,'html.parser').get_text()+'AI 开源通识引言全书目录评审稿'
    for figure in figures:
        if figure['file'].endswith('.svg'):
            visible+=BeautifulSoup((ROOT/'textbook/assets/figures'/figure['file']).read_text(),'xml').get_text()
    font_inputs=prepare_fonts(args,visible)
    style=ROOT/'scripts/print-introduction.css'
    fc=FontConfiguration()
    document=HTML(string=doc,base_url=str(ROOT)).render(stylesheets=[CSS(filename=style,font_config=fc)],font_config=fc)
    output=ROOT/'textbook/print/AIOS101-Introduction-and-Contents-Review.pdf'
    document.write_pdf(output,optimize_images=True,jpeg_quality=95,pdf_identifier=b'AIOS101-introduction-0.5.0-contents-0.1.0')
    work=ROOT/'tmp/pdfs';work.mkdir(parents=True,exist_ok=True)
    (work/'introduction-review.html').write_text(doc)
    inputs=SOURCES+['scripts/build_introduction_review.py','scripts/print-introduction.css','scripts/course_markdown.py','site/assets/course/logo-light.svg','site/assets/logo-light.svg']
    inputs += ['textbook/assets/figures/'+f['file'] for f in figures]
    inputs += [p.relative_to(ROOT).as_posix() for p in sorted((PRINT/'fonts').glob('*.ttf'))]
    record={'sourceVersions':{'PREFACE':intro['version'],'OUTLINE':contents['version']},'file':output.name,'pages':len(document.pages),'paper':'A4','bytes':output.stat().st_size,'sha256':digest(output),'fontSources':font_inputs,'figureMetadataSha256':hashlib.sha256(json.dumps(figures,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),'inputs':{p:digest(ROOT/p) for p in sorted(inputs)}}
    (ROOT/'textbook/print/introduction-review-manifest.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in record.items() if k not in ('inputs','fontSources')},ensure_ascii=False))


if __name__=='__main__':
    main()
