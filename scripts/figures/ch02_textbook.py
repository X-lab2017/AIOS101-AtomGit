"""Exact, editable reading diagrams; the DSH image contains original screenshot pixels."""
from pathlib import Path
import base64,hashlib,json,html
R=Path(__file__).resolve().parents[2];F=R/'textbook/assets/figures'
INK='#1D2433';BLUE='#5146D9';GREEN='#3F958D';ORANGE='#CB6549'
def text(x,y,s,size=24,color=INK,bold=False):
 return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}"'+(' font-weight="700"' if bold else '')+'>'+html.escape(s)+'</text>'
def rect(x,y,w,h,fill='#F6F3EB',stroke='none',rx=14):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}"/>'
def svg(w,h,content):
 return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="Noto Sans CJK SC, sans-serif">'+rect(0,0,w,h,'#FFFDFA',rx=0)+content+'</svg>'
rows=[('这是什么？','README / 模型卡','定位目标、用途和继续阅读的入口'),('怎样形成？','方法说明 / 技术报告','理解模型来源、训练方法与评估条件'),('怎样使用？','文件目录 / 运行文档','辨认权重、配置，以及实际运行所需条件'),('怎样共同建设？','贡献指南 / 讨论记录','认识问题反馈、文档、插件与代码等工作')]
c=text(42,62,'带着问题，选择材料',32,bold=True)+text(42,103,'先找到能够回答问题的地方，再向相关材料扩展。',22,color='#626777')
for i,(q,m,d) in enumerate(rows):
 y=136+i*137
 c+=rect(35,y,970,117,'#F1F0F7' if i%2==0 else '#EEF5F2')
 c+=text(60,y+40,f'0{i+1}',25,color=BLUE,bold=True)+text(125,y+40,q,26,bold=True)
 c+=text(410,y+40,m,25,color=BLUE,bold=True)+text(125,y+84,d,24)
c+=text(48,724,'许可文件：为后续复用保存入口，第三章继续阅读。',23,color=GREEN)
(F/'ag-02-01-project-reading-map.svg').write_text(svg(1040,770,c))
c=text(42,59,'同一个新模型，两种不同的来源关系',30,bold=True)
c+=rect(36,101,450,145,'#F0EDF9')+text(58,145,'Qwen2.5-Math-7B',30,color=BLUE,bold=True)+text(58,192,'已有模型：作为训练起点',24)+text(58,224,'提供此前训练形成的参数',21,color='#626777')
c+=rect(554,101,450,145,'#ECF4F1')+text(580,145,'DeepSeek-R1',30,color=GREEN,bold=True)+text(580,192,'生成模型：提供训练样本',24)+text(580,224,'通过生成的样本传递信息',21,color='#626777')
c+='<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="#626777"/></marker></defs>'
c+='<path d="M 260 247 V 302 L 400 355" fill="none" stroke="#5146D9" stroke-width="3" marker-end="url(#a)"/><path d="M 780 247 V 302 L 640 355" fill="none" stroke="#3F958D" stroke-width="3" marker-end="url(#a)"/>'
c+=text(50,307,'基础模型',23,color=BLUE)+text(800,307,'生成的样本',23,color=GREEN)
c+=rect(138,365,764,133,'#F6F3EB',stroke='#CEC9DD')+text(170,411,'DeepSeek-R1-Distill-Qwen-7B',30,bold=True)+text(170,455,'以 Qwen 为基础，利用 R1 样本进行微调',25)
c+=text(50,550,'关系来自项目原文，箭头不表示性能优劣。',24,color='#626777')+text(50,590,'图中只展示本章解释所需的两种联系。',23,color='#626777')
(F/'ag-02-02-r1-relations.svg').write_text(svg(1040,630,c))
data=base64.b64encode((R/'docs/review/sources/ch02-dsh-readme-f3803c9.jpg').read_bytes()).decode()
c=text(42,62,'读 DSH：身份、去向与阶段',31,bold=True)
items=[('项目身份','它是什么？',0,112,765,38),('文档入口','下一步去哪里？',0,193,765,40),('开发者预览','文档描述的是哪个阶段？',0,294,765,40)]
for i,(a,b,x,y,w,h) in enumerate(items):
 top=100+i*185
 c+=rect(30,top,980,161,'#F5F4F8')+text(51,top+36,a,25,color=BLUE,bold=True)+text(350,top+36,b,24)
 c+=f'<svg x="50" y="{top+58}" width="940" height="85" viewBox="{x} {y} {w} {h}" preserveAspectRatio="xMinYMid meet"><defs><clipPath id="crop{i}"><rect x="{x}" y="{y}" width="{w}" height="{h}"/></clipPath></defs><image clip-path="url(#crop{i})" href="data:image/jpeg;base64,{data}" x="0" y="0" width="1017" height="365"/></svg>'
c+=text(45,698,'原页面像素局部放大；标题和阅读问题为课程标注。',22,color='#626777')
(F/'ag-02-03-dsh-reading.svg').write_text(svg(1040,740,c))
records=json.loads((F/'manifest.json').read_text());old=[x for x in records if x['id'].startswith('AG-02-')]
archive=R/'docs/review/2026-10-30-ch02-previous-figures.json'
if not archive.exists(): archive.write_text(json.dumps(old,ensure_ascii=False,indent=2)+'\n')
records=[x for x in records if not x['id'].startswith('AG-02-')]
specs=[('01','project-reading-map',1040,770,'按照问题选择项目材料','四组真实阅读任务对应 README、模型卡、技术报告、文件目录、运行文档与贡献指南。','课程依据 GitHub README、Hugging Face Model Cards 官方文档与本章项目材料绘制。','课程原创阅读图'),('02','r1-relations',1040,630,'基础模型与训练样本：R1-Distill-Qwen 的两种联系','Qwen2.5-Math-7B 提供基础模型，DeepSeek-R1 提供生成样本，两者进入 R1-Distill-Qwen-7B 的微调过程。','依据 DeepSeek-R1 README@0cf78561f1d51c84a21b2190626b21116d5c68bb 的 Model Downloads 与 Distillation 说明绘制；非 OD 数据图。','依据项目说明重绘 · 非性能比较'),('03','dsh-reading',1040,740,'从 DSH 中文说明中读出身份、去向与阶段','真实 DSH README 的三处原像素局部放大，分别呈现框架身份、文档链接与开发者预览说明。','复用已登记截图 docs/review/sources/ch02-dsh-readme-f3803c9.jpg；对应 DSH README.zh.md@f3803c96974ad4a94195fb97e5c637e9c2a3afe3。课程新增 SVG 放大布局与阅读标注。','真实页面局部放大 · 课程阅读标注')]
for num,name,w,h,title,alt,source,credit in specs:
 file=f'ag-02-{num}-{name}.svg';b=(F/file).read_bytes()
 records.append(dict(id=f'AG-02-{num}',file=file,title=title,alt=alt,width=w,height=h,source=source,credit=credit,license='课程原创图形与标注；原项目内容及第三方标识的权利和使用条件分别保留。',date='2026-10-30',sha256=hashlib.sha256(b).hexdigest(),bytes=len(b)))
(F/'manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('CH02: three verified-content SVG figures generated')
