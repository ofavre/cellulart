# -*- coding: utf-8 -*-
# License: See LICENSE file.

required_states = []
required_matrices = []

def run(name, world, matrices, states, key, default=None):
    return states.get(key,default)
