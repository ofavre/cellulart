# -*- coding: utf-8 -*-

import math
import random

required_states = ['direction']
required_matrices = []

def run(name, world, matrices, states, max_turn=math.pi/6):
    d = states['direction']
    # Add a ± 15° to the direction
    d = (d + (1-2*random.random())*max_turn) % (2*math.pi)
    states['direction'] = d
