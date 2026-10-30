# 第三章研究依据与第一部分更新设计

日期：2026-10-30（北京时间）。范围：第三章独立评审稿，随后联动 CH01—03 的标题、概念、实践与打印稿；不推进第四章。读者为各专业大学生和自学者，无编程先修。依据为宪法 0.2.1、前三章现稿及维护者确认的六节更新策略。

## 立题与章际分工

第一章建立整体认识并以给定材料开始创作；第二章独立选择项目材料、形成档案与修订；第三章解释开放怎样支持复用与共同创造，并完成一项材料处理、一次读者导向改进及必要说明。主线保持“科技研究与咨询：开源生态专题”。

第三章题名采用“开源的力量：从成果复用到共同创造”；第二章采用“打开一个开源项目：从项目全貌到材料与协作”。第一章“初识 AI 开源”保持。节标题准确指向知识或任务，小节标题说明具体关系；实践末节统一为任务与完成要求、参考成果与分析、自我评价与后续学习。以教学内容决定节数，不强行凑齐。

## 研究问题与证据

| 问题 | 主要依据与读取范围 | 判断及采用方式 |
| --- | --- | --- |
| 开放怎样支持共同创造？ | 原版 AIOS101 CH02 全文，固定提交 9acf393；Open Source Guides 的贡献类型与沟通段落 | 解释材料、授权、适配、评审、维护各自作用；机制为教材分析，不写成自动产生公共价值的因果定律 |
| 三个历史窗口说明什么？ | GNU 初始声明及自由软件定义的既有资料，本轮官方索引摘录；Linux RELNOTES-0.01 全文；OSI history 与 OSD 全文 | 保留历史问题，不扩写英雄传记。GNU/FSF 原页面本轮多次打开超时，未把索引命中称为全文重读；FSF 官方历史与 GNU 文集索引交叉支持 1983 声明、1984 开始 |
| 普通学生怎样实际复用？ | DSH 固定 LICENSE；Open Source Guides README、notices、完整 CC BY 4.0 LICENSE、how-to-contribute 的非代码贡献段落；CC 官方摘要 | 以真实知识材料作为主例，DSH MIT 作短对照；纸面给出核心材料与完整署名示范，原许可随包保存 |
| 小改动怎样进入项目？ | AIInfra PR #364 正文、文件差异、issue comments、reviews API | 2025-12-04 提出、2025-12-22 合并；一文件一行替换，16 字节改为 2 字节。没有公开评论或正式 review 记录，不能编写讨论对话或虚构审查细节 |
| 怎样收束第一部分？ | CH01 简报、CH02 档案、宪法五维目标 | 同一简报逐次改善。编写者示范明确身份；协作准备与真实贡献、预设反馈与真人试读分别记录 |

## 固定来源与使用边界

- Open Source Guides：`e7ac98e94600c5eea834f9a026c000d26b28df24`；README、notices、LICENSE、`_articles/how-to-contribute.md`。原文其他人物引语、头像、截图不随例子复制。内容版权归 Open Source Guides authors；内容 CC BY 4.0，代码 CC0 及例外另见 notices，不能混用。
- AIInfra PR #364：<https://github.com/Infrasys-AI/AIInfra/pull/364>；文件 `05Infer/06CompDistill/05Quantization01.md`；合并提交 `b97c0385ba07a62a717d82a0e7aed2927f12fc35`。PR 概述将语境简写为 8-bit；教材按实际差异说明“从 2 字节到 1 字节”，不声称 8 位本身占 2 字节，不外推整机内存与速度。
- DSH：`f3803c96974ad4a94195fb97e5c637e9c2a3afe3`；本轮重新读取完整 LICENSE，与包内原文一致。只对选定原材料解释 MIT，不为学生整份报告选许可。
- OpenDipper：沿用 CH02 固定快照 `465c4737a36c4c5e67e39f971b3e09d28d1e84f5`；应用许可待定的历史状态保持。Issue #19 仅表示任务邀请，不能和 AIInfra PR 拼成连续事件。
- CC 官方摘要：<https://creativecommons.org/licenses/by/4.0/deed.en>；完整条款使用上述项目原文。简短课堂说明不取代完整条件，来源、修改、许可与免责入口一起交代。
- Linux：<https://www.kernel.org/pub/linux/kernel/Historic/old-versions/RELNOTES-0.01>；OSI：<https://opensource.org/about/history-of-the-open-source-initiative>、<https://opensource.org/osd>。
- GNU 初始声明：<https://www.gnu.org/gnu/initial-announcement.html>；自由软件定义：<https://www.gnu.org/philosophy/free-sw.html>；交叉资料为 <https://www.gnu.org/doc/fsfs-ii-2.pdf> 官方索引中的原始声明与 <https://www.fsf.org/history/> 官方索引。此限制保留在编辑研究记录中。

## 插图与交付

保留历史人物图和读者共同修订图；精简材料分类 SVG，使其服务于“具体对象—具体条件”。新增精确协作机制图，表达复用与共同改进的分支及反馈；不让历史插画代替机制解释。已有肖像参考的出版使用事项见原 provenance，继续作为评审稿边界。

先完成 CH03 独立正文、材料与 PDF 排版核对，再联动前两章各级标题、衔接段与任务名称，生成三个单章及带连续页码的第一部分合订稿。目标、材料、例题、练习与反馈在纸面完整；账号与文件操作留配套包。网页构建、排版检查、维护者内容评审和真人试学分别记录。
