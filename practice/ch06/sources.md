# 来源、版本与记录边界

核对日期：2026-10-29。本轮实际阅读以下官方固定版原文；源提交均为 `f3803c96974ad4a94195fb97e5c637e9c2a3afe3`。文档版本不同于学习者实际安装的软件版本。

1. [DSH README.zh.md](https://github.com/deepseek-ai/deepseek-harness/blob/f3803c96974ad4a94195fb97e5c637e9c2a3afe3/README.zh.md)：开头的项目身份、开发者预览、运行入口与许可说明。材料 A 沿用第一章的课程转述。
2. [DSH Web UI 指南](https://github.com/deepseek-ai/deepseek-harness/blob/f3803c96974ad4a94195fb97e5c637e9c2a3afe3/docs/user/guide/index.zh.md)：开头的服务前提、配置模型、选择工作区、运行任务中的文件工具与依权限策略审批。材料 B 沿用第一章的课程转述。

3. [DSH 安全说明](https://github.com/deepseek-ai/deepseek-harness/blob/f3803c96974ad4a94195fb97e5c637e9c2a3afe3/SAFETY.zh.md)：实验性状态、沙箱限制、最小权限、专用环境与备份。该版本说明软件未经安全审计，权限与审批不能保证隔离或防止损害；本包不将提示词限制描述成安全保证。

原文明确指南从服务器已运行开始，模型需要配置，全新 Web UI 需要添加并选中工作区；运行任务段说明工具能力和条件式审批。这些是该版本的文档说明，不是本课程已经完成接入、读取、写入或发布的证据。实际操作还需对照所用版本；不承诺免费模型额度，也不承诺每一步都有同样的弹窗。

## 本包哪些不是原始证据

- `materials/guide-before.md` 是为练习构造的待修订原稿，不是实际模型输出。
- `examples/task-trace.md` 的 T1—T9 是课程设计的过程卡，不是 DSH 原始日志，不展示真实工具名称、时间戳或实际权限配置。
- `examples/self-check.md` 是预设反馈，不是同伴意见或实测结论。
- `prompt.txt` 是课程编写的任务要求，不是系统已执行这些限制的证据。

课程使用 AI 辅助起草并进行编辑核对；学习者应另记自己使用 AI 的位置。可见工具记录说明对外发生的请求和返回，不能据此重建模型完整内部思维。未显示的信息记“未显示”，不补猜。
