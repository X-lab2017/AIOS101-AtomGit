# 规格入口与单一正本

先读 [课程宪法](../CONSTITUTION.md)。结构化课程正本是 [course.json](course.json)：章节身份、名称、目标、任务、学习证据及顺序均由它维护。

- [课程总规格](course-spec.md)：范围与教学实现。
- [章节规格索引](chapters/README.md)：十二章的前置知识、内容边界和验收要求。
- [贯穿实践规格](practice-spec.md)：观察站、里程碑、示范与模板。
- [评价规格](assessment-spec.md)：学习成果与可观察证据。
- [内容与证据规范](content-evidence-spec.md)：背景、术语、来源及运行状态。
- [网站规格](website-spec.md)：路由、阅读体验、状态和发布。
- [视觉规范](visual-spec.md)：品牌复用、图件及手机阅读。
- [验收规格](acceptance-spec.md)：自动检查与人工评审的边界。

状态：outline 为章节提纲；draft 为正文草稿；review 为待内容评审；published 为维护者已确认可发布的正文。状态写在教材文件开头，网站读取它，不按文件存在推断完成。

修改章节结构后运行 `python scripts/sync_specs.py`，更新课程矩阵、章节规格和实践里程碑的自动区；再运行 `python scripts/check_all.py`。自动区以外的正文和人工说明不会被覆盖。
