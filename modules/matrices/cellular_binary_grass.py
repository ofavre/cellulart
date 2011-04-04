# -*- coding: utf-8 -*-

import colors
import random

dtype = bool
track_updates = False
border = 'wrap'
colormap = colors.BinaryBooleanColormap((0,0,0,0),(255,255,255,255))
visible = True
alpha = 0.1

def init(world, matrix):
    if True: # uniform
        for i in xrange(matrix.size):
            matrix.data[i] = '\x01' if random.random() < 0.4 else '\x00'
    else: # more in the center
        for y in xrange(matrix.shape[0]):
            py = 1 - abs(y - matrix.shape[0]/2) / float(matrix.shape[0]/2)
            py *= 2
            for x in xrange(matrix.shape[1]):
                px = 1 - abs(x - matrix.shape[1]/2) / float(matrix.shape[1]/2)
                px *= 2
                matrix[y,x] = True if random.random() < 0.4 * px * py else False
