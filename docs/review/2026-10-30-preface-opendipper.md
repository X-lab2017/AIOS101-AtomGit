# 序言 0.3.0 图文更新记录

日期：2026-10-30（北京时间）。状态：按维护者指令直接更新图文并发布 Pages，供内容评审。

## 本轮决定

维护者提供了中国国际科技交流中心的发布报道，并指定参考 AIOS101 原版序言中的 OpenDipper 图文。本轮跳过单独研究报告，以真实项目和报告实践直接重写序言。

新标题为“从一个开源项目说起”。顺序为：开源北斗引出问题—日内瓦活动与报告预览版—全球观测与开源星系—课程主张—研究报告/动态页面/AtomGit 项目—五维目标—四篇路径与自学。校园口述史工具选择是引导读者设想选题的例子，没有写成已经发生的学生成果。

保留第一章一页导览的起点，把它解释为逐步发展成研究报告的学习片段。保留维护者最新修改的“X-lab 开放实验室与奇点智能研究院联合出品”署名，并同步 README。

## 事实与素材核对

- [发布报道](https://www.ciste.org.cn/gzdt/kxzs/art/2026/art_bed9ae4a12b049e7b4ae56083023159e.html)：页面发表于 2026-07-17，记载 CCOSI 在日内瓦相关活动期间发布宣言，宣言收录于同期发布的《2026 全球开源发展报告》预览版。正文按这个版本和关联表述。
- [报告在线目录](https://www.x-lab.info/2026-Global-Open-Source-Development-Report/2026/zh/)与[项目说明](https://github.com/X-lab2017/2026-Global-Open-Source-Development-Report/blob/c51e3441361407b68f10b339d97eff288319b503/README.md)：支持文字、地图、榜单、技术全景与关系研究互补，以及内容和材料通过公开仓库维护。
- [OpenDipper](https://github.com/X-lab2017/open-dipper/blob/da08d0edd190a58c37127d94eb773fd45134043e/README.md)、[OpenDigger](https://github.com/X-lab2017/open-digger/blob/master/README.md)、DSH 官方 README、OSI 开源定义及 AtomGit 产品介绍均已阅读；来源登记在 specs/sources.json。
- 当前 OD 界面与在线报告作为课程素材使用，不声称它们是七月现场画面，也不声称报告由 OD 自动生成。

## 图件复用与适配

| 当前图号 | 采用图件 | 来源 |
| --- | --- | --- |
| AG-00-01 | OpenDipper 全球观测：发现值得追问的问题 | AIOS101@9acf393 原图 0-4 |
| AG-00-02 | OpenDipper 开源星系：看见项目之间的联系 | AIOS101@9acf393 原图 0-5 |

依据维护者明确的课程素材复用指令，沿用真实截图与手绘装帧。以原生 SVG 适配图号、标题和三步导读；两份 SVG 内嵌的界面与装帧图像字节保持一致，没有生成式重绘数字、地图或节点。原始来源见[上游制作记录](https://github.com/X-lab2017/AIOS101/blob/9acf393293ed629cdf1ffd1162d1257814aa57e7/textbook/assets/figures/sources/preface-opendipper-2026-10-29.md)。

本版发布 2000 × 1660、quality 92 的 WebP，保留原尺寸打开入口。图号、图题、替代文字、来源和哈希由 manifest 管理。原两幅概念图退出当前序言和发布清单，文件留在仓库供历史记录回查；旧评审记录中的相同编号属于当时版本。

复现入口：scripts/figures/adapt_preface_opendipper.py。输入为 AIOS101 固定提交的检出目录、NotoSansCJKsc-Regular.otf 和 QA 输出目录；使用 CairoSVG 2.9.1、Pillow 13.0.0、fontTools 4.68.0。脚本核对上游 Git blob，再从原生 SVG 导出；具体哈希和压缩体积见[图件记录](2026-10-30-preface-od-figures.json)。

## 自审与发布范围

已逐段检查初次术语解释、真实故事与任务构想的区分、五维目标及综合项目的对应、两图位置与第一章衔接。去掉旧“观察站”叙事和重复的操作边界提醒。图件逐幅查看，缩短星系图右下导读，避免碰到放大镜装饰。

本轮只改序言、相关规格与来源、两幅图及生成脚本、入口和状态记录；十二章、实践包、宪法及维护者最新 about.md 保持基线内容。

`python scripts/check_all.py` 通过：35 个静态页面、13 份实践下载包、规格映射、图件完整性、站内链接与锚点、品牌文件及 JavaScript 语法均通过现有检查。两幅 WebP 共 695,580 字节，保留 2000 × 1660 分辨率。

浏览器已检查桌面版、390 px 宽 iframe 模拟窄屏及深浅主题。窄屏正文为 19 px，文档宽度与可视宽度一致，没有横向溢出；两幅图均载入原始 2000 px 宽图件，放大入口可打开独立图片页。已点击序言末尾入口，确认进入第一章“先做成一件事”。这属于工程与模拟视口检查，不替代真实手机和学生试学。临时 QA 页面不进入仓库或发布包。

提交后以对应 commit 的 GitHub Actions 结果和公开 `/preface/` 页面核验发布；本记录中的正文状态保持 review，供维护者内容评审。
