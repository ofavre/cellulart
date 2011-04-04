# -*- coding: utf-8 -*-

import math



required_states = ['position']
required_matrices = ['trace']



def run(name, world, matrices, states, y=None, x=None, opacity=1.0):
    if y == None or x == None:
        y,x = states['position']
    iy = int(y)
    ix = int(x)
    rx = x % 1.0
    ry = y % 1.0
    if rx > 0.5:
        dx = 1
        rx = 1-rx
    else:
        dx = -1
    if ry > 0.5:
        dy = 1
        ry = 1-ry
    else:
        dy = -1
    matrices['trace'][iy,   ix   ] += (ry+0.5)*(rx+0.5)*opacity
    matrices['trace'][iy,   ix+dx] += (ry+0.5)*(0.5-rx)*opacity
    matrices['trace'][iy+dy,ix   ] += (0.5-ry)*(rx+0.5)*opacity
    matrices['trace'][iy+dy,ix+dx] += (0.5-ry)*(0.5-rx)*opacity
