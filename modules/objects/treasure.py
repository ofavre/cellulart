# -*- coding: utf-8 -*-
# License: See LICENSE file.

import random



def init(world, count=1, **kwargs):
    y,x = world.get_shape()
    y -= 1
    x -= 1
    objs = [(random.randint(0,y),random.randint(0,x)) for i in xrange(count)]
    world.add_new_objects('treasure', objs)

def created(world, object):
    pass

def exists(world, object):
    try:
        pixels = world.get_matrix('pixels')
    except:
        pass
    else:
        pixels[object] = (255,255,0,255)

def deleted(world, object):
    try:
        pixels = world.get_matrix('pixels')
    except:
        pass
    else:
        pixels[object] = (0,0,0,0)
