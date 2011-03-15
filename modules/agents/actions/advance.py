# -*- coding: utf-8 -*-

import math

required_states = ['position', 'direction', 'speed']
required_matrices = []

def run(world, matrices, states, *args, **kwargs):
    # Advance 'speed' cells in the given 'direction'
    y,x = states['position']
    d = states['direction']
    s = states['speed']
    sy,sx = world.get_shape()
    sx = float(sx)
    sy = float(sy)
    # Ensure x and y are (float) within 0 and world's shape x/y
    y = math.fmod(y + s*math.sin(d), sy)
    x = math.fmod(x + s*math.cos(d), sx)
    if y < 0: y += sy
    if x < 0: x += sx
    states['position'] = (y,x)
