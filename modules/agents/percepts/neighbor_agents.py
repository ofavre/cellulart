# -*- coding: utf-8 -*-

import math
import sys
import operator



required_states = []
required_matrices = []



def run(name, world, matrices, states, dist_min=0.0, dist_max=float('inf'), count_max=sys.maxint, closer_before=True):
    y,x = states['position']
    rtn = []
    # Iterate over each agents #TODO: A KD-Tree at least should be used to improve performances
    for a in world.get_agents(name):
        # Skip the agent itself
        if a.states is states:
            continue
        ay,ax = a.states['position']
        dist = math.hypot(y-ay,x-ax)
        # Filter by distance as asked in the parameters
        if dist_min <= dist and dist <= dist_max:
            rtn.append((a, dist))
    # Return the closest/farther
    rtn.sort(key=operator.itemgetter(1), reverse=not closer_before)
    # Return only the asked number of results
    del rtn[count_max:]
    return rtn
