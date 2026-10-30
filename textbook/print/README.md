# 章节打印书稿

本目录包含 A4 书稿的排版说明、来源与输入摘要；生成的 PDF 由 `.gitignore` 排除，只在对话中另行交付，不提交 GitHub 或 Pages。教材 Markdown 仍是内容正本；不要直接编辑 PDF 或构建后的 dist/。

## 重建第一章

先把随书稿交付的 `AIOS101-CH01-print-resources.zip` 解压到仓库根目录，恢复 `textbook/print/assets/` 和 `textbook/print/fonts/` 中的文件。打印大图、字体子集及 PDF 均不纳入 Git 历史；资源包保留同版输入与字体授权。

随后在仓库根目录，使用 Python 3.12 和可运行 WeasyPrint 70 的环境：

```bash
python -m pip install -r textbook/print/requirements.txt
python scripts/build_print.py
python scripts/print_manifest.py
python scripts/check_all.py
```

构建会生成 `AIOS101-AtomGit-CH01.pdf` 与 `manifest.json`，临时排版 HTML 放在忽略的 `tmp/pdfs/`。普通 Pages 流程不复制或依赖 PDF，也不安装排版依赖。打印专用大图和字体子集由随书稿交付的资源包提供，构建时检查所需汉字覆盖；新增汉字不在子集时会明确失败，须更新子集后重建，不依赖宿主机字体兜底。

源字体来自 [Noto CJK](https://github.com/notofonts/noto-cjk)，适用 [SIL OFL](fonts/OFL.txt)，版权记录见 [NOTICE](fonts/NOTICE.txt)。子集已改名为 AIOSBookSerif、AIOSBookSans、AIOSBookSansBold；分别取自 Noto Serif SC 与 Noto Sans SC 的官方 TrueType 可变字体，固定为 400/700 字重。不要把字体授权误作教材或第三方图像授权。

需要扩展字体时，准备对应原始 TTF 文件并运行：

```bash
python scripts/subset_print_fonts.py --serif /path/to/NotoSerifSC-VF.ttf --sans /path/to/NotoSansSC-VF.ttf --bold /path/to/NotoSansSC-VF.ttf
python scripts/build_print.py
```

## 交付检查

1. 用 `pdftoppm -png` 渲染全部页面，逐页看标题、段落、表格、图题、来源、页眉页码与孤行；仅提取文字不能代替此步。
2. 用 `pdffonts` 核验中文字体嵌入；检查六道练习的编号与参考解答对应，四个图号与正文、图件登记表对应。
3. 核对主要图中文字的实际打印大小；图 AG-01-03 的关键信息有原像素局部放大，图 AG-01-02 保持矢量。
4. 打印交付前运行 `python scripts/print_manifest.py`，改变任一排版输入而不重建会触发过期检测；再核对交付文件摘要。
5. 运行全站检查，确认网页不包含 PDF 或 PDF 下载入口；将书稿单独交付并保留验收记录。

当前提供“实际大小 / 100%”A4 打印稿，可双面长边翻转；内容仍待维护者评审。出版社要求的特定开本、CMYK、出血或 PDF/X 属于后续生产规格，不以当前阅读书稿代替印前确认。
