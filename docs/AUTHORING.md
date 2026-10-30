# 作者只改内容：从这里开始

## 1. 找到章节

十二章正文在 textbook/chapters/CH01.md 至 CH12.md。目录、名称和任务正本在 specs/course.json；对应教学规格在 specs/chapters/。先阅读目标、前置知识与边界，再开始写正文。

## 2. 写正文

保留文件第一行标题、顶部状态和版本。当前 `> 状态：outline` 是提纲。开始写作改为 `draft`，提交内容评审改为 `review`，经维护者确认后改为 `published`。状态变化和版本号都留在同一个 Markdown 文件，网站自动读取。

按 [教材体例规范](../specs/textbook-style-spec.md) 编写适合书籍与独立自学的正文：交代背景、解释概念，结合例题说明方法，提供综合实践、小结、练习与参考反馈。操作步骤放入相应配套材料。以序言 v0.4.0 的叙述语气与全书主线、CH01 v0.6.0 的讲解深度与图文打印质量为共同基准；结构按教学需要组织。用 `##` 分节、`###` 分小节，网站自动生成节目录。普通段落、列表、表格、代码、引用与链接均可用。

不要把正文复制到网页。不要编辑 dist/ 或为每次文字更新手工修改 HTML。若改章节名称、任务或学习目标，先改 specs/course.json，再运行 `python scripts/sync_specs.py`；正文标题需要同步。

## 3. 加图

图片放入 textbook/assets/figures/，登记 manifest.json 中的图号、文件、图题、替代文字、尺寸、来源、许可和日期。正文独立一行引用图片。构建保留比例并链接原图，图题自动跟随登记信息。

## 4. 检查与上线

按教材体例规范中的质量基准逐项复核，在本章评审记录中简述对齐情况和必要差异，再运行工程检查。沿用“逐章立题、研究先行、材料补充、图文共创、上线评审”的推进方式。

```bash
python scripts/sync_specs.py --check
python scripts/check_all.py
```

常规正文改动不需要运行非检查模式的 sync_specs。结构变化后才运行 `python scripts/sync_specs.py`。检查通过的 main 提交由 GitHub Actions 构建并发布 Pages；PR 只检查。查看 Actions 结果，并核对线上对应章节。

## 5. 继续实践与维护

实践说明在 practice/README.md，示范在 practice/demo/，模板在 practice/template/。本版未验证的运行和反馈应保留准确状态。当前事实写 docs/STATUS.md，重要决定写 docs/decisions/。

## 首轮创作顺序

先写序言与 CH01，打通一个真实任务；随后补齐 CH02—06 的理解与判断；再完成 CH07—09 的完整作品过程；最后以 CH10—12 的真实协作和迁移记录收束。内容可逐章上线，状态分别记录。

已提供打印稿的章节，更新正文、图件、图注或排版输入后须重新生成 PDF，并逐页检查；交付前运行 `python scripts/print_manifest.py` 检查新鲜度。PDF 只单独交付，不提交 GitHub；普通网站构建不依赖 PDF。见 [打印构建说明](../textbook/print/README.md) 和 [打印规范](../specs/print-spec.md)。
