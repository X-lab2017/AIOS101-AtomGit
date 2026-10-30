#!/usr/bin/env python3
"""Rebuild renamed OFL subsets when the chapter adds characters."""
import argparse
from pathlib import Path
from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    for name in ('serif','sans','bold'): parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    paths = [ROOT/'textbook/chapters/CH01.md', ROOT/'textbook/chapters/CH02.md', ROOT/'scripts/build_print.py', ROOT/'scripts/print-book.css', ROOT/'textbook/assets/figures/manifest.json']
    paths += list((ROOT/'textbook/assets/figures').glob('ag-01-*.svg'))
    paths += list((ROOT/'textbook/assets/figures').glob('ag-02-*.svg'))
    (ROOT/'textbook/print/fonts').mkdir(parents=True,exist_ok=True)
    text = ''.join(p.read_text() for p in paths)+''.join(chr(i) for i in range(32,127))+'•'
    notices = []
    for source, name, weight in [(args.serif,'AIOSBookSerif',400),(args.sans,'AIOSBookSans',400),(args.bold,'AIOSBookSansBold',700)]:
        font = TTFont(source)
        notices.append(name+'\n'+font['name'].getDebugName(0))
        options = subset.Options()
        options.name_IDs = ['*']; options.name_legacy = True; options.name_languages = ['*']; options.recalc_timestamp = False
        worker = subset.Subsetter(options=options); worker.populate(text=text); worker.subset(font)
        if 'fvar' in font: font = instantiateVariableFont(font, {'wght':weight}, inplace=True)
        for record in font['name'].names:
            if record.nameID in [1,4,6,16]: record.string = name.encode(record.getEncoding())
        target = ROOT/'textbook/print/fonts'/(name+'.ttf'); font.save(target)
        print(target.name, target.stat().st_size)
    (ROOT/'textbook/print/fonts/NOTICE.txt').write_text('AIOS101 print font subsets. Renamed derivatives, licensed under SIL OFL 1.1 (OFL.txt).\nSource: https://github.com/notofonts/noto-cjk\n'+'\n\n'.join(notices)+'\n')


if __name__ == '__main__': main()
