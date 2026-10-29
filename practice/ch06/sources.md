# 来源、版本与记录边界

核对日期：2026-10-29。本轮实际阅读以下官方固定版原文；源提交均为 `f3803c96974ad4a94195fb97e5c637e9c2a3afe3`。文档版本不同于学习者实际安装的软件版本。

1. [DSH README.zh.md](https://github.com/deepseek-ai/deepseek-harness/blob/f3803c96974ad4a94195fb97e5c637e9c2a3afe3/README.zh.md)：开头的项目身份、开发者预览、运行入口与许可说明。材料 A 沿用第一章的课程转述。
2. [DSH Web UI 指南](https://github.com/deepseek-ai/deepseek-harness/blob/f3803c96974ad4a94195fb97e5c637e9c2a3afe3/docs/user/guide/index.zh.md)：开头的服务前提、配置模型、选择工作区、运行任务中的文件工具与依权限策略审批。材料 B 沿用第一章的课程转述。

3. [DSH 安全说明](https://github.com/deepseek-ai/deepseek-harness/blob/f3803c96974ad4a94195fb97e5c637e9c2a3afe3/SAFETY.zh.md)：实验性状态、沙箱限制、最小权限、专用环境与备份。该版本说明软件未经安全审计，权限与审批不能保证隔离或防止损害；本包不将提示词限制描述成安全保证。

原文明确指南从服务器已运行开始，模型需要配置，全新 Web UI 需要添加并选中工作区；运行任务段说明工具能力和条件式审批。这些是该版本的文档说明，不是本课程已经完成接入、读取、写入或发布的证据。实际操作还需对照所用版本；不承诺免费模型额度，也不承诺每一步都有同样的弹窗。

## DSH 循环的依据

4. [架构文档：轮次流程与会话日志](https://github.com/deepseek-ai/deepseek-harness/blob/f3803c96974ad4a94195fb97e5c637e9c2a3afe3/docs/architecture.zh.md#turn-flow)：本轮新读。一个步骤包含一次模型请求及工具调用，工具结果接入后续步骤，会话记录用于形成模型历史。正文只解释这些职责，不要求初学者读完整架构。

参考导览、机制卡和自查反馈均为课程编写材料，不是运行日志。机制卡只演练一次路径失败与下一步选择；本包不预填学习者的调用、产物和成功结果。
