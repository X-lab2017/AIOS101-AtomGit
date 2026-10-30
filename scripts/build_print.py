#!/usr/bin/env python3
"""Build the CH01 A4 reading edition from canonical Markdown and figure metadata."""
import base64
import hashlib
import html
import json
import re
from pathlib import Path

from bs4 import BeautifulSoup
from fontTools.ttLib import TTFont
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
import course_markdown as md

ROOT = Path(__file__).resolve().parents[1]
PRINT = ROOT / 'textbook/print'
SOURCE = 'textbook/chapters/CH01.md'
OUTPUT = PRINT / 'AIOS101-AtomGit-CH01.pdf'
PUBLIC = 'https://www.x-lab.info/AIOS101-AtomGit/'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    required = ['fonts/AIOSBookSerif.ttf', 'fonts/AIOSBookSans.ttf', 'fonts/AIOSBookSansBold.ttf',
                'assets/ag-01-01-report-to-brief.jpg', 'assets/ag-01-04-editorial-brief.jpg']
    missing = [name for name in required if not (PRINT/name).is_file()]
    if missing:
        raise FileNotFoundError('Extract AIOS101-CH01-print-resources.zip at the repository root; missing: ' + ', '.join(missing))
    figures = json.loads((ROOT/'textbook/assets/figures/manifest.json').read_text())
    chapter_figures = [f for f in figures if f['id'].startswith('AG-01-')]
    assert len(chapter_figures) == 4
    unit = md.unit(ROOT/SOURCE, ROOT, 'main', {}, 'CH01')
    assert '插画占位' not in unit['markdown']
    parts = []
    for section in unit['sections']:
        title = section['title']
        css = 'opening' if section['id'] == 'opening' else 'main-section'
        if title == '学习目标与阅读准备': css = 'learning'
        if title.startswith('1.1 '): css += ' first'
        if title == '参考文献': css += ' reference-section'
        heading = '' if section['id'] == 'opening' else '<h2>'+html.escape(title)+'</h2>'
        parts.append('<section class="'+css+'">'+heading+section['html']+'</section>')
    body = BeautifulSoup(''.join(parts), 'html.parser')
    for figure in body.select('figure'):
        fid = figure['id'].removeprefix('figure-').upper()
        record = next(f for f in chapter_figures if f['id'] == fid)
        image = figure.img
        path = ROOT/'textbook/assets/figures'/record['file']
        if path.suffix == '.webp': path = PRINT/'assets'/(path.stem+'.jpg')
        if path.suffix == '.svg':
            svg = re.sub(r'font-family="[^"]+"', 'font-family="BookSans"', path.read_text())
            image['src'] = 'data:image/svg+xml;base64,'+base64.b64encode(svg.encode()).decode()
        else:
            image['src'] = path.as_uri()
        for attr in ['loading','decoding','width','height']: image.attrs.pop(attr, None)
        figure.a.unwrap()
        for link in figure.figcaption.select('a'): link.decompose()
        # Remove the UI-only separator preceding the removed enlarge link.
        for string in list(figure.figcaption.children):
            if isinstance(string, str): string.replace_with(str(string).rstrip(' ·'))
    # Explicit counters work in PDF renderers even without HTML presentational hints.
    for ordered in body.select('ol[start]'):
        ordered['style'] = 'counter-reset:list-item '+str(int(ordered['start'])-1)
    # Keep fixed-source hyperlinks, but show concise canonical addresses on paper.
    from urllib.parse import urlsplit
    for paragraph in body.select('.reference-section p'):
        shown = set()
        for link in list(paragraph.select('a')):
            href = link.get('href', '')
            if href.startswith('https://'):
                parsed = urlsplit(href)
                visible_url = href
                if parsed.netloc == 'github.com' and '/blob/' in parsed.path:
                    visible_url = 'https://github.com/' + '/'.join(parsed.path.strip('/').split('/')[:2])
                if visible_url not in shown:
                    span = body.new_tag('span', attrs={'class':'reference-url'})
                    anchor = body.new_tag('a', href=href)
                    anchor.string = visible_url
                    span.append(anchor)
                    paragraph.append(span)
                    shown.add(visible_url)
                link.decompose()
        # Do not leave a separator where the second source link was removed.
        for item in list(paragraph.children):
            if isinstance(item, str) and item.strip() == '；': item.extract()
    css_path = ROOT/'scripts/print-book.css'
    title = html.escape(unit['title'].split('：', 1)[0])
    doc = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><title>第 1 章 · {title} — AI 开源通识（AtomGit 版）</title><meta name="author" content="X-lab"><meta name="description" content="第一章图文书稿，含完整正文、四幅图、练习与反馈。"></head><body>
    <header class="book-brand"><img src="{(ROOT/'site/assets/course/logo-light.svg').as_uri()}" alt="AI 开源通识"><img class="producer" src="{(ROOT/'site/assets/logo-light.svg').as_uri()}" alt="X-lab AI"></header>
    <div class="chapter-number">第一部分 认识开源</div><h1>第 1 章　{title}</h1>
    {body}
    </body></html>'''
    # Check bundled font coverage instead of silently depending on the host fonts.
    visible = BeautifulSoup(doc, 'html.parser').get_text()
    for record in chapter_figures:
        if record['file'].endswith('.svg'):
            svg = BeautifulSoup((ROOT/'textbook/assets/figures'/record['file']).read_text(), 'xml')
            visible += ''.join(t.get_text() for t in svg.select('text'))
    needed = {ord(c) for c in visible if '\u3400' <= c <= '\u9fff'}
    for file in (PRINT/'fonts').glob('*.ttf'):
        cmap = TTFont(file).getBestCmap()
        missing = needed - set(cmap)
        if missing: raise ValueError(f'Update font subset {file.name}: '+''.join(chr(c) for c in sorted(missing)))
    # SVG text uses the bundled fonts as well, keeping diagrams portable and searchable.
    doc = doc.replace('Noto Sans CJK SC, sans-serif','BookSans, sans-serif')
    work = ROOT/'tmp/pdfs'; work.mkdir(parents=True, exist_ok=True)
    (work/'CH01.html').write_text(doc)
    font_config = FontConfiguration()
    rendered = HTML(string=doc, base_url=str(ROOT)).render(stylesheets=[CSS(filename=css_path,font_config=font_config)],font_config=font_config)
    rendered.write_pdf(OUTPUT, optimize_images=True, jpeg_quality=95, pdf_identifier=('AIOS101-AtomGit-CH01-v'+unit['version']).encode())
    # Build an explicit inventory of every content/layout input that can stale the PDF.
    inputs = [SOURCE,'scripts/build_print.py','scripts/course_markdown.py','scripts/print-book.css',
              'site/assets/course/logo-light.svg','site/assets/logo-light.svg']
    inputs += [p.relative_to(ROOT).as_posix() for p in sorted((PRINT/'fonts').glob('*.ttf'))]
    for f in chapter_figures:
        inputs.append('textbook/assets/figures/'+f['file'])
        jpg = PRINT/'assets'/(Path(f['file']).stem+'.jpg')
        if jpg.exists(): inputs.append(jpg.relative_to(ROOT).as_posix())
    manifest = {'CH01': {'version':unit['version'],'source':SOURCE,'file':OUTPUT.name,'pages':len(rendered.pages),
        'paper':'A4','bytes':OUTPUT.stat().st_size,'sha256':digest(OUTPUT),
        'figureMetadataSha256':hashlib.sha256(json.dumps(chapter_figures,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),
        'inputs':{p:digest(ROOT/p) for p in sorted(set(inputs))}}}
    (PRINT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in manifest['CH01'].items() if k!='inputs'},ensure_ascii=False))


if __name__ == '__main__': main()
