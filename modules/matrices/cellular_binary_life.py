# -*- coding: utf-8 -*-
# License: See LICENSE file.

import colors
import random

dtype = bool
track_updates = False
border = 'wrap'
colormap = colors.BinaryBooleanColormap((0,0,0,0),(255,255,255,255))
visible = True
alpha = 0.1

def init(world, matrix):
    matrix.fill(False)
    xmax = matrix.shape[1]-1
    ymax = matrix.shape[0]-1
    for y in xrange(matrix.shape[0]):
        matrix[y,0] = matrix[y,xmax] = True
    for x in xrange(matrix.shape[1]):
        matrix[0,x] = matrix[ymax,x] = True
    # A planner
    #matrix[5,5] = matrix[6,6] = matrix[6,7] = matrix[5,7] = matrix[4,7] = True
