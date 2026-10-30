"""Exact, editable diagrams for CH03; no generated text or invented UI."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
FIG = ROOT / 'textbook/assets/figures'
head = '<svg xmlns="http://www.w3.org/2000/svg" width="760" height="{height}" viewBox="0 0 760 {height}" role="img" aria-labelledby="title desc"><title id="title">{title}</title><desc id="desc">{desc}</desc><rect width="760" height="{height}" fill="#faf9f5"/><g font-family="Noto Sans CJK SC, sans-serif" fill="#1d2433">'
rows = [
    ('程序代码','具体文件、许可与第三方声明'),
    ('模型权重','确切条目、权重与上游说明'),
    ('数据材料','数据集来源、范围与使用条件'),
    ('外来图文','作者、出处与对应授权'),
    ('AI 输出','输入来源、输出内容与服务约定'),
]
parts = [head.format(height=530,title='同一份作品中的材料，需要分别确认条件',desc='五类材料分别核对。自己的新增内容另作说明。')]
parts.append('<text x="32" y="46" font-size="20" font-weight="700">选定一项材料，寻找与它对应的说明</text>')
parts.append('<path d="M32 66H728" stroke="#5146d9" stroke-width="2"/>')
for i,(label,hint) in enumerate(rows):
    y=99+i*73
    color=['#5146d9','#3f958d','#a74831','#5146d9','#3f958d'][i]
    parts.append(f'<rect x="32" y="{y-17}" width="4" height="48" fill="{color}"/><text x="53" y="{y+8}" font-size="19" font-weight="700">{label}</text><text x="246" y="{y+8}" font-size="18">{hint}</text><path d="M32 {y+43}H728" stroke="#d8d7df"/>')
parts.append('<text x="32" y="488" font-size="18" fill="#585961">自己的新增内容另作说明；未知项保留具体处理安排。</text></g></svg>')
(FIG/'ag-03-02-materials-and-conditions.svg').write_text(''.join(parts)+'\n')

parts=[head.format(height=480,title='复用与共同改进：材料、适配、评审和反馈',desc='既有成果经过理解与适配进入自己的任务，可以进一步提出改进，由评审与整合进入共同成果，再为下一次复用提供材料。')]
parts.append('<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10Z" fill="#5146d9"/></marker></defs>')
boxes=[
 (36,46,'已有成果与说明',['材料、版本与使用条件'],'#f0edf9'),
 (444,46,'用于自己的任务',['理解、适配并检查结果'],'#edf6f3'),
 (444,286,'提出具体改进',['说明问题、依据与变化'],'#f7f0e9'),
 (36,286,'更新共同成果',['整合、说明并持续维护'],'#f0edf9'),
]
for x,y,title,lines,color in boxes:
    parts.append(f'<rect x="{x}" y="{y}" width="280" height="108" rx="8" fill="{color}" stroke="#c8c4d4"/><text x="{x+140}" y="{y+39}" text-anchor="middle" font-size="20" font-weight="700">{title}</text><text x="{x+140}" y="{y+76}" text-anchor="middle" font-size="17">{lines[0]}</text>')
for path in ['M324 100H436','M584 162V278','M436 340H324','M176 278V162']:
    parts.append(f'<path d="{path}" fill="none" stroke="#5146d9" stroke-width="2" marker-end="url(#arrow)"/>')
parts.append('<text x="380" y="78" text-anchor="middle" font-size="16">理解与适配</text><text x="600" y="215" font-size="16">选择参与</text><text x="380" y="318" text-anchor="middle" font-size="16">评审与整合</text><text x="192" y="215" font-size="16">继续复用</text>')
parts.append('<text x="380" y="441" text-anchor="middle" font-size="17">实际反馈可推动再次理解与修改；复用不必都回到原项目。</text></g></svg>')
(FIG/'ag-03-03-reuse-and-collaboration.svg').write_text(''.join(parts)+'\n')

p=FIG/'manifest.json';records=json.loads(p.read_text())
old=json.loads((ROOT/'docs/review/2026-10-30-ch03-previous-figures.json').read_text())
new=[old[0],dict(old[1],width=760,height=530,date='2026-10-30'),
 dict(id='AG-03-03',file='ag-03-03-reuse-and-collaboration.svg',title='复用与共同改进：材料、适配、评审和反馈',alt='已有成果经过理解与适配进入新任务；可选择提出改进，经评审整合后更新共同成果，继续支持复用。不是所有复用都必须回馈原项目。',width=760,height=480,source='X-lab / AIOS101-AtomGit 教学分析；依据第三章对复用、贡献与维护的解释绘制。',credit='课程绘制 · 协作机制示意',license='本课程原创图件；统一对外许可待维护者确定',date='2026-10-30'),
 dict(old[2],id='AG-03-04',file='ag-03-04-improve-with-a-reader.webp',source=old[2]['source']+' 2026-10-30 原样复用并顺延编号，像素内容未修改。')]
for item in new:
    data=(FIG/item['file']).read_bytes();item.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
index=next(i for i,x in enumerate(records) if x['id'].startswith('AG-03-'))
records=[x for x in records if not x['id'].startswith('AG-03-')]
records[index:index]=new
p.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('CH03: two reused illustrations and two precise SVG diagrams')
