# -*- coding: utf-8 -*-

import math
import random

import utils
import operator


required_percepts = ['get_state']
required_actions = ['set_state','advance','turnabit','turn_toward']



def run(name, world, percepts, actions):
    # Hide our old position
    actions['set_pixel']((0,0,0,0))
    actions['set_state']('speed', 0.50)
    neighbors = percepts['agentorobject_rangequery'](agentorobject_name="flocking_bird", count_max=10, dist_min=8, dist_max=30, distance=utils.distance(world.get_shape(), utils.WRAP))
    neighbors.sort(key=operator.itemgetter(1))

    try:
        bird, distance = neighbors[0]
        actions['turn_toward'](*bird.states['position'], wrap=True, max_turn=math.pi/6)
    except IndexError:
        # Add a random turn
        actions['turnabit'](max_turn=math.pi/24)


    # Go on to next position
    actions['advance']()
    actions['trace']()
    # Mark our current position
    actions['set_pixel']((0,255,255,255))
    # Survive
    return True
