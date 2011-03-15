# -*- coding: utf-8 -*-

import math
import random

required_states = ['direction']
required_matrices = []

def run(world, matrices, states, *args, **kwargs):
    d = states['direction']
    # Add a ± 15° to the direction
    d = math.fmod(d + (1-2*random.random())*math.pi/6, 2*math.pi)
    # Ensure it stays between 0 and 2*Pi
    if d < 0: d += 2*math.pi
    states['direction'] = d
