# -*- coding: utf-8 -*-

import sys
import math
import random

import utils



required_percepts = ['get_state', 'agentorobject_rangequery', 'get_densezoneof_boolean', 'matrix_rangequery']
required_actions = ['set_state','advance','turnabit','turn_toward', 'eat_cellular_grass']



def run(name, world, percepts, actions):
    # Eat the grass under our feet
    actions['eat_cellular_grass']()
    # Hide our old position
    actions['set_pixel']((0,0,0,0))
    # Walk
    actions['set_state']('speed', 0.45)
    # Go to the closest cell with food, within a small radius
    foods = percepts['matrix_rangequery'](matrix_name='cellular_binary_grass', wrap=True, dist_max=4, filter=lambda val,pos,dist: val==True, count_max=1, closer_before=True)
    if len(foods) > 0:
        food_position = foods[0][1]
    else:
        # If no close food found
        # Get point of the highest density of food, within a larger radius
        position = percepts['get_state']('position')
        food_position,density = percepts['get_densezoneof_boolean']('cellular_binary_grass', initial_position=position, search_radius_in_zones=4, zone_size=8, search_for_max=True, wrap=True, return_value_if_same_zone=(None,0))
        if food_position == None:
            # Best zone is the current zone
            pass
        elif density == 0:
            # Highest density is "no food", don't use this information
            food_position = None
        else:
            # Found some food!
            pass
    # Get nearest cows
    dist_max=5
    cows = percepts['agentorobject_rangequery'](agentorobject_name='cow', distance=utils.distance(world.get_shape(), utils.WRAP), count_max=5, dist_min=0, dist_max=dist_max)
    if len(cows) > 1:
        del cows[0] # don't count ourself
        # Walk a bit faster
        actions['set_state']('speed', 0.55)
        mean_position = [0,0]
        weight = 0
        for cow, distance in cows:
            pos = cow.states['position']
            distance = dist_max - distance
            mean_position[0] += pos[0] * distance
            mean_position[1] += pos[1] * distance
            weight += distance
        position = percepts['get_state']('position')
        # Get opposite, get away from other cows
        mean_position[0] = 2*position[0] - mean_position[0]/weight
        mean_position[1] = 2*position[1] - mean_position[1]/weight
        # If the best food position is inside our area, get closer to it
        if food_position != None:
            food_distance = math.hypot(food_position[0]-position[0], food_position[1]-position[1])
            mean_distance = math.hypot(mean_position[0]-position[0], mean_position[1]-position[1])
            max_distance = max(food_distance, mean_distance)
            food_distance = dist_max - food_distance
            mean_distance = 2*(dist_max - mean_distance)
            weight = food_distance + mean_distance
            mean_position[0] *= mean_distance
            mean_position[1] *= mean_distance
            mean_position[0] += food_position[0] * food_distance
            mean_position[1] += food_position[1] * food_distance
            mean_position[0] /= weight
            mean_position[1] /= weight
        # Get toward food and away from the other cows
        actions['turn_toward'](mean_position[0], mean_position[1], wrap=True, get_closer=True, max_turn=math.pi/6)
    elif food_position != None:
        # Simply turn toward food if there are no neighbor cows
        actions['turn_toward'](food_position[0], food_position[1], wrap=True, get_closer=True, max_turn=math.pi/6)
    else:
        # We can see no food at all
        pass
    # Add a random turn
    actions['turnabit'](max_turn=math.pi/24)
    # Go on to next position
    actions['advance']()
    # Mark our current position
    actions['set_pixel']((255,255,255,255))
    # Trace
    actions['trace'](opacity=0.1)
    # Survive
    return True
