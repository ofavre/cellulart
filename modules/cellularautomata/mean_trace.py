# -*- coding: utf-8 -*-

required_matrices = ['trace']

def run(world, x, y, matrices):
    m = matrices['trace']
    val = 0.0
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            val += m[y+dy,x+dx]
    m[y,x] = val/9
