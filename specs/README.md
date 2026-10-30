# 规格入口与单一正本

先读 [课程宪法 v0.2.1](../CONSTITUTION.md)。学习目标采用“理解—判断—创造—协作—迁移”五维框架，综合项目为借助 OpenDipper 完成研究报告、动态展示页面与 AtomGit 开源交付。

**迁移状态：**[course.json](course.json) 仍为已实施的 0.1.0 结构正本，维护现有章节身份、名称、目标、任务、证据及顺序；“关于课程”已同步新理念，下游章节、实践和其他页面仍逐步对齐。其旧任务用于定位现有内容，不能覆盖 v0.2 目标。先按 [ADR-0007](../docs/decisions/ADR-0007-opendipper-research-course.md) 完成新规格与逐章迁移，再同步生成产物。

- [课程总规格](course-spec.md)：范围与教学实现。
- [序言规格](preface-spec.md)：读者动机、入门背景、贯穿实践与开篇图件。
- [章节规格索引](chapters/README.md)：十二章的前置知识、内容边界和验收要求。
- [贯穿实践规格](practice-spec.md)：新综合项目要求与待迁移的实践、示范及模板。
- [评价规格](assessment-spec.md)：学习成果与可观察证据。
- [内容与证据规范](content-evidence-spec.md)：背景、术语、来源及运行状态。
- [网站规格](website-spec.md)：路由、阅读体验、状态和发布。
- [视觉规范](visual-spec.md)：品牌复用、图件及手机阅读。
- [验收规格](acceptance-spec.md)：自动检查与人工评审的边界。

状态：outline 为章节提纲；draft 为正文草稿；review 为待内容评审；published 为维护者已确认可发布的正文。状态写在教材文件开头，网站读取它，不按文件存在推断完成。

修改章节结构后运行 `python scripts/sync_specs.py`，更新课程矩阵、章节规格和实践里程碑的自动区；再运行 `python scripts/check_all.py`。自动区以外的正文和人工说明不会被覆盖。

宪法只规定稳定方向与原则；教学、技术和实施细节在相应规格中按需设计。“关于课程”是面向读者的理念说明，不复制内部验收与操作清单。分层原则见 [ADR-0008](../docs/decisions/ADR-0008-constitution-and-about.md)。
