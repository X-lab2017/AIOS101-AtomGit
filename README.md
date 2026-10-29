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

当前为 0.1.0 骨架评审版：四篇十二章、章节提纲、规范和实践模板已经建立，正文将在评审后逐章创作。提纲、草稿和正式正文分别标记。示范不代表任务实测或社区贡献已经完成。

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
