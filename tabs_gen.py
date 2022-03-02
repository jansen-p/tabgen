#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
import sys
from PIL import Image, ImageDraw, ImageFont

#name of the input file as arg!
s = open(sys.argv[1], 'r')

#please don't judge me
xscale = 80
yscale = 40
yoffset = 160
fontsize = 40
width = 2800
height = 3000
x_margin = 160
y_spacing = 2*yscale

colreset = 0

kp = s.readlines()
name = kp[0].strip()

lines = [r.strip().split(',') for r in kp[1:]]

img = Image.new('RGB', (width, height), color = 'white')
d = ImageDraw.Draw(img)

fnt = ImageFont.truetype('FiraCodeBoldNerdFontComplete.ttf', fontsize)
fntcomment = ImageFont.truetype('FiraCodeBoldNerdFontComplete.ttf', int(fontsize/2))
d.text((30, 20), name, font=fnt, fill=(100,100,0))

for k in range(4):
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
        print("|")
        d.line((1.2*x_margin+colnum*xscale,yoffset, 1.2*x_margin+colnum*xscale,yoffset+5*yscale), fill=(80,80,80))
        continue
    if col == ['||']:
        print("||")
        d.line((1.2*x_margin+colnum*xscale,yoffset, 1.2*x_margin+colnum*xscale,yoffset+5*yscale), fill=(80,80,80))
        d.line((1.25*x_margin+colnum*xscale,yoffset, 1.25*x_margin+colnum*xscale,yoffset+5*yscale), fill=(80,80,80))
        continue
    if ':' in col[0]:
        print(":x||")
        d.text((x_margin+colnum*xscale, yoffset-yscale), col[0][:-2], font=fnt, fill=(150,0,0))
        d.line((1.2*x_margin+colnum*xscale,yoffset, 1.2*x_margin+colnum*xscale,yoffset+5*yscale), fill=(80,80,80))
        d.line((1.25*x_margin+colnum*xscale,yoffset, 1.25*x_margin+colnum*xscale,yoffset+5*yscale), fill=(80,80,80))
        continue

    print(col)

    if '#' in col[-1]:
        comment = col[-1]
        d.text((x_margin+colnum*xscale, yoffset-yscale), comment.split('#')[1], font=fntcomment, fill=(150,150,0))

        if len(col) == 7:
            col = col[:-1]
        else:
            col[-1] = ''

    for idx, note in enumerate(reversed(col)):
        size = fontsize if len(note) == 1 else int(fontsize*4/5)
        fnt = ImageFont.truetype('FiraCodeBoldNerdFontComplete.ttf', size)

        if len(note) != 0:
            d.text((x_margin+int(size/2)+colnum*xscale, yoffset+idx*yscale-int(size/1.7)), note, font=fnt, fill=(0,0,0))

img.save('{}.png'.format(name))
