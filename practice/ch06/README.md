# 第六章材料包：观察或运行一次智能体任务

> 状态：review
> 版本：0.5.0

本包提供独立原稿、来源卡、教学记录与反馈，无需前章作品或编程。DSH 是可选实例，其他具备文件读写能力的 Agent 也可使用。

## 开始前

请求说明要做什么，返回说明执行后得到什么，状态说明现在进展到哪里。工作区是本次任务的文件区域；materials/guide-before.md 表示 materials 文件夹里的原稿，work/guide-candidate.md 表示 work 文件夹里的候选。以 ch06 文件夹为寻找这些相对路径的起点。.md 是可直接阅读的 Markdown 文本，# 和 ## 标记标题。工具分工与完整读取示例见[第六章](../../textbook/chapters/CH06.md)。

## 输入与完成标准

输入为[原稿](materials/guide-before.md)、[来源 A](materials/source-a.md)和[来源 B](materials/source-b.md)。任务是保留原有准确内容，新增两个阅读入口及用途，另存候选，保留原稿。目录与项目状态依据[固定来源](sources.md)。

## 观察路径：核心机制学习

阅读[完整教学过程](examples/mechanism-cards.md)，用来源与[参考候选](examples/guide-reference.md)解释 T1—T6。区分请求、返回、实际状态；讨论路径错误、无权访问和写入结果不明时的下一步。使用[记录表](work/task-record.md)写出自己的分析，再对照[自查反馈](examples/self-check.md)。

全部 T1—T6 是课程构造的情境，不是 DSH 实跑。观察路径能够完成本章核心机制目标；请记录为“依据教材教学记录”，不声称自己产生了这些文件或日志。

## 运行路径：补充真实过程

有合适环境时，先读[运行准备](setup.md)，把 ch06 文件夹本身选为工作区，提交[任务提示](prompt.txt)。实际步骤可与教学记录不同，不强制制造错误或固定轮数。保留关键请求与返回，打开 work/guide-candidate.md 检查，再提出一条基于实际结果的具体反馈并复查。没有发现用途遗漏时，不要假装发生了教材的预设问题；可以检查另一项真实改进需要。

本包没有预填学习者的 work/guide-candidate.md。参考文件在 examples/ 中；实际运行后形成的候选与记录由学习者保存。过程是否实际执行、成果是否有依据分别评价。

可请 AI 解释一段记录，再由自己对照请求、返回与文件核实。也可与同伴交换候选稿，依据真实阅读提出一条反馈并修订；把改动理由保存在原记录中，不必新增一份作业。

[回到第六章](https://www.x-lab.info/AIOS101-AtomGit/chapters/06/)。
