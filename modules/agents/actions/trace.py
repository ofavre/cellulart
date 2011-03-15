# -*- coding: utf-8 -*-

required_states = ['position']
required_matrices = ['trace']

def run(world, matrices, states, *args, **kwargs):
    y,x = states['position']
    matrices['trace'][int(y),int(x)] += 1
