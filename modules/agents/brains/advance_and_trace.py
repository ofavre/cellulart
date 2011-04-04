# -*- coding: utf-8 -*-
# License: See LICENSE file.

import math
import random



required_percepts = ['get_age', 'in_smelling_trace', 'agentorobject_rangequery']
required_actions = ['advance','turnabit','trace','getolder','slowdownwithage','eat_cellular_life', 'parthenogenesis', 'turn_toward']



def run(name, world, percepts, actions):
    # Do we die now?
    age = percepts['get_age']()
    if age <= 0:
        # Die
        return False
    # Breed if young enough, in a very "smelling" part of the trace matrix (ie, near an agent passing by earlier), and if luck
    if age > 10 and age < 100 and random.random() < 0.2:
        t = percepts['get_trace']()
        if t >= 0.1 and t <= 0.2:
            actions['parthenogenesis']()
            actions['getolder'](10)
    # Eat a cell
    actions['eat_cellular_life']()
    # Draw a trace
    actions['trace']()
    # Get nearest agent
    neighbors = percepts['agentorobject_rangequery'](wrap=True, count_max=1, dist_min=10, dist_max=40)
    try:
        nearest_neighbor, distance = neighbors[1] # the first neighbor is forcefully the agent itself
        # Turn toward it
        actions['turn_toward'](*nearest_neighbor.states['position'], max_turn=math.pi/6)
    except IndexError:
        # No neighbors
        pass
    # Add a random turn
    actions['turnabit'](max_turn=math.pi/24)
    # Go on to next position
    actions['advance']()
    # Slow down as we get older
    actions['slowdownwithage']()
    # Get older
    actions['getolder']()
    # Survive
    return True