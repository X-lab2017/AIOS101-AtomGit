# 参与课程创作

请先读 [课程宪法](CONSTITUTION.md)、[规格入口](specs/README.md) 和 [作者指南](docs/AUTHORING.md)。

一般正文创作只需编辑 textbook/chapters/CHxx.md，按章节规格补齐背景、解释、案例、任务和自查。图件放入 textbook/assets/figures/ 并登记。设计目标、任务或范围变化先改 specs/course.json，再同步规格自动区。

提出修改时说明问题、影响位置、依据和验证方式。不要预填虚构实验、反馈或贡献，不将无法确认的材料补成事实。提交前运行 `python scripts/check_all.py`。

文档反馈、资料核验、图解、教学设计、可及性改进和工程维护都属于贡献。具体开源授权待维护者统一确定；原素材与第三方许可保持原条件。
