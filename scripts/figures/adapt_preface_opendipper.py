#!/usr/bin/env python3
"""Adapt native SVG captions; preserve the upstream embedded screenshots."""
import argparse
import hashlib
import io
import json
import xml.etree.ElementTree as ET
from pathlib import Path

import cairosvg
from PIL import Image
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

ROOT = Path(__file__).resolve().parents[2]
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)
p = argparse.ArgumentParser()
p.add_argument('--source-root', required=True, help='AIOS101 checkout at 9acf393')
p.add_argument('--font', required=True, help='NotoSansCJKsc-Regular.otf')
p.add_argument('--qa-dir', required=True)
args = p.parse_args()
font = TTFont(args.font)
glyphs = font.getGlyphSet()
cmap = font.getBestCmap()
qa = Path(args.qa_dir)
qa.mkdir(parents=True, exist_ok=True)
figures = ROOT / 'textbook/assets/figures'


def replace_text(group, value, x, y, size, color):
    names = [cmap[ord(c)] for c in value]
    units = font['head'].unitsPerEm
    width = sum(glyphs[n].width for n in names) * size / units
    if width > 1800 and y == 95:
        size *= 1800 / width
    group.clear()
    group.attrib.update({'aria-label': value, 'fill': color,
                         'transform': f'translate({x} {y}) scale({size/units} {-size/units})'})
    cursor = 0
    for name in names:
        pen = SVGPathPen(glyphs)
        glyphs[name].draw(pen)
        ET.SubElement(group, f'{{{NS}}}path', {'d': pen.getCommands(),
                                             'transform': f'translate({cursor} 0)'})
        cursor += glyphs[name].width


records = []
provenance = []
for index, key, title, old_title, blob, steps in [
    (1, 'global', 'OpenDipper 全球观测：发现值得追问的问题', 'OpenDipper 全球观测：从分布追问口径',
     '6ba654255cff1670906b748ac8fd9cd1a017704c',
     [('① 选对象', '从感兴趣的人、组织或项目出发'), ('② 看分布', '比较区域，找到值得追问的差异'), ('③ 追来源', '沿着指标查看材料与观察时间')]),
    (2, 'galaxy', 'OpenDipper 开源星系：看见项目之间的联系', 'OpenDipper 开源星系：从连线追问证据',
     '6e6911842151727c60b23c0578fd230a0446df16',
     [('① 找项目', '从一个任务或项目名称开始'), ('② 探关系', '沿节点与连线发现新的线索'), ('③ 提问题', '形成自己的研究问题')]),
]:
    old_number = f'0-{index+3}'
    source = Path(args.source_root) / f'textbook/assets/figures/AIOS101_Fig-00-0{index+3}_opendipper-{key}_v01.svg'
    raw = source.read_bytes()
    actual = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    assert actual == blob, f'Unexpected upstream SVG: {source}'
    svg = ET.fromstring(raw)
    embedded = [e.attrib['href'] for e in svg.findall(f'{{{NS}}}image')]
    groups = [g for g in svg.findall(f'{{{NS}}}g') if 'aria-label' in g.attrib]
    assert len(groups) == 8
    figure_id = f'AG-00-{index:02d}'
    new_title = f'图 {figure_id}　{title}'
    assert groups[0].attrib['aria-label'] == f'图 {old_number}　{old_title}'
    replace_text(groups[0], new_title, 100, 95, 38, '#1D2433')
    for i, (heading, explanation) in enumerate(steps):
        left = [265, 800, 1330][i]
        replace_text(groups[1 + i*2], heading, left, 1425, 36, '#1D2433')
        replace_text(groups[2 + i*2], explanation, left, 1494, 26, '#4B5360')
    replace_text(groups[-1], 'OpenDipper 界面快照 · 手绘导读', 655, 1584, 24, '#656577')
    svg.find(f'{{{NS}}}title').text = new_title
    assert embedded == [e.attrib['href'] for e in svg.findall(f'{{{NS}}}image')]
    native = ET.tostring(svg, encoding='utf-8', xml_declaration=True)
    name = f'ag-00-{index:02d}-opendipper-{key}'
    (qa / (name + '.svg')).write_bytes(native)
    rendered = cairosvg.svg2png(bytestring=native, output_width=2000, output_height=1660)
    (qa / (name + '.png')).write_bytes(rendered)
    target = figures / (name + '.webp')
    buffer = io.BytesIO()
    Image.open(io.BytesIO(rendered)).convert('RGB').save(buffer, 'WEBP', quality=92, method=6)
    data = buffer.getvalue()
    temporary = target.with_suffix('.webp.tmp')
    temporary.write_bytes(data)
    temporary.replace(target)
    records.append({
        'id': figure_id, 'file': target.name, 'title': title,
        'alt': ('OpenDipper 全球观测界面置于手绘观测手册中，左侧图层、中间地图和右侧观察面板引导读者选择对象、查看分布并追查来源。' if index == 1 else
                'OpenDipper 开源星系真实界面置于手绘星图档案中，两组网络展示软件与模型等对象，引导读者寻找项目、探索关系并提出研究问题。'),
        'width': 2000, 'height': 1660,
        'source': '复用 AIOS101@9acf393 的 OpenDipper 真实界面与手绘装帧；原图由维护者于 2026-10-29 提供，本版仅适配原生矢量图号、标题与导读。',
        'credit': 'OpenDipper 界面快照 · 复用 AIOS101 手绘装帧并适配导读',
        'license': '依维护者明确指令用于本课程；源项目、地图、数据及品牌的各自条件保持不变',
        'date': '2026-10-30', 'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data),
    })
    provenance.append({'id': figure_id, 'upstreamPath': source.relative_to(Path(args.source_root)).as_posix(),
                       'upstreamBlob': actual, 'upstreamCommit': '9acf393293ed629cdf1ffd1162d1257814aa57e7',
                       'embeddedImagesUnchanged': True, 'bytes': len(data),
                       'sha256': hashlib.sha256(data).hexdigest(), 'dimensions': [2000, 1660], 'webpQuality': 92})

manifest_path = figures / 'manifest.json'
manifest = json.loads(manifest_path.read_text())
manifest = records + [f for f in manifest if f['id'] not in {'AG-00-01', 'AG-00-02'}]
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
(ROOT / 'docs/review/2026-10-30-preface-od-figures.json').write_text(json.dumps(provenance, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(provenance, ensure_ascii=False, indent=2))
