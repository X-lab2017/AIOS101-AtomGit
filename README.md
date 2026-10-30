# AI 开源通识（AtomGit 版）

**用开源来理解 AI，用 AI 来贡献开源。**

理解 AI，学会判断，在开放协作中创造。X-lab 开放实验室与奇点智能研究院联合出品，面向所有专业的学生、教师与自学者。

**开源北斗 OpenDipper（OD）**是全球开源生态的数据观测与研究项目。本课程将它同时作为学习教学工具与真实项目案例，结合 DeepSeek 模型、DSH 智能体工具和 AtomGit 协作实践。

课程采用 **理解—判断—创造—协作—迁移** 的 AI 时代五维学习目标框架。综合大作业是利用 OpenDipper 完成**专业开源研究报告及配套动态展示页面**，将报告、页面及相关材料作为同一个开源项目托管在 AtomGit，积累个人技能集与作品集。

**当前迁移状态：**[宪法 v0.2.1](CONSTITUTION.md)、[序言](https://www.x-lab.info/AIOS101-AtomGit/preface/)与[关于课程](https://www.x-lab.info/AIOS101-AtomGit/about/)已对齐新的设计理念；十二章与实践材料将按 OpenDipper 主线逐步完善。实施安排见 [ADR-0007](docs/decisions/ADR-0007-opendipper-research-course.md)，本轮简化原则见 [ADR-0008](docs/decisions/ADR-0008-constitution-and-about.md)。

## 从这里开始

- [在线评审站](https://www.x-lab.info/AIOS101-AtomGit/)
- [课程宪法](CONSTITUTION.md) · [课程总规格](specs/course-spec.md) · [十二章规格](specs/chapters/README.md)
- [作者指南](docs/AUTHORING.md) · [当前状态](docs/STATUS.md) · [AI 协作者指南](AGENTS.md)
- [实践与迁移说明](practice/README.md) · [示范结构](practice/demo/README.md) · [实践模板](practice/template/README.md)

## 已上线内容与迁移范围

宪法版本为 0.2.1，课程结构为 0.2.3；各章按新主线逐步迁移。现有四部分十二章图文评审稿保留供阅读与迁移复用，下列内容说明属于已上线版本，其中的旧称与任务将按新宪法逐章调整。示范不代表任务实测或社区贡献已经完成。

[序言 0.4.0](textbook/preface.md)从国家发展方向与全球 AI 普惠引出学习必要性，再走进 OpenDipper 与《2026 全球开源发展报告》的真实实践，连接研究报告、动态页面与 AtomGit 综合项目。三幅手绘图按阅读顺序统一编号。见[本轮图文记录](docs/review/2026-10-30-preface-policy.md)。

第一部分三章已完成本轮教材联动：第一章 0.7.1、第二章 0.4.1、第三章 0.3.0。统一章、节、小节标题与学习单元，沿用同一简报形成“创作—项目阅读—复用与改进”的递进。详见 [本轮评审](docs/review/2026-10-30-first-part-textbook.md)；前三章早期的 [联合记录](docs/review/2026-10-29-ch01-03.md)保留历史身份。

- [第一章：初识 AI 开源](textbook/chapters/CH01.md)——四幅图与 [练习包](practice/ch01/README.md)，从真实材料与 OD 观察形成一页研究简报。
- [第二章：打开一个开源项目](textbook/chapters/CH02.md)——两幅图与 [材料包](practice/ch02/README.md)，从项目全貌、材料与协作建立档案。
- [第三章：开源的力量](textbook/chapters/CH03.md)——四幅图与 [九文件复用包](practice/ch03/README.md)，理解开放机制，完成材料复用与读者导向改进。

三个 A4 单章和第一部分合订 PDF 在对话中单独交付，不纳入 GitHub 或 Pages。排版方法见 [打印说明](textbook/print/README.md)。

- [第四章：模型怎样学会本领](textbook/chapters/CH04.md)——[纸面实验材料包](practice/ch04/README.md)，用教学合成数据理解训练、检验与适用边界。

- [第五章：AI 为什么会答错](textbook/chapters/CH05.md)——[生成对照材料包](practice/ch05/README.md)，理解生成与上下文，并为同一导览做一次有依据的修订。

- [第六章：从回答到行动](textbook/chapters/CH06.md)——[任务追踪材料包](practice/ch06/README.md)，分清读取、生成、执行和人的授权核验。

- [第七章：找到值得解决的问题](textbook/chapters/CH07.md)——[设计材料包](practice/ch07/README.md)，围绕具体读者选择问题、范围和标准。
- [第八章：把想法变成作品](textbook/chapters/CH08.md)——[创作材料包](practice/ch08/README.md)，从草图到实际候选，说明自己的关键取舍。
- [第九章：让作品经得起检验](textbook/chapters/CH09.md)——[检验材料包](practice/ch09/README.md)，核验、修订并比较前后。

- [第十章：让别人用上你的成果](textbook/chapters/CH10.md)——[分享材料包](practice/ch10/README.md)，用浏览器整理版本、检查访问和阅读路径。
- [第十一章：在反馈中共同改进](textbook/chapters/CH11.md)——[协作材料包](practice/ch11/README.md)，从具体问题、差异走向回应与改进。
- [第十二章：建立个人技能集与作品集](textbook/chapters/CH12.md)——[迁移材料包](practice/ch12/README.md)，从代表作品提炼方法，在新项目问题中检验。

[序言](textbook/preface.md)与全部十二章现为图文评审稿。第四至九章为 0.3.0，第十至十二章为 0.2.0；后者已逐章自审并联合对齐，见[本轮记录](docs/review/2026-10-30-ch10-12.md)。第七至九章采用[观察站产品修订版](docs/review/2026-10-29-ch07-09-realignment.md)，不再沿用旧的角色地图主线。工具和平台实操、真人试学仍需继续验证。

## 创作方式

只需在 textbook/chapters/ 中创作 Markdown 正文；目录、阅读页、状态与下载由构建生成。结构变化先修改 specs/course.json，再同步规格。

```bash
python scripts/sync_specs.py --check
python scripts/check_all.py
```

main 检查通过后由 GitHub Actions 发布 Pages。PR 仅检查。详见 [作者指南](docs/AUTHORING.md)。

## 复用与来源

继承 [AIOS101](https://github.com/X-lab2017/AIOS101) 的 Open Folio 1.0.0 视觉、阅读方法和 SDD 经验，按新大纲独立组织。固定来源、资产哈希和适配说明见 [品牌复用记录](brand/README.md)。

课程源码维护于 GitHub，AtomGit 承载学习者的专题研究成果与社区实践。当前尚未配置统一 AtomGit 教学空间，不预设自动集成。

## 使用条件

本仓库保留源资产与第三方许可，课程及代码的统一对外许可待维护者确定，不自动新增授权。见 [素材来源](site/assets/NOTICE.md) 与 [参与指南](CONTRIBUTING.md)。

