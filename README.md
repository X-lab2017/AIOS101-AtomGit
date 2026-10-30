# AI 开源通识（AtomGit 版）

**用开源来理解 AI，用 AI 来贡献开源。**

理解 AI，学会判断，在开放协作中创造。X-lab 开放实验室与奇点智能研究院联合出品，面向所有专业的学生、教师与自学者。

课程采用**理解—判断—创造—协作—迁移**五维目标，以**认识开源、理解 AI、开展 AI 创作、参与开放协作**四篇组织十二章。开源创作与 AI 创作从起步阶段贯穿，各章提供独立实践，允许自主延续与择优整合。

OpenDipper 是可选的生态数据观察入口与真实案例；DSH 和其他合适的 Agent 支持研究与创作；AtomGit 示范版本管理与开放协作。报告与交互展示保留为综合创作示范方向，具体结课要求由教学设计明确。

## 从这里开始

- [在线课程](https://www.x-lab.info/AIOS101-AtomGit/) · [引言](https://www.x-lab.info/AIOS101-AtomGit/preface/) · [全书目录](https://www.x-lab.info/AIOS101-AtomGit/outline/)
- [课程宪法](CONSTITUTION.md) · [课程总规格](specs/course-spec.md) · [十二章规格](specs/chapters/README.md)
- [章节实践与作品资源](practice/README.md) · [关于课程](textbook/about.md)
- [第三部分逐章与联合评审](docs/review/2026-10-31-third-part-textbook.md) · [第三部分研究与取舍](docs/research/2026-10-31-third-part-source-map.md)
- [第二部分逐章评审](docs/review/2026-10-30-second-part-textbook.md) · [已采纳的标题与实践设计](docs/review/2026-10-30-titles-and-practice.md)
- [作者指南](docs/AUTHORING.md) · [当前状态](docs/STATUS.md) · [AI 协作者指南](AGENTS.md)

## 第一部分已审定基线

宪法 0.3.0、引言 0.6.0、目录 0.2.0 与前三章依次更新并逐项自审，维护者于 2026-10-30 确认本次内容全部评审通过，见 [ADR-0018](docs/decisions/ADR-0018-first-part-content-approved.md)。五维目标、学习矩阵和自主性阶梯保留，取消同一研究作品的强制延续。教材案例与授权分享的学生作品库预留方向，具体画像案例待后续设计。

| 章节 | 内容重点 | 独立实践 |
| --- | --- | --- |
| [第一章：开源与人工智能](textbook/chapters/CH01.md) · 0.8.0 | AI 与开源基本认识，材料与判断，人机合作 | [AI 辅助阅读与短篇表达](practice/ch01/README.md) |
| [第二章：开源项目的结构与运作](textbook/chapters/CH02.md) · 0.5.0 | 目的、成果、材料与协作，完整阅读项目 | [选择一个项目制作画像](practice/ch02/README.md) |
| [第三章：开源协作与创新](textbook/chapters/CH03.md) · 0.4.0 | 历史、复用条件、共同改进与创新 | [复用材料，改进读者说明](practice/ch03/README.md) |

前三章各五节、十五小节，保留例题、六题及反馈和十幅图；引言保留四幅图。两幅结构图的文字与新设计同步，其余有效图件复用。本轮正文与配套材料已通过维护者内容评审；真人试学、全部工具流程与新版打印排版另行验证。

## 第二部分：理解 AI（0.5.0，待内容评审）

按“逐章立题、研究先行、材料补充、图文共创、上线评审”完成第四至六章。保留第一部分基线，逐章自审后进入下一章，研究取舍见[来源记录](docs/research/2026-10-30-second-part-source-map.md)。

本轮增加章首阅读起点、必要术语与基本概念、完整操作与算式解释，并将 AI 辅助、独立核对和读者反馈融入原有实践；同步收敛图件显示尺度。见[入门阅读与对齐评审](docs/review/2026-10-31-second-part-reading-ux.md)。

| 章节 | 重点 | 独立实践 |
| --- | --- | --- |
| [第四章：机器学习基础](textbook/chapters/CH04.md) | 样本、参数、误差与泛化 | [比较学习结果，解释适用条件](practice/ch04/README.md) |
| [第五章：大语言模型的生成与局限](textbook/chapters/CH05.md) | 上下文、生成、来源与比较 | [改善材料组织，比较生成结果](practice/ch05/README.md) |
| [第六章：智能体的工作机制](textbook/chapters/CH06.md) | 工具请求、执行、反馈与检查 | [观察或运行一次智能体任务](practice/ch06/README.md) |

三章各自有完整材料、例题、实践、六道练习与反馈；复用六幅有效图件，新增三幅原创矢量图。Neo Lee 课件、AIInfra、李博杰及贡献者的书与 Chip Huyen 配套资源分别按问题选材，不复制整份资料或将摘要视为原书全文。当前为编写自审完成、等待维护者评审；未宣称真实试学或工具实跑验收。

## 第三部分：开展 AI 创作（0.4.0，待内容评审）

沿用已审定章目与入门阅读基线，按第七章→第八章→第九章完成研究、图文编写与逐章自审。Neo Lee 课件用于需求、范围、流程、原型与持续改进；项目材料按用途选取，来源版本及取舍见[研究记录](docs/research/2026-10-31-third-part-source-map.md)。

| 章节 | 重点 | 独立实践 |
| --- | --- | --- |
| [第七章：创作选题与方案设计](textbook/chapters/CH07.md) | 需要、假设、范围、材料与完成标准 | [根据 AIInfra 材料设计一件作品](practice/ch07/README.md) |
| [第八章：作品的构建与表达](textbook/chapters/CH08.md) | 内容结构、图文依据、原型与人机合作 | [依据给定方案制作 Agent 概念导览](practice/ch08/README.md) |
| [第九章：作品的评价与改进](textbook/chapters/CH09.md) | 主张核验、表达一致、任务走查与复查 | [评议并改进 aie-book 资源导览](practice/ch09/README.md) |

三章均补齐章首术语、概念解释、材料卡、三例题、六道练习与反馈。复用两幅插画，重绘三幅原创 SVG；图中文字按正文尺度控制。三套材料包各自可开始，方法递进不要求作品串联。编写者示范、AI 建议和真人试读分别记录，不虚构实际运行或学习效果。见[逐章与联合评审](docs/review/2026-10-31-third-part-textbook.md)。

第十至十二章仍保留上一版正文与任务，并明确标注待优化。已有示范和模板供选择参考，不再作为新版课程各章必交路径。

**PDF 暂不更新。**旧 PDF 和打印输入摘要保留历史交付身份；第一部分已审定，第二、三部分待维护者评审；后续再统一排版并验收。本轮仓库与 Pages 不提供新版 PDF。见[打印说明](textbook/print/README.md)。

## 创作与验证

textbook/ 是 Markdown 正本，规格在 specs/，配套实践在 practice/。结构变化先改 specs/course.json，再运行 `python scripts/sync_specs.py`。按“逐章立题、研究先行、材料补充、图文共创、上线评审”推进。

```bash
python scripts/sync_specs.py --check
python scripts/check_all.py
```

main 检查通过后由 GitHub Actions 发布 Pages，PR 仅检查。决策与版本记录见 [ADR-0021](docs/decisions/ADR-0021-third-part-creation-upgrade.md) 和 [当前状态](docs/STATUS.md)。

## 复用与使用条件

继承 [AIOS101](https://github.com/X-lab2017/AIOS101) 的 Open Folio 1.0.0 视觉、阅读方法和 SDD 经验，按本课结构独立组织；来源和摘要见[品牌复用记录](brand/README.md)。课程源码维护于 GitHub，学习成果可在 AtomGit 等合适空间交流，当前不预设统一教学空间或自动集成。

本仓库保留源资产与第三方许可，课程及代码的统一对外许可待维护者确定，不自动新增授权。见[素材来源](site/assets/NOTICE.md)与[参与指南](CONTRIBUTING.md)。
