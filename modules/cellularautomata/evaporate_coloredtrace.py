# -*- coding: utf-8 -*-
# License: See LICENSE file.

import numpy



required_matrices = ['coloredtrace']



def run(world, matrices):
    m = matrices['coloredtrace']
    numpy.multiply(m, 0.9999, m)
    m.set_modified()
