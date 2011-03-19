# -*- coding: utf-8 -*-

required_states = []
required_matrices = []



def run(name, world, matrices, states):
    y,x = states['position']
    return matrices['trace'][int(y),int(x)]
