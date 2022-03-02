#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import os
import argparse

def exists(name):
    for f in os.listdir('../'):
        if name == f[:-4]:
            return True
    return False

parser = argparse.ArgumentParser(description="Convert the chords stored in file ./notes to pdf files. Don't forget to adjust the output directory! ")
parser.add_argument('--regenerate', action='store_true', default=False, help='Regenerate all chords')
parser.add_argument('--allnames', action='store_true', default=False, help="Add the names of all chords. Names of chords starting with '_' aren't added by default.")

args = parser.parse_args()

s = open('notes', 'r')
kp = s.readlines()

strings = {0: 'E', 1: 'A', 2: 'D', 3: 'G', 4: 'B', 5: 'e'}

if args.regenerate:
    print("Regenerating all chords")
else:
    print("Generating new chords")
if args.allnames:
    print("Printing all chord names")


for chord in kp:
    chord = chord.split(',')
    name = chord[0].strip()
    inp = chord[1].strip()

    if not args.regenerate and exists(name):
        print('   Skipping chord {}..'.format(name))
        continue

    print("   Generating chord {}, frets: {}".format(name,inp))

    if '-' in inp:
        inp = inp.split('-')

    notes = [int(x) for x in inp if x != "x" and x != '0']
    base = min(notes)
    frets = max(max(notes)-min(notes)+1,2)

    shifted = [int(x)-base if x != 'x' else 'x' for x in inp]

    xspace = 20
    yspace = 10

    fig,ax = plt.subplots(1)

    #horizontal
    for y in [yspace*i+20 for i in range(6)]:
        plt.axline((-3, y), (20*frets, y), color='black')

    #vertical
    for x in [xspace*i for i in range(frets+1)]:
        plt.axline((x, xspace), (x, 10+yspace*6), color='black')
    ax.set_aspect('equal')

    if args.allnames or name[0] != '_':
        ax.text(-3, 75, name, color='black', fontsize=30)

    for num in range(frets):
        ax.text(num*xspace+xspace/2-2, 12, str(base+num), color='black', fontsize=30)
    ax.axis('off')

    for x,y in zip(shifted,range(6)):
        if x == 'x':
            ax.text(0, yspace*y+2*yspace-2, 'x', color='red', fontsize=40)
        elif x >= 0:
            ax.add_patch(Circle((xspace*x+xspace/2,yspace*y+2*yspace),3,color='darkgreen'))
        ax.text(-3, yspace*y+2*yspace-3, strings[y], color='black', fontsize=15)

    fig.savefig(f"{os.getenv('NAS')}/uni/guitar/chords/{name}.pdf",bbox_inches='tight', pad_inches=0)
    plt.close()
