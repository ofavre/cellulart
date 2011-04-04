# -*- coding: utf-8 -*-
# License: See LICENSE file.

import math
import random

required_states = ['direction', 'position']
required_matrices = []

def run(name, world, matrices, states, target_y, target_x, wrap=False, get_closer=True, min_dist=1e-6, max_turn=math.pi/6):
    d = states['direction'] % (2*math.pi)
    y,x = states['position']
    if wrap:
        wh,ww = world.get_shape()
        y %= wh
        x %= ww
        target_y %= wh
        target_x %= ww
        dy = target_y - y
        dx = target_x - x
        # Is it shorter to wrap the y ordinate to reach target ?
        if y < target_y:
            dy2 = target_y - (y+wh)
            if abs(dy2) < abs(dy):
                dy = dy2
        else:
            dy2 = target_y+wh - y
            if abs(dy2) < abs(dy):
                dy = dy2
        # Is it shorter to wrap the x ordinate to reach target ?
        if x < target_x:
            dx2 = target_x - (x+ww)
            if abs(dx2) < abs(dx):
                dx = dx2
        else:
            dx2 = target_x+ww - x
            if abs(dx2) < abs(dx):
                dx = dx2
    else:
        dy = target_y - y
        dx = target_x - x
    # Already close enough to the target?
    dist = math.hypot(dy, dx)
    if dist <= min_dist or dist == 0:
        return
    a = math.atan2(dy, dx) % (2*math.pi)
    if not get_closer:
        a = (a+math.pi) % (2*math.pi)
    # Which way to turn (also a wrapping problem)
    if a < d and abs(a+2*math.pi-d) < abs(a-d):
        a += 2*math.pi
    elif abs(a-2*math.pi-d) < abs(a-d):
        a -= 2*math.pi
    # Delta angle, limited
    dd = max(-max_turn, min(max_turn, (a-d)/2))
    # Add the adjustment to the direction, in order to turn toward the desired position
    d += dd
    states['direction'] = d % (2*math.pi)
