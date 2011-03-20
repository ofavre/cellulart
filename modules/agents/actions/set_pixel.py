# -*- coding: utf-8 -*-

required_states = ['position']
required_matrices = ['pixels']



def run(name, world, matrices, states, rgba_color, y=None, x=None):
    if y == None:
        pos = states['position']
        y = pos[0]
        if x == None:
            x = pos[1]
    elif x == None:
        x = states['position'][1]
    matrices['pixels'][int(y),int(x)] = rgba_color
