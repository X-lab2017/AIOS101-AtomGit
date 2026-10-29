# 来源、版本与记录类型

访问日期：2026-10-29。材料卡是课程转述，待审稿是编写者构造，均不是实际模型输出。来源版本与学习者实际运行的软件版本分别记录。

## 本次任务材料

1. [DSH README.zh.md](https://github.com/deepseek-ai/deepseek-harness/blob/f3803c96974ad4a94195fb97e5c637e9c2a3afe3/README.zh.md)：开头、开发者预览。对应 A1、A2。
2. [DSH Web UI 指南](https://github.com/deepseek-ai/deepseek-harness/blob/f3803c96974ad4a94195fb97e5c637e9c2a3afe3/docs/user/guide/index.zh.md)：开头、配置模型、选择工作区、运行任务。对应 B1—B3。

源提交均为 `f3803c96974ad4a94195fb97e5c637e9c2a3afe3`，本轮重新阅读原段。它们说明该文档版本，不能证明当前账户、环境或某次操作已经成功。原站不可访问时使用材料卡，记明只读了课程转述。

## 机制与方法背景

- [Google：语言模型入门](https://developers.google.com/machine-learning/crash-course/llm)：词元、上下文与候选选择。
- [Google：大语言模型](https://developers.google.com/machine-learning/crash-course/llm/transformers)：生成式模型利用已生成文字继续生成；本章不讲结构推导。
- [Google：提示与微调](https://developers.google.com/machine-learning/crash-course/llm/tuning)：提示改变当前输入，通常不改变参数。
- [NIST AI 600-1，2024 年 7 月版](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)：2.2 Confabulation，报告正文第 6 页（PDF 第 10 页），错误内容、引用和自信表达的边界。
- [Lewis 等，Retrieval-Augmented Generation，v4](https://arxiv.org/abs/2005.11401v4)：摘要中的外部检索与生成结合。仅用来交代 RAG 的基本思路，不借论文结果宣称本课程方法已被验证。

课程原创建议：先确定问题与判断标准，只改变材料，保留全部结果和无法控制的条件。自学材料对照与模型实测分开记录。
