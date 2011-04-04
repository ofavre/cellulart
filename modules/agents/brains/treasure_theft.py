# -*- coding: utf-8 -*-

import math
import random

import utils



required_percepts = ['get_state']
required_actions = ['set_state','advance','turnabit','turn_toward']



def run(name, world, percepts, actions):
    # Hide our old position
    actions['set_pixel'](color=(0,0,0,0))
    # Seeking a treasure or fleeing away from the guards?
    has_treasure = percepts['get_state']('treasure', False)
    if has_treasure == False:
        # Walk
        actions['set_state']('speed', 0.45)
        # Get nearest treasure
        treasures = percepts['agentorobject_rangequery'](agent_otherwise_object=False, agentorobject_name="treasure", position_getter=lambda obj: obj, distance=utils.distance(world.get_shape(), utils.WRAP), count_max=1, dist_min=0, dist_max=50)
        try:
            treasure, distance = treasures[0]
            if distance < 0.5:
                # Take the treasure
                world.remove_objects('treasure',(treasure,))
                actions['set_state']('treasure', treasure)
                has_treasure = True
            else:
                # Turn toward it
                actions['turn_toward'](*treasure, wrap=True, max_turn=math.pi/6)
                # Add a random turn
                actions['turnabit'](max_turn=math.pi/48)
                # Walk faster
                # Do not go too fast if we may miss it by walking past it in one step
                actions['set_state']('speed', min(0.70,distance))
        except IndexError:
            # No treasure at sight
            # Add a random turn
            actions['turnabit'](max_turn=math.pi/24)
    if has_treasure != False:
        # Run!
        actions['set_state']('speed', 0.95)
        # Get nearest guards
        dist_max=20
        guards = percepts['agentorobject_rangequery'](agentorobject_name="treasure_guard", distance=utils.distance(world.get_shape(), utils.WRAP), count_max=5, dist_min=0, dist_max=dist_max)
        if len(guards) > 0:
            mean_position = [0,0]
            weight = 0
            for guard, distance in guards:
                pos = guard.states['position']
                distance = dist_max - distance
                mean_position[0] += pos[0] * distance
                mean_position[1] += pos[1] * distance
                weight += distance
            # Flee from them
            actions['turn_toward'](mean_position[0]/weight, mean_position[1]/weight, wrap=True, get_closer=False, max_turn=math.pi/6)
        # Add a random turn
        actions['turnabit'](max_turn=math.pi/48)
    # Go on to next position
    actions['advance']()
    # Mark our current position
    actions['set_pixel'](color=(255,0,0,255))
    # Survive
    return True
