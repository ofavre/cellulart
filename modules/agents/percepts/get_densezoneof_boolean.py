# -*- coding: utf-8 -*-

required_states = []
required_matrices = ['cellular_binary_grass']

def run(name, world, matrices, states, *args, **kwargs):
    return world.get_query('densezoneof_boolean').query(*([world]+list(args)), **kwargs)
