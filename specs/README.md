# 规格入口与单一正本

先读 [课程宪法 v0.3.0](../CONSTITUTION.md)。五维目标为“理解—判断—创造—协作—迁移”。各章实践独立起步，允许延续和整合成果；报告与交互展示是综合示范方向。OpenDipper 提供可选材料，DSH 及其他合适工具支持创作。

**实施状态：**course.json 为 0.5.0；宪法、引言、目录、关于课程、前三章与配套实践已通过维护者内容评审，见 [ADR-0018](../docs/decisions/ADR-0018-first-part-content-approved.md)。CH04—06 已完成正文与独立实践升级，当前为 review，见 [第二部分评审](../docs/review/2026-10-30-second-part-textbook.md)；CH07—09 已完成正文及独立实践升级，为 0.4.0 review，见[第三部分评审](../docs/review/2026-10-31-third-part-textbook.md)；CH10—12 仍标记正文、任务待迁移。内容审定、真人试学与打印验收分别记录；本次不重建 PDF。

CH04—06 正文及材料包现为 0.5.0，已补齐入门解释和人机合作支持，并按正文字号控制图件尺度，见[本轮阅读评审](../docs/review/2026-10-31-second-part-reading-ux.md)。第二部分章目、目标与映射未变；本轮第三部分结构与任务迁移使课程元数据更新至 0.5.0。

- [课程总规格](course-spec.md)：范围与教学实现。
- [引言规格](preface-spec.md)：课程方法、五维目标、学习矩阵、阶梯与独立实践。
- [目录评审规格](outline-review-spec.md) · [全书目录](../textbook/contents-review.md)：四篇十二章与前三章三级标题，已通过本轮内容评审。
- [章名与独立实践的新一轮评审](../docs/review/2026-10-30-titles-and-practice.md)：标题建议、各章实践、工具分工与作品库；本轮据此实施，见 ADR-0017。
- [章节规格索引](chapters/README.md)：十二章的前置知识、内容边界和验收要求。
- [章节实践规格](practice-spec.md)：独立任务、可选综合创作、案例和作品库设计。
- [评价规格](assessment-spec.md)：学习成果与可观察证据。
- [教材体例规范](textbook-style-spec.md)：书籍与在线自学共用正文、概念解释、例题和练习反馈。
- [打印书稿规范](print-spec.md)：单一正文、多端呈现、PDF 一致性与逐页验收。
- [内容与证据规范](content-evidence-spec.md)：背景、术语、来源及运行状态。
- [网站规格](website-spec.md)：路由、阅读体验、状态和发布。
- [视觉规范](visual-spec.md)：品牌复用、图件及手机阅读。
- [验收规格](acceptance-spec.md)：自动检查与人工评审的边界。

状态：outline 为章节提纲；draft 为正文草稿；review 为待内容评审；published 为维护者已确认可发布的正文。状态写在教材文件开头，网站读取它，不按文件存在推断完成。

修改章节结构后运行 `python scripts/sync_specs.py`，更新课程矩阵、章节规格和实践里程碑的自动区；再运行 `python scripts/check_all.py`。自动区以外的正文和人工说明不会被覆盖。

宪法只规定稳定方向与原则；教学、技术和实施细节在相应规格中按需设计。“关于课程”是面向读者的理念说明，不复制内部验收与操作清单。分层原则见 [ADR-0008](../docs/decisions/ADR-0008-constitution-and-about.md)。
