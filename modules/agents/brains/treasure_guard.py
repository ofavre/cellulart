# -*- coding: utf-8 -*-

import math
import random

import utils


required_percepts = ['get_state']
required_actions = ['set_state','set_coloredtrace','advance','turnabit','turn_toward']



def run(name, world, percepts, actions):
    # Hide our old position
    actions['set_pixel'](color=(0,0,0,0))
    default_walk = False
    has_treasure = percepts['get_state']('treasure', False)
    if has_treasure == False:
        # Get nearest theft with a stolen treasure
        thefts = percepts['agentorobject_rangequery'](agentorobject_name="treasure_theft", filter=lambda theft,dist: theft.states.get('treasure', False) != False, distance=utils.distance(world.get_shape(), utils.WRAP), count_max=1, dist_min=0, dist_max=50)
        try:
            theft, distance = thefts[0]
            # Add a trace
            actions['set_coloredtrace']()
            # Are we close enough to catch him?
            if distance < 1:
                # Take treasure away from him
                treasure = theft.states['treasure']
                del theft.states['treasure']
                actions['set_state']('treasure', treasure)
                # Stay in place for this step
                actions['set_state']('speed', 0)
            else:
                # Turn toward it
                actions['turn_toward'](*theft.states['position'], wrap=True, max_turn=math.pi/4)
                # Add a random turn
                actions['turnabit'](max_turn=math.pi/96)
                # Run!
                # Evict turning around each other with the theft
                # (0.0-1.0) middle value induce more turning, higher values makes it hard to catch the theft but less tightened circles
                # 0.001 break loops efficiently, making more straight lines
                # 1.0 makes many curves, but not many circles
                # 0.1 makes some straights lines, but many circles
                # 0.05 (the difference between the guards' and the theft's speed) starts to break circles fast enough)
                decelerate_if_close = .01
                actions['set_state']('speed', min(max(0,distance-decelerate_if_close),1.00))
        except IndexError:
            # No theft with treasure at sight
            # Add a random turn
            actions['turnabit'](max_turn=math.pi/12)
            # Walk
            actions['set_state']('speed', 0.50)
    else:
        # Get the treasure away from the theft
        thefts = percepts['agentorobject_rangequery'](agentorobject_name="treasure_theft", distance=utils.distance(world.get_shape(), utils.WRAP), count_max=1, dist_min=0, dist_max=50)
        try:
            theft, distance = thefts[0]
            # Turn away from him
            actions['turn_toward'](*theft.states['position'], wrap=True, get_closer=False, max_turn=math.pi/6)
            # Add a random turn
            actions['turnabit'](max_turn=math.pi/12)
            # Walk a bit faster than usual
            actions['set_state']('speed', 0.75)
        except IndexError:
            # No theft at sight
            # Drop the treasure
            treasure = percepts['get_state']('treasure')
            actions['set_state']('treasure', False)
            world.add_new_objects('treasure', [percepts['get_state']('position')])
            # Stay in place for this step
            actions['set_state']('speed', 0)
    # Go on to next position
    actions['advance']()
    # Mark our current position
    actions['set_pixel'](color=(0,255,0,255))
    # Survive
    return True
