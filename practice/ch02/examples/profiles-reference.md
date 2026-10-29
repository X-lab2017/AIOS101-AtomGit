# 编写者参考档案：资料阅读，不是运行报告

日期：2026-10-29；材料版本：0.2.0。下面依据本轮实际查阅的官方材料整理，并由 AI 辅助起草；仅示范如何组织记录。它不是学生提交，不证明任何学习者访问过原站，不包含 DSH 运行或真人试学。

## DeepSeek-R1：模型对象

对象范围：R1 README 中列为 DeepSeek-R1 的模型条目；没有把 Zero、Distill、其他后续版本或当前聊天服务合并为一个对象。

入口依据：[官方 R1 发布页](https://deepseek.com/en/news/deepseek-r1/)中的技术报告链接指向 deepseek-ai/DeepSeek-R1。发布页日期为 2025-01-20；课程查阅日期为 2026-10-29，两者不是同一个日期。

材料一：[README](https://github.com/deepseek-ai/DeepSeek-R1/blob/0cf78561f1d51c84a21b2190626b21116d5c68bb/README.md)的 Model Downloads 与 How to Run Locally。固定文档提交 `0cf78561f1d51c84a21b2190626b21116d5c68bb`，查阅日期 2026-10-29。

材料二：[模型文件目录](https://huggingface.co/deepseek-ai/DeepSeek-R1/tree/56d4cbbb4d29f4355bab4b9a39ccb717a14ad5ad)中的 README.md、config.json 与 model-…safetensors 条目。固定目录提交 `56d4cbbb4d29f4355bab4b9a39ccb717a14ad5ad`，查阅日期 2026-10-29。

- 项目说明：README 提供模型下载和运行说明的入口，并区分多个模型条目。
- 阅读观察：本轮查阅中找到了 DeepSeek-R1 对应链接，文件页可见说明、配置及权重分片。
- 判断边界：目录观察不能证明本机满足运行要求；没有下载或加载模型。
- 未知与问题：若以后选择某个具体条目运行，需要在哪份文档确认环境条件？

## DeepSeek Harness：工具对象

入口依据：[DSH 官方产品页](https://www.deepseek.com/en/harness/)的 GitHub 链接指向 deepseek-ai/deepseek-harness。

材料一：[中文 README](https://github.com/deepseek-ai/deepseek-harness/blob/f3803c96974ad4a94195fb97e5c637e9c2a3afe3/README.zh.md)的开头与“开发者预览”；材料二：[中文贡献指南](https://github.com/deepseek-ai/deepseek-harness/blob/f3803c96974ad4a94195fb97e5c637e9c2a3afe3/CONTRIBUTING.zh.md)的开头与参与方式列表。两者文档提交均为 `f3803c96974ad4a94195fb97e5c637e9c2a3afe3`，查阅日期 2026-10-29。

- 项目说明：README 将 DSH 介绍为智能体框架；贡献指南说明该版本暂不接受外部 PR，同时列出其他参与方式。
- 阅读观察：本轮在指南中找到了操作指南、文章和答疑等途径。没有提交 PR、发帖或与维护者取得联系。
- 待验证判断：把第一章导览完善成新手指南可能有价值；项目欢迎某类成果，不表示已经认可某一件作品。
- 未知与问题：导览是否帮助首次接触 DSH 的同学分清模型与工具？下一步需要实际阅读反馈。

## 一句话的修订示范

原句（教学构造）：“我已经全面了解并验证了 DSH。”

更准确的写法：“我查阅了固定版本的中文 README 与贡献指南，确认了项目定位和文档所列的参与方式；软件接入与任务运行尚未验证。”

好的档案可以很短，但应当让读者看到依据和边界。
