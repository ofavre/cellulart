# -*- coding: utf-8 -*-
# License: See LICENSE file.

required_states = ['age', 'speed']
required_matrices = []

def run(name, world, matrices, states, *args, **kwargs):
    states['speed'] *= 1.0 - 0.5/states['age']
