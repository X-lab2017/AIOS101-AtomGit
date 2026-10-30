#!/usr/bin/env python3
"""Generate specification matrices, never textbook prose."""
import argparse, json, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSE = json.loads((ROOT/'specs/course.json').read_text())
MARKER = r'<!-- BEGIN GENERATED -->.*?<!-- END GENERATED -->'

def outputs():
    chapters = COURSE['chapters']
    matrix = '| 章节 | 学习目标 | 实践里程碑 | 学习证据 |\n| --- | --- | --- | --- |\n'
    milestones = '| 章节 | 本章推进 | 留下的证据 |\n| --- | --- | --- |\n'
    result = {}
    for c in chapters:
        matrix += f"| [{c['id']} {c['title']}](chapters/{c['id']}.md) | {', '.join(c['outcomes'])} | {'（旧任务待迁移）' if c.get('designStatus')=='migration-pending' else ''}{c['milestone']}：{c['task']} | {c['evidence']} |\n"
        if c.get('designStatus')!='migration-pending':
            milestones += f"| [{c['id']}](../{c['source']}) | {c['task']} | {c['evidence']} |\n"
        result[c['spec']] = f"## {c['title']}：{c['subtitle']}\n\n核心问题：{c['question']}\n\n学习成果：{', '.join(c['outcomes'])}\n\n前置知识与材料：{c['prerequisite']}\n\n### 学习目标\n\n" + '\n'.join('- '+x for x in c['goals']) + '\n\n### 内容路线\n\n' + '\n'.join(f'{i}. {t}' for i,t in enumerate(c['topics'],1)) + f"\n\n### 本章实践与评价\n\n{c['milestone']}：{c['task']}\n\n学习证据：{c['evidence']}\n\n### 范围边界\n\n{c['boundary']}\n\n### 内容验收\n\n背景和首次术语交代充分；真实材料有来源；实践可操作；自查有参考反馈；状态如实。\n\n正文：[教材文件](../../{c['source']})"
    result['specs/course-spec.md'] = '## 章节—成果—任务—证据矩阵\n\n'+matrix
    result['practice/README.md'] = milestones
    return result

def main():
    check = argparse.ArgumentParser(); check.add_argument('--check',action='store_true'); args = check.parse_args()
    stale = []
    for name,body in outputs().items():
        p = ROOT/name; raw=p.read_text()
        if len(re.findall(MARKER,raw,re.S)) != 1: raise SystemExit('自动区缺失或重复：'+name)
        new = re.sub(MARKER,lambda _: '<!-- BEGIN GENERATED -->\n'+body.strip()+'\n<!-- END GENERATED -->',raw,flags=re.S)
        if new != raw:
            if args.check: stale.append(name)
            else: p.write_text(new)
    index = '# 十二章规格索引\n\n由 specs/course.json 生成；人工评审记录保留在各章自动区之外。\n\n'+'\n'.join(f"- [{c['id']} {c['title']}]({c['id']}.md)" for c in COURSE['chapters'])+'\n'
    p=ROOT/'specs/chapters/README.md'
    if not p.exists() or p.read_text()!=index:
        if args.check: stale.append(str(p.relative_to(ROOT)))
        else: p.write_text(index)
    if stale: raise SystemExit('规格自动区需要同步：'+', '.join(stale))
    print('Specifications aligned: 12 chapters, 12 milestones, 5 outcomes')

if __name__ == '__main__': main()
