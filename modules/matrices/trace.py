# -*- coding: utf-8 -*-
# License: See LICENSE file.

import colors
import random

dtype = float
track_updates = False
border = 'wrap'
colormap = colors.LinearGradientColormap(value_min=0.0, value_max=1.0, color_min=(0,0,0,0), color_max=(0,0,255,255))
visible = True
alpha = 1.0

def init(world, matrix):
    matrix.fill(0)
