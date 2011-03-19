# -*- coding: utf-8 -*-

import math
import random

required_states = ['direction', 'position']
required_matrices = []

def run(name, world, matrices, states, target_y, target_x, get_closer=True, min_dist=1, max_turn=math.pi/6):
    d = math.fmod(states['direction'], 2*math.pi)
    y,x = states['position']
    dy = target_y - y
    dx = target_x - x
    # Already close enough to the target?
    if math.hypot(dy, dx) < min_dist:
        return
    a = math.atan2(dy, dx)
    if not get_closer:
        a += math.pi
    # Which way to turn
    if abs(a-d) > abs(a-d+2*math.pi):
        a += 2*math.pi
    # Delta angle, limitted
    dd = max(-max_turn, min(max_turn, (a-d)/2))
    # Add the adjustment to the direction, in order to turn toward the desired position
    d += dd
    states['direction'] = d
