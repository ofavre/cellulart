# -*- coding: utf-8 -*-

required_matrices = ['cellular_binary_life']

def run(world, x, y, matrices):
    matrices['cellular_binary_life'][y,x] = not matrices['cellular_binary_life'][y,x]
