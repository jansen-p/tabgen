#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import sys
from PIL import Image, ImageDraw, ImageFont

#name of the input file as arg!
if len(sys.argv) not in [2,3]:
    print("Invalid number of arguments, check docu!")
    sys.exit()

s = open(sys.argv[1], 'r')

verbose = False
if len(sys.argv) == 3:
    verbose = True


#please don't judge me
xscale = 80
yscale = 40
yoffset = 160
fontsize = 40
x_margin = 160
y_spacing = 2*yscale

colreset = 0

kp = s.readlines()

#config lines
try:
    size = kp[0].split('x')
    width = int(size[0].strip())
    height = int(size[1].strip())
    rows = int(kp[1].split('=')[1].strip())
    print(f"Width: {width}, height: {height}, #rows: {rows}")
except:
    print("Output dimension or number of rows not specified correctly, check input file! Exiting...")
    sys.exit()
    
name = kp[2].strip()

lines = [r.strip().split(',') for r in kp[3:]]

img = Image.new('RGB', (width, height), color = 'white')
d = ImageDraw.Draw(img)

fnt = ImageFont.truetype('FiraCodeBoldNerdFontComplete.ttf', fontsize)
fntcomment = ImageFont.truetype('FiraCodeBoldNerdFontComplete.ttf', int(fontsize/1.5))
d.text((30, 20), name, font=fnt, fill=(100,100,0))

for k in range(rows):
    for i in range(6):
        d.line((x_margin,yoffset+k*(y_spacing+6*yscale)+i*yscale, width-x_margin,yoffset+k*(y_spacing+6*yscale)+i*yscale), fill=(80,80,80))

for colnum, col in enumerate(lines):
    if col == ['']:
        #rowbreak
        yoffset += y_spacing + 6*yscale
        colreset = colnum+1
        continue

    colnum -= colreset

    if col == ['|']:
        if verbose:
            print("|")
        d.line((1.2*x_margin+colnum*xscale,yoffset, 1.2*x_margin+colnum*xscale,yoffset+5*yscale), fill=(80,80,80))
        continue
    if col == ['||']:
        if verbose:
            print("||")
        d.line((1.2*x_margin+colnum*xscale,yoffset, 1.2*x_margin+colnum*xscale,yoffset+5*yscale), fill=(80,80,80))
        d.line((1.25*x_margin+colnum*xscale,yoffset, 1.25*x_margin+colnum*xscale,yoffset+5*yscale), fill=(80,80,80))
        continue
    if ':' in col[0]:
        if verbose:
            print(":x||")
        d.text((x_margin+colnum*xscale, yoffset-yscale), col[0][:-2], font=fnt, fill=(150,0,0))
        d.line((1.2*x_margin+colnum*xscale,yoffset, 1.2*x_margin+colnum*xscale,yoffset+5*yscale), fill=(80,80,80))
        d.line((1.25*x_margin+colnum*xscale,yoffset, 1.25*x_margin+colnum*xscale,yoffset+5*yscale), fill=(80,80,80))
        continue

    if verbose:
        print(col)

    if '#' in col[-1]:
        comment = col[-1].split('#')
        d.text((x_margin+colnum*xscale, yoffset-yscale), comment[1], font=fntcomment, fill=(150,150,0))

        if len(col) == 7:
            col = col[:-1]
        else:
            col[-1] = comment[0] #extract note before comment

    for idx, note in enumerate(reversed(col)):
        size = fontsize if len(note) == 1 else int(fontsize*4/5)
        fnt = ImageFont.truetype('FiraCodeBoldNerdFontComplete.ttf', size)

        if len(note) != 0:
            d.text((x_margin+int(size/2)+colnum*xscale, yoffset+idx*yscale-int(size/1.7)), note, font=fnt, fill=(0,0,0))

img.save('{}.png'.format(name))
