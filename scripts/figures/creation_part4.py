#!/usr/bin/env python3
"""Editable Open Folio figures for the final course part; labels are source text."""
from pathlib import Path
from html import escape
R=Path(__file__).resolve().parents[2]
D=R/'textbook/assets/figures'
def text(x,y,s,size=28,color='#1D2433',weight=400):
 return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}">{escape(s)}</text>'
def rect(x,y,w,h,fill='#FFFFFF',stroke='#1D2433'):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
def line(x1,y1,x2,y2,color='#5146D9',dash=''):
 return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color}" stroke-width="3" fill="none"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
def save(name,title,desc,h,body):
 s=f'<svg xmlns="http://www.w3.org/2000/svg" width="800" height="{h}" viewBox="0 0 800 {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc><rect width="800" height="{h}" fill="#F6F3EB"/><g font-family="Noto Sans CJK SC, Microsoft YaHei, sans-serif">{body}</g></svg>'
 (D/name).write_text(s)
def version():
 b=text(48,62,'同一座观察站，两种地址',34,weight=700)+text(48,104,'一个跟随更新，一个回到当时。',26)
 b+=text(65,164,'提交历史',25,'#5146D9',700)+line(100,202,100,580)
 for y,n,t,d in [(220,'A','整理入口','项目、来源与作品已连接'),(375,'B','修改条件说明','让读者在行动前看见条件'),(530,'C','补充作品入口','新版本继续成长')]:
  b+=f'<circle cx="100" cy="{y}" r="15" fill="#5146D9"/>'+rect(145,y-42,585,112)+text(170,y,n+' · '+t,30,weight=700)+text(170,y+40,d,25)
 b+=line(715,375,760,375,'#3F958D')+line(760,375,760,655,'#3F958D')
 b+=rect(48,620,640,118,'#E8F0EB','#3F958D')+text(72,661,'固定提交 B 的入口',29,'#24675F',700)+text(72,702,'评审同一版；之后继续修改不改变 B。',26)
 b+=line(760,655,688,655,'#3F958D')
 b+=rect(48,770,704,118,'#EBE8FA','#5146D9')+text(72,812,'当前入口：此刻指向 C',29,'#5146D9',700)+text(72,854,'日常阅读；后续提交会带来新内容。',26)
 b+=text(48,938,'A / B / C 为教学标识，不是真实提交编号。',23)
 save('ag-10-02-version-address.svg','当前入口与固定版本各有用途','三次提交从 A 到 C 演进。固定提交 B 对应当时内容，当前入口显示最新 C，未来会变化。',980,b)
def collaboration():
 b=text(48,62,'让改动先被看见，再共同采用',33,weight=700)
 b+=text(48,104,'文档、图解与程序，都可以这样协作。',26)
 b+=text(50,176,'共同版本',29,'#5146D9',700)+text(480,176,'修改分支',29,'#3F958D',700)
 b+=line(110,220,110,880)+line(605,300,605,605,'#3F958D')
 b+='<path d="M110 250 C110 295 605 235 605 300" stroke="#3F958D" stroke-width="3" fill="none"/>'
 b+=text(165,243,'从约定版本开始',25)
 for x,y,c in [(110,250,'#5146D9'),(110,535,'#5146D9'),(605,340,'#3F958D'),(605,500,'#3F958D'),(110,880,'#5146D9')]:
  b+=f'<circle cx="{x}" cy="{y}" r="13" fill="{c}"/>'
 b+=rect(370,365,380,96,'#E8F0EB','#3F958D')+text(394,403,'修改并提交',29,weight=700)+text(394,440,'例如修复一个文档链接',24)
 b+=text(148,523,'读者仍可使用',26)+text(148,562,'现有内容',26)
 b+=rect(292,590,458,150,'#FFFFFF','#3F958D')+text(318,629,'PR：请求把修改合进来',27,weight=700)+text(318,671,'读差异、检查结果、讨论',25)+text(318,710,'有必要就修订，再检查',25)
 b+='<path d="M605 740 V770 H110 V880" stroke="#F27A59" stroke-width="3" stroke-dasharray="8 7" fill="none"/>'
 b+=text(245,817,'符合规则后，由有权限的人合并',25)
 b+=text(148,887,'共同版本纳入改动，再复查',29,weight=700)
 b+=line(48,942,752,942,'#B7B3AA')+text(48,986,'没有写权限？',27,weight=700)+text(48,1028,'若项目允许，可在自己的 Fork 中修改，',26)+text(48,1068,'再向原项目提出 PR；否则按规则反馈。',26)
 b+=text(48,1120,'创建请求 ≠ 已合并；关闭请求也可能未合并。',24)
 save('ag-11-01-review-branches.svg','修改先被讨论，再进入共同版本','共同版本与修改分支从同一基线出发；在分支提交并以PR讨论，按规则和权限合并后再核对。Fork作为没有原仓库写权限时的可选路径。',1160,b)
def transfer():
 b=text(48,62,'带走方法，重新建立结论',34,weight=700)
 b+=text(48,104,'迁移需要比较条件，并实际检验。',26)
 b+=rect(48,150,328,196,'#EBE8FA','#5146D9')+text(72,193,'旧作品的经验',29,'#5146D9',700)+text(72,243,'DSH 观察站',27)+text(72,285,'对象、条件与入口',25)+text(72,325,'已有行动与证据',25)
 b+=rect(424,150,328,196,'#F9E7DE','#B65539')+text(448,193,'新任务的条件',29,'#98462E',700)+text(448,243,'另一个 AI 项目',27)+text(448,285,'对象可能不同',25)+text(448,325,'材料需要重新查',25)
 b+=line(210,346,210,400)+line(590,346,590,400,'#B65539')+line(210,400,590,400)
 b+=line(400,400,400,442)
 b+=rect(85,442,630,170,'#FFFFFF','#5146D9')+text(112,487,'保留方法，调整步骤',31,weight=700)+text(112,535,'先辨认对象，再查来源与条件',27)+text(112,579,'不能只替换项目名或照搬结论',26)
 b+=line(400,612,400,668)
 b+=rect(85,668,630,160,'#E8F0EB','#3F958D')+text(112,714,'做一次新的尝试',31,'#24675F',700)+text(112,758,'形成小成果，按预定办法检查',26)+text(112,801,'说明结果、差异与仍未验证的部分',25)
 b+='<path d="M715 748 H760 V920 H85" fill="none" stroke="#3F958D" stroke-width="3"/>'
 b+=text(85,896,'用新发现修订自己的技能条目',28,weight=700)
 b+=text(48,982,'阅读证据支持文档判断；运行效果需要运行证据。',24)
 save('ag-12-01-transfer.svg','方法可以迁移，条件必须重查','旧作品的经验与新任务的条件共同进入判断；保留方法、调整步骤、完成新尝试，再以实际结果修订能力说明。',1030,b)
if __name__=='__main__':
 version()
 collaboration()
 transfer()
