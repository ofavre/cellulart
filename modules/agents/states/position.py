# -*- coding: utf-8 -*-

import random

def init(world):
    """ Position is a tuple of floats ranging between 0 and the y/x shape of the world.
        The first number is the y ordinate, the second is the x ordinate.
        To get a y,x index for matrices, do not forget to convert to int with the following code:
        int(position[0]),int(position[1])."""
    return random.random()*world.get_shape()[0], random.random()*world.get_shape()[1]
