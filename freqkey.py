#!/usr/bin/env python3

from argparse import ArgumentParser
from collections import defaultdict

import fileinput
import subprocess as sub

letter_keys = [(10, 21), (24, 35), (38, 49), (51, 61)]
mods = ['Shift', 'Control', 'Super', 'Alt']

def xmodmap():
    out = sub.check_output(["xmodmap", "-pke"])
    lines = [ str(l, 'utf-8').split() for l in out.split(b'\n') ]
    return { int(l[1]) : l[3:] for l in lines if len(l) > 3 }

ap = ArgumentParser()
ap.add_argument('keylog', nargs='*', default=[])
ap.add_argument('--map', default=xmodmap())
args = ap.parse_args()

combos = defaultdict(lambda: 0)
current_combo = []

for line in fileinput.input(args.keylog):
    tk = line.split()
    state = tk[1]
    code = int(tk[2])
    keys = args.map[code]
    pre = keys[0].split('_')[0]
    if state == 'press':
        # start a combo
        if len(current_combo) == 0:
            if pre not in mods:
                # one-shot key
                combos[(keys[0],)] += 1
                continue
        current_combo.append(keys[0])
    elif state == 'release':
        # end a combo
        # if it's a modifier key being released, do some checks
        if len(current_combo) == 0:
            continue
        cmb = tuple(current_combo)
        if cmb[0].startswith('Shift') and len(cmb) > 1:
            if keys[1] == 'NoSymbol':
                print('wah', cmb, keys)
            cmb = (keys[1],)
        combos[cmb] += 1
        current_combo.clear()

for combo, count in combos.items():
    print(combo, count)
