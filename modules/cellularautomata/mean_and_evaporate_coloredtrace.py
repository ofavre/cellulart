# -*- coding: utf-8 -*-
# License: See LICENSE file.

import numpy



required_matrices = ['coloredtrace']



def run(world, matrices):
    m = matrices['coloredtrace']
    # We need to use a copy for temporary results
    mean = numpy.ndarray(m.shape, dtype=m.dtype)
    # Initialize it with the current values, attenuated
    numpy.multiply(m, 0.95, mean)
    # Then add after having shifted the lines and columns as needed to iterate over the 8 neigbors
    numpy.add(mean, numpy.roll(m, -1, axis=0), mean)
    numpy.add(mean, numpy.roll(m, 1, axis=0), mean)
    numpy.add(mean, numpy.roll(m, -1, axis=1), mean)
    numpy.add(mean, numpy.roll(m, 1, axis=1), mean)
    numpy.add(mean, numpy.roll(numpy.roll(m, -1, axis=0), -1, axis=1), mean)
    numpy.add(mean, numpy.roll(numpy.roll(m, 1, axis=0), -1, axis=1), mean)
    numpy.add(mean, numpy.roll(numpy.roll(m, -1, axis=0), 1, axis=1), mean)
    numpy.add(mean, numpy.roll(numpy.roll(m, 1, axis=0), 1, axis=1), mean)
    # Finally divide to calculate a mean (and directly overrite the destination matrix)
    numpy.divide(mean, 9, m)
    m.set_modified()
