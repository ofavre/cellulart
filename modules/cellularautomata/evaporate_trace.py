# -*- coding: utf-8 -*-

import random

required_matrices = ['trace']

def run(world, x, y, matrices):
    matrices['trace'][y,x] *= 0.95
