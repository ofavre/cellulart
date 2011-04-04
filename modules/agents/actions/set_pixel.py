# -*- coding: utf-8 -*-
# License: See LICENSE file.

required_states = ['position']
required_matrices = ['pixels']



def run(name, world, matrices, states, y=None, x=None, color=None):
    if color == None:
        color = states['color']
    if y == None:
        pos = states['position']
        y = pos[0]
        if x == None:
            x = pos[1]
    elif x == None:
        x = states['position'][1]
    matrices['pixels'][int(y),int(x)] = color
