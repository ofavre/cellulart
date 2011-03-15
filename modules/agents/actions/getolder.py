# -*- coding: utf-8 -*-

required_states = ['age']
required_matrices = []

def run(world, matrices, states, *args, **kwargs):
    states['age'] -= 1
