# -*- coding: utf-8 -*-

import colors
import random

dtype = bool
track_updates = True
border = 'wrap'
colormap = colors.LinearGradientColormap(value_min=False, value_max=True, color_min=(0,0,0,0), color_max=(255,255,255,255))
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
