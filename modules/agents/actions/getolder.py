# -*- coding: utf-8 -*-
# License: See LICENSE file.

required_states = ['age']
required_matrices = []

def run(name, world, matrices, states, older_by=1):
    states['age'] -= older_by
