# -*- coding: utf-8 -*-
# License: See LICENSE file.


required_states = ['position']
required_matrices = ['cellular_binary_grass']

def run(name, world, matrices, states, extra_life=10):
    y,x = states['position']
    #if matrices['cellular_binary_grass'][int(y),int(x)]:
    # Eat the cell under the agent's position
    matrices['cellular_binary_grass'][int(y),int(x)] = False
    #endif
