# -*- coding: utf-8 -*-
# License: See LICENSE file.

import math
import random



required_states = ['age','position','direction']
required_matrices = ['trace']



def run(name, world, matrices, states):
    # Breed a new agent
    c, = world.add_new_agents(name, 1)
    # Inherit some state from the parent
    y,x = states['position']
    c.states['position'] = (y,x)
    c.states['direction'] = math.pi/12*(random.random()*2-1) + states['direction']
