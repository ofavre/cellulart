# -*- coding: utf-8 -*-

import numpy



required_matrices = ['trace']



def run(world, matrices):
    m = matrices['trace']
    numpy.multiply(m, 0.9999, m)
    m.set_modified()
