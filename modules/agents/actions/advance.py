# -*- coding: utf-8 -*-
# License: See LICENSE file.

import math

required_states = ['position', 'direction', 'speed']
required_matrices = []

def run(name, world, matrices, states, *args, **kwargs):
    # Advance 'speed' cells in the given 'direction'
    y,x = states['position']
    d = states['direction']
    s = states['speed']
    sy,sx = world.get_shape()
    sx = float(sx)
    sy = float(sy)
    # Ensure x and y are (float) within 0 and world's shape x/y
    y = (y + s*math.sin(d)) % sy
    x = (x + s*math.cos(d)) % sx
    if y < 0: y += sy
    if x < 0: x += sx
    states['position'] = (y,x)
