# -*- coding: utf-8 -*-

import math
import random

import utils
import operator


required_percepts = ['get_state']
required_actions = ['set_state','advance','turnabit','turn_toward']

def average_direction(long_range, actions):
    direction = 0
    for bird, distance in long_range:
        direction += bird.states['direction']
    if len(long_range) > 0:
        direction /= len(long_range)
        actions['set_state']('direction', direction)
    else:
        actions['turnabit'](max_turn=math.pi/10)

def average_position(long_range, world, actions):
    destx, desty = 0, 0
    for bird, distance in long_range:
        bx, by = bird.states['position']
        destx += bx
        desty += by
    if len(long_range) > 0:
        destx /= len(long_range)
        desty /= len(long_range)
        actions['turn_toward'](*(destx, desty), wrap=True, max_turn=math.pi/24)


def run(name, world, percepts, actions):
    # Hide our old position
    actions['set_pixel'](color=(0,0,0,0))
    actions['set_state']('speed', 1.00)
    short_range = percepts['agentorobject_rangequery'](agentorobject_name="flocking_bird", count_max=1000, dist_min=2, dist_max=10, distance=utils.distance(world.get_shape(), utils.WRAP))
    long_range = percepts['agentorobject_rangequery'](agentorobject_name="flocking_bird", count_max=1000, dist_min=3, dist_max=20, distance=utils.distance(world.get_shape(), utils.WRAP))
    short_range.sort(key=operator.itemgetter(1))

    average_direction(long_range, actions)
    average_position(long_range, world, actions)



    # Go on to next position
    actions['advance']()
    actions['trace']()
    # Mark our current position
    actions['set_pixel'](color=(0,255,255,255))
    # Survive
    return True
