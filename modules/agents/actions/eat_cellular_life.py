# -*- coding: utf-8 -*-


required_states = ['position','age']
required_matrices = ['cellular_binary_life']

def run(world, matrices, states, *args, **kwargs):
    y,x = states['position']
    if matrices['cellular_binary_life'][int(y),int(x)]:
        # Eat the cell under the agent's position
        matrices['cellular_binary_life'][int(y),int(x)] = False
        # And give an extra lifetime
        states['age'] += 10
