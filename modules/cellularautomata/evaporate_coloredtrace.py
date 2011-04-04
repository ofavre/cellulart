# -*- coding: utf-8 -*-
# License: See LICENSE file.

import numpy



required_matrices = ['coloredtrace']


decrement_every_n_steps = 5
step_count = 0


def run(world, matrices):
    global step_count, decrement_every_n_steps
    step_count += 1
    if step_count % decrement_every_n_steps == 0:
        m = matrices['coloredtrace']
        decr = numpy.ndarray((4,),dtype=numpy.uint8)
        decr[:] = (0,0,0,1)
        mm1 = numpy.subtract(m, decr)
        mout = numpy.where(m > 0, mm1, m)
        m.data[:] = mout.data
        m.set_modified()
