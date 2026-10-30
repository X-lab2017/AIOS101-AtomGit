# 材料 B：从关系中发现线索

以下是课程依据 OpenDipper 固定数据并与上述实际界面对照整理的观察卡。模型网络的数据观察日为 2026 年 8 月 5 日；本轮查阅及截图日期为 2026 年 10 月 30 日。模型信息来自 Hugging Face 公开元数据。**Hugging Face** 是分享模型、数据与应用的平台；**元数据**可先理解为描述这些对象的信息，例如名称、发布账号和声明的关联。

- **B1 · 身份。**模型星系中存在 `deepseek-ai/DeepSeek-R1` 节点，类型为模型，任务类别为文本生成；其项目主页指向 Hugging Face 上的对应模型页面。
- **B2 · 观察。**该节点与 `unsloth/DeepSeek-R1-GGUF` 存在“模型派生关联”。这里保留完整名称作为检索线索，暂时不需要理解 GGUF 文件格式。
- **B3 · 依据。**这是来源元数据明确记录的关联。OD 的关系说明提供来源入口，并说明当前按无向关系展示；这条记录本身不是效果比较，也不足以确定派生方向。
- **B4 · 追问。**如果想知道关联对象改变了什么、为谁解决什么问题，应继续阅读它的项目说明。仅凭相似名称、节点大小或一条连线，不能替代这一步。


来源：[OpenDipper 模型网络固定数据](https://github.com/X-lab2017/open-dipper/blob/465c4737a36c4c5e67e39f971b3e09d28d1e84f5/public/data/galaxy/model.json)；[关系与数据口径说明](https://github.com/X-lab2017/open-dipper/blob/465c4737a36c4c5e67e39f971b3e09d28d1e84f5/docs/OPEN_GALAXY.md)。节点标识为 `hf:model:deepseek-ai/DeepSeek-R1`。本卡是课程整理的观察，不等于你已经亲自操作；请按真实情况记录。
