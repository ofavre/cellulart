# -*- coding: utf-8 -*-

import colors
import random

dtype = bool
track_updates = True
border = 'wrap'
colormap = colors.BinaryGradientColormap((0,0,0,0),(255,255,255,255))
visible = True
alpha = 1.0

def init(world, matrix):
    for y in xrange(matrix.shape[0]):
        for x in xrange(matrix.shape[1]):
            matrix[y,x] = False #random.random() <= 0.3
    # A planner
    matrix[4,6] = True
    matrix[5,5] = True
    matrix[6,5] = True
    matrix[6,6] = True
    matrix[6,7] = True
