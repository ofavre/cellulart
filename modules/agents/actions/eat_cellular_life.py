# -*- coding: utf-8 -*-
# License: See LICENSE file.


required_states = ['position','age']
required_matrices = ['cellular_binary_life']

def run(name, world, matrices, states, extra_life=10):
    y,x = states['position']
    if matrices['cellular_binary_life'][int(y),int(x)]:
        # Eat the cell under the agent's position
        matrices['cellular_binary_life'][int(y),int(x)] = False
        # And give an extra lifetime
        states['age'] += extra_life
