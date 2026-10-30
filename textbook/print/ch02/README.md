# 第二章打印书稿

教材正本为 textbook/chapters/CH02.md；PDF 单独交付，不提交 GitHub 或 Pages。图件、字体子集、构建脚本与来源保留在仓库。

```bash
python -m pip install -r textbook/print/ch02/requirements.txt
python scripts/build_print_ch02.py
python scripts/check_all.py
```

输出 AIOS101-AtomGit-CH02.pdf 与本目录 manifest.json；临时 HTML 在 tmp/pdfs/CH02.html。打印使用 A4、实际大小、双面长边翻转；网页与 PDF 的编号、材料卡和练习保持一致。

新增汉字后，使用原始 Noto Serif SC 与 Noto Sans SC TrueType 可变字体运行 scripts/subset_print_fonts_ch02.py（参数 --serif、--sans、--bold），再重建 PDF。字体子集遵循 SIL OFL，已改名；授权与版权见 fonts/。正文、图件、字体、CSS 与构建脚本的摘要保存在 manifest.json。

交付前用 Poppler 渲染每页，检查图题、截断、分页、标题与页码，并用 pdffonts 核对嵌入字体。教材页数由内容决定，出版社的开本和印前规格另行落实。
