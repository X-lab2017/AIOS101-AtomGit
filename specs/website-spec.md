# 网站规格

> ID：WEB-ATOMGIT · 版本：0.1.0

静态、多页、子路径兼容的阅读网站。首页 → 学习路径 → 序言/章节；独立项目实践页 → 示范/模板；关于页提供理念、历史与 GitHub 入口。

- textbook/ 是正文正本；specs/course.json 是结构正本；构建输出 dist/，不提交。
- 路由：首页 /、学习路径 /learn/、序言 /preface/、章节 /chapters/01/ 至 /chapters/12/、项目实践 /practice/、示范 /practice/demo/、模板 /practice/template/、关于 /about/。
- 明确展示 outline/draft/review/published；不把提纲渲染成已完成正文。没有虚构课时、学习人数或完成率。
- 桌面章节目录与正文，小屏折叠目录；原生 HTML 支持无 JS 阅读，JS 仅承担主题、界面语言、字号、菜单与目录搜索。
- 中文正文为当前语言。EN 切换仅翻译界面并明确中文正文状态，不能暗示存在英文教材。
- 暖纸白、靛蓝、Open Folio 与 X-lab 原版署名。保持低干扰，无手账、已读进度或提交表单。
- 正文最大宽度约 760px，图片保持原比例，表格横向滚动仅发生在容器内。阅读可调整字号，打印隐藏导航并保留正文。
- 核心导航和下载不得死链。外部资源集中在需要的实践/来源位置，保持 GitHub 入口可见。
- 推送 main 后自动检查、构建、部署 GitHub Pages；PR 仅检查。页脚和 build.json 记录构建提交。
