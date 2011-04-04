# -*- coding: utf-8 -*-
# License: See LICENSE file.

import math
import random

import utils
import operator


required_percepts = ['get_state']
required_actions = ['set_state','set_coloredtrace', 'advance','turnabit','turn_toward']

def average_direction(long_range, actions):
    direction = 0
    for bird, distance in long_range:
        direction += bird.states['direction']
    if len(long_range) > 0:
        direction /= len(long_range)
        actions['set_state']('direction', direction)
    else:
        actions['turnabit'](max_turn=math.pi/24)

def average(agent_list, world):
    shape = world.get_shape()
    mean_x, mean_y = 0, 0
    weight_x, weight_y = 0, 0
    for agent, dist in agent_list:
        ax, ay = agent.states['position']
        mean_x = utils.weighted_sum_wrap(mean_x, weight_x, ax, 1, shape[0])
        weight_x += 1
        mean_y = utils.weighted_sum_wrap(mean_y, weight_y, ay, 1, shape[1])
        weight_y += 1
    return (mean_x, mean_y)

def average_position(long_range, world, actions):
    if len(long_range) > 0:
        actions['turn_toward'](*average(long_range, world), wrap=True, max_turn=math.pi/10)

def local_repulsion(short_range, world, actions):
    if len(short_range) > 0:
        actions['turn_toward'](*average(short_range, world), wrap=True, max_turn=math.pi/5, get_closer=False)
        actions['advance']()


def run(name, world, percepts, actions):
    # Hide our old position
    actions['set_pixel'](color=(0,0,0,0))
    actions['set_state']('speed', 0.80)
    short_range = percepts['agentorobject_rangequery'](agentorobject_name="flocking_bird", count_max=1000, dist_min=0.3, dist_max=4, distance=utils.distance(world.get_shape(), utils.WRAP))
    short_range.sort(key=operator.itemgetter(1))

    if not local_repulsion(short_range, world, actions):
        long_range = percepts['agentorobject_rangequery'](agentorobject_name="flocking_bird", count_max=1000, dist_min=3, dist_max=20, distance=utils.distance(world.get_shape(), utils.WRAP))
        average_direction(long_range, actions)
        average_position(long_range, world, actions)
        actions['advance']()



    # Go on to next position
    actions['set_coloredtrace']()
    # Mark our current position
    actions['set_pixel'](color=(0,255,255,255))
    # Survive
    return True
