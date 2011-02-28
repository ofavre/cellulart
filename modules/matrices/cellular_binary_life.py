# -*- coding: utf-8 -*-

import colors
import random

dtype = bool
track_updates = True
colormap = colors.LinearGradientColormap(value_min=False, value_max=True, color_min=(0,0,0,255), color_max=(255,255,255,255))
visible = True
alpha = 1.0

def init(matrix):
    for y in xrange(matrix.shape[0]):
        for x in xrange(matrix.shape[1]):
            matrix[y,x] = random.random() <= 0.3
