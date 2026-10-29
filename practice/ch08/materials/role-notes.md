# 可选补充：角色地图的机制材料

课程转述，2026-10-30（北京时间）。不是实际 DSH 运行记录；R 编号仅用于本包，不与早期 A/B 编号混用。

- R1：DSH 的架构把模型适配、工具、会话日志和智能体循环等作为可组合部分。一个步骤涉及模型请求及其工具调用；工具结果进入后续处理。模型可以生成内容或工具请求，具体文件动作由工具执行。[来源 1]
- R2：固定版 Web UI 指南从服务已启动开始，包含模型配置和工作区选择。工作区是当前任务使用的文件位置。指南说明智能体可以读取、编辑工作区文件；某操作是否审批取决于权限策略。[来源 2]
- R3：DSH 是 DeepSeek 开发的开源智能体框架；固定版 README 标为开发者预览。材料所用提交不是本次安装版本的证明。[来源 3]
- R4：AtomGit 提供仓库、版本管理与协作能力。本课程把整理作品、分享和共同改进安排在后续篇章；本地保存与平台分享是不同动作。本例没有验证 DSH 与 AtomGit 的自动集成。[来源 4；课程任务设计]

## 原始来源

1. [DSH 架构：轮次流程](https://github.com/deepseek-ai/deepseek-harness/blob/f3803c96974ad4a94195fb97e5c637e9c2a3afe3/docs/architecture.zh.md#turn-flow)
2. [DSH Web UI 指南](https://github.com/deepseek-ai/deepseek-harness/blob/f3803c96974ad4a94195fb97e5c637e9c2a3afe3/docs/user/guide/index.zh.md)
3. [DSH 中文 README](https://github.com/deepseek-ai/deepseek-harness/blob/f3803c96974ad4a94195fb97e5c637e9c2a3afe3/README.zh.md)
4. [AtomGit 产品介绍](https://docs.atomgit.com/docs/start/)（访问日期：2026-10-30；只使用仓库与协作职责，不转用营销统计）

作品应保留具体原始链接和自己的修改说明。旧导览中的 A/B 标记仍对应旧导览原有材料，本卡不替代那套编号。若无法提供编号对应的原材料，给作品使用完整原始链接，避免悬空编号。
