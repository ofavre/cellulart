# -*- coding: utf-8 -*-
# License: See LICENSE file.

import colors
import random

dtype = "(4,)uint8"
track_updates = False # because of the CopyColormap: no need to use the slow pixel by pixel copy, let's use the matrix replacement, way faster
border = 'wrap'
colormap = colors.CopyColormap()
visible = True
alpha = 1.0

def init(world, matrix):
    matrix.fill(0)
