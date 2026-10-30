# AI 开源通识（AtomGit 版）

**用开源来理解 AI，用 AI 来贡献开源。**

理解 AI，学会判断，在开放协作中创造。X-lab 开放实验室与奇点智能研究院联合出品，面向所有专业的学生、教师与自学者。

课程采用**理解—判断—创造—协作—迁移**五维目标，以**认识开源、理解 AI、开展 AI 创作、参与开放协作**四篇组织十二章。开源创作与 AI 创作从起步阶段贯穿，各章提供独立实践，允许自主延续与择优整合。

OpenDipper 是可选的生态数据观察入口与真实案例；DSH 和其他合适的 Agent 支持研究与创作；AtomGit 示范版本管理与开放协作。报告与交互展示保留为综合创作示范方向，具体结课要求由教学设计明确。

## 从这里开始

- [在线课程](https://www.x-lab.info/AIOS101-AtomGit/) · [引言](https://www.x-lab.info/AIOS101-AtomGit/preface/) · [全书目录](https://www.x-lab.info/AIOS101-AtomGit/outline/)
- [课程宪法](CONSTITUTION.md) · [课程总规格](specs/course-spec.md) · [十二章规格](specs/chapters/README.md)
- [章节实践与作品资源](practice/README.md) · [关于课程](textbook/about.md)
- [本轮分项评审](docs/review/2026-10-30-independent-practice-implementation.md) · [已采纳的标题与实践设计](docs/review/2026-10-30-titles-and-practice.md)
- [作者指南](docs/AUTHORING.md) · [当前状态](docs/STATUS.md) · [AI 协作者指南](AGENTS.md)

## 本轮更新与评审范围

宪法 0.3.0、引言 0.6.0、目录 0.2.0 与前三章依次更新并逐项自审。五维目标、学习矩阵和自主性阶梯保留，取消同一研究作品的强制延续。教材案例与授权分享的学生作品库预留方向，具体画像案例待后续设计。

| 章节 | 内容重点 | 独立实践 |
| --- | --- | --- |
| [第一章：开源与人工智能](textbook/chapters/CH01.md) · 0.8.0 | AI 与开源基本认识，材料与判断，人机合作 | [AI 辅助阅读与短篇表达](practice/ch01/README.md) |
| [第二章：开源项目的结构与运作](textbook/chapters/CH02.md) · 0.5.0 | 目的、成果、材料与协作，完整阅读项目 | [选择一个项目制作画像](practice/ch02/README.md) |
| [第三章：开源协作与创新](textbook/chapters/CH03.md) · 0.4.0 | 历史、复用条件、共同改进与创新 | [复用材料，改进读者说明](practice/ch03/README.md) |

前三章各五节、十五小节，保留例题、六题及反馈和十幅图；引言保留四幅图。两幅结构图的文字与新设计同步，其余有效图件复用。正文、配套材料和页面均为待评审稿，工程检查与上线不等于维护者审定或真人试学。

第四至十二章本轮仅对齐章名，正文与任务保留上一版，并明确标注待优化。已有示范和模板供选择参考，不再作为新版课程各章必交路径。

**PDF 暂不更新。**旧 PDF 和打印输入摘要保留历史交付身份；待维护者评审新正文后再统一定稿排版。本轮仓库与 Pages 不提供新版 PDF。见[打印说明](textbook/print/README.md)。

## 创作与验证

textbook/ 是 Markdown 正本，规格在 specs/，配套实践在 practice/。结构变化先改 specs/course.json，再运行 `python scripts/sync_specs.py`。按“逐章立题、研究先行、材料补充、图文共创、上线评审”推进。

```bash
python scripts/sync_specs.py --check
python scripts/check_all.py
```

main 检查通过后由 GitHub Actions 发布 Pages，PR 仅检查。决策与版本记录见 [ADR-0017](docs/decisions/ADR-0017-independent-practice-implementation.md) 和 [当前状态](docs/STATUS.md)。

## 复用与使用条件

继承 [AIOS101](https://github.com/X-lab2017/AIOS101) 的 Open Folio 1.0.0 视觉、阅读方法和 SDD 经验，按本课结构独立组织；来源和摘要见[品牌复用记录](brand/README.md)。课程源码维护于 GitHub，学习成果可在 AtomGit 等合适空间交流，当前不预设统一教学空间或自动集成。

本仓库保留源资产与第三方许可，课程及代码的统一对外许可待维护者确定，不自动新增授权。见[素材来源](site/assets/NOTICE.md)与[参与指南](CONTRIBUTING.md)。
