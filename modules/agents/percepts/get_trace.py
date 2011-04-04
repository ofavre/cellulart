# -*- coding: utf-8 -*-
# License: See LICENSE file.

required_states = ['position']
required_matrices = ['trace']



def run(name, world, matrices, states, y=None, x=None):
    if y == None:
        pos = states['position']
        y = pos[0]
        if x == None:
            x = pos[1]
    elif x == None:
        x = states['position'][1]
    return matrices['trace'][int(y),int(x)]
