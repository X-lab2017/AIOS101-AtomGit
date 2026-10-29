# AI 开源通识（AtomGit 版）

**用开源来理解 AI，用 AI 来贡献开源。**

理解 AI，学会判断，在开放协作中创造。X-lab 出品，面向所有专业的学生、教师与自学者。

DeepSeek 模型与 DSH 智能体工具兼具学习对象和创作工具身份；以 **AI 开源项目观察站** 为贯穿式项目实践载体，在 AtomGit 社区实践中建立个人技能集与作品集。

## 从这里开始

- [在线评审站](https://www.x-lab.info/AIOS101-AtomGit/)
- [课程宪法](CONSTITUTION.md) · [课程总规格](specs/course-spec.md) · [十二章规格](specs/chapters/README.md)
- [作者指南](docs/AUTHORING.md) · [当前状态](docs/STATUS.md) · [AI 协作者指南](AGENTS.md)
- [观察站实践](practice/README.md) · [示范结构](practice/demo/README.md) · [实践模板](practice/template/README.md)

## 本轮范围

课程结构版本为 0.1.0：四篇十二章、规范和实践模板已经建立，正文逐章创作与评审。提纲、草稿和正式正文分别标记。示范不代表任务实测或社区贡献已经完成。

序言与前三章现为 0.2.1 图文评审稿。前三章已完成一轮[联合编辑评审与修订](docs/review/2026-10-29-ch01-03.md)，围绕同一份导览推进：

- [第一章：先做成一件事](textbook/chapters/CH01.md)——三幅图、[八文件练习包](practice/ch01/README.md)，做出并核对初稿。
- [第二章：打开一个项目](textbook/chapters/CH02.md)——三幅图、[七文件观察包](practice/ch02/README.md)，建立档案并检查导览中的一句话。
- [第三章：开放的力量](textbook/chapters/CH03.md)——三幅图、[八文件复用包](practice/ch03/README.md)，为一项材料补齐使用说明。

- [第四章：模型怎样学会本领](textbook/chapters/CH04.md)——[纸面实验材料包](practice/ch04/README.md)，用教学合成数据理解训练、检验与适用边界。

- [第五章：AI 为什么会答错](textbook/chapters/CH05.md)——[生成对照材料包](practice/ch05/README.md)，理解生成与上下文，并为同一导览做一次有依据的修订。

- [第六章：从回答到行动](textbook/chapters/CH06.md)——[任务追踪材料包](practice/ch06/README.md)，分清读取、生成、执行和人的授权核验。

[序言](textbook/preface.md)含两幅概念插画，入门路径同步对齐。第四至六章已作 0.3.0 机制与实践重构，等待内容复核，其余六章仍为提纲；本轮不表示工具实测或真人试学已经完成。

## 创作方式

只需在 textbook/chapters/ 中创作 Markdown 正文；目录、阅读页、状态与下载由构建生成。结构变化先修改 specs/course.json，再同步规格。

```bash
python scripts/sync_specs.py --check
python scripts/check_all.py
```

main 检查通过后由 GitHub Actions 发布 Pages。PR 仅检查。详见 [作者指南](docs/AUTHORING.md)。

## 复用与来源

继承 [AIOS101](https://github.com/X-lab2017/AIOS101) 的 Open Folio 1.0.0 视觉、阅读方法和 SDD 经验，按新大纲独立组织。固定来源、资产哈希和适配说明见 [品牌复用记录](brand/README.md)。

课程源码维护于 GitHub，AtomGit 承载学习者的观察站与社区实践。当前尚未配置统一 AtomGit 教学空间，不预设自动集成。

## 使用条件

本仓库保留源资产与第三方许可，课程及代码的统一对外许可待维护者确定，不自动新增授权。见 [素材来源](site/assets/NOTICE.md) 与 [参与指南](CONTRIBUTING.md)。
