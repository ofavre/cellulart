# -*- coding: utf-8 -*-

import math
import sys
import operator



required_states = []
required_matrices = []



def run(name, world, matrices, states, search_position=None, agent_otherwise_object=True, agentorobject_name=None, position_getter=lambda agent: agent.states['position'], dist_min=0.0, dist_max=float('inf'), filter=lambda obj,dist: True, distance=lambda origin,position: math.hypot(origin[0]-position[0],origin[1]-position[1]), count_max=sys.maxint, closer_before=True):
    if agentorobject_name == None: agentorobject_name = name
    if search_position == None: search_position = states['position']
    rtn = []
    # Iterate over each agents #TODO: A KD-Tree at least should be used to improve performances
    for obj in world.get_agents(agentorobject_name) if agent_otherwise_object else world.get_objects(agentorobject_name):
        position = position_getter(obj)
        dist = distance(search_position, position)
        # Filter by distance as asked in the parameters
        if dist_min <= dist and dist <= dist_max:
            if filter(obj, dist):
                rtn.append((obj, dist))
    # Return the closest/farther
    rtn.sort(key=operator.itemgetter(1), reverse=not closer_before)
    # Return only the asked number of results
    del rtn[count_max:]
    return rtn
