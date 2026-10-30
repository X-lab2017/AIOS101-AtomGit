# 第一部分三章打印书稿

教材 Markdown 是内容正本。三章使用同一渲染器和 A4 样式，PDF 只在对话中交付，不提交 GitHub 或 Pages。本目录记录可重建的排版、字体来源与输入摘要。

## 重建

将同版 `AIOS101-Part1-print-resources.zip` 解压到仓库根目录，恢复忽略的 `textbook/print/assets/` 与 `textbook/print/fonts/`。资源包包括第一章打印大图、三章共用中文字体子集及字体授权；第二、三章插图直接使用仓库中的 WebP，SVG 保持矢量。

使用 Python 3.12 与 WeasyPrint 70：

```bash
python -m pip install -r textbook/print/requirements.txt
python scripts/build_print.py
python scripts/print_manifest.py
python scripts/check_all.py
```

`build_print.py` 默认同时生成三章；`--chapter 1` 、`--chapter 2` 或 `--chapter 3` 可单独重建。输出均为 `textbook/print/AIOS101-AtomGit-CH0N.pdf`，共同摘要在 `textbook/print/manifest.json`。默认还生成含目次、连续页码的 `AIOS101-AtomGit-Part1.pdf`，摘要在 `part-manifest.json`。旧 `build_print_ch02.py` 是兼容入口，旧 ch02 子目录不再承担当前排版。

需要新增汉字时，准备 [Noto CJK](https://github.com/notofonts/noto-cjk) 原始字体并运行：

```bash
python scripts/subset_print_fonts.py --serif /path/to/NotoSerifSC-VF.ttf --sans /path/to/NotoSansSC-VF.ttf --bold /path/to/NotoSansSC-VF.ttf
python scripts/build_print.py
```

子集按 SIL OFL 改名为 AIOSBookSerif、AIOSBookSans 与 AIOSBookSansBold，字重分别为 400、400、700。版权见 [NOTICE](fonts/NOTICE.txt) 和 [OFL](fonts/OFL.txt)。更新字体后应同时重建三章并更新资源包。

## 交付验收

- 渲染全部页面，查看段落、表格、图件、图题、来源、页眉和页码；文字提取不能替代视觉检查。
- 核对字体嵌入、三章各六题与反馈、第一章四图、第二章两图和第三章四图；精确图形的文字原则上不大于正文。
- `print_manifest.py` 校验内容、图件、字体和样式全部输入，任一改变均需重建。PDF 摘要以交付前本地版本为准。
- 全站检查确认规格、正文、材料包和网页一致，Pages 不依赖排版环境，不复制 PDF。

按 A4 实际大小打印，可双面长边翻转；当前为教材评审稿，尚未完成维护者终审或真人试学。出版社要求的开本、CMYK、出血和 PDF/X 属于后续印前生产规格。
