# -*- coding: utf-8 -*-
# License: See LICENSE file.

import numpy
import math
import sys
import operator


def run(name, world, matrices, states, matrix_name, search_position=None, agent_otherwise_object=True, agentorobject_name=None, position_getter=lambda agent: agent.states['position'], dist_max=float('inf'), filter=lambda value,position,distance: True, wrap=False, count_max=sys.maxint, closer_before=True):
    if search_position == None: search_position = states['position']
    search_position = [int(i) for i in search_position]
    matrix = world.get_matrix(matrix_name)
    if wrap == False:
        if dist_max > math.hypot(matrix.shape[0], matrix.shape[1]):
            dist_max = math.hypot(matrix.shape[0], matrix.shape[1])
    else:
        if dist_max > math.hypot(matrix.shape[0]/2, matrix.shape[1]/2):
            dist_max = math.hypot(matrix.shape[0]/2, matrix.shape[1]/2)
    rtn = []
    pos = [0,0]
    # For each possible dy (easy to find : -R,+R, with dx forcefully at 0)
    for dy in xrange(-int(math.floor(dist_max)), int(math.floor(dist_max))+1):
        # Set first coordinate, adjust according to the wrapping
        pos[0] = search_position[0]+dy
        if wrap:
            pos[0] %= matrix.shape[0]
        elif pos[0] < 0 or pos[0] >= matrix.shape[0]:
            # If we cannot wrap and we're outside, skip
            continue
        # Test first with a dx equal to 0
        pos[1] = search_position[1]
        dist = math.hypot(dy,0)
        val = matrix[tuple(pos)]
        if filter(val, tuple(pos), dist):
            rtn.append((val, tuple(pos), dist))
        # Now go as far as possible in 2 directions
        for xstep in -1,1:
            dx = xstep # dx=0 already done
            dist = math.hypot(dy,dx)
            # Stay in the search radius
            while dist < dist_max:
                # Set second coordinate, adjust according to the wrapping
                pos[1] = search_position[1]+dx
                if wrap:
                    pos[1] %= matrix.shape[1]
                elif pos[1] < 0 or pos[1] >= matrix.shape[1]:
                    # If no wrapping and outside, that's over for this direction
                    break
                # Test the new value
                val = matrix[tuple(pos)]
                if filter(val, pos, dist):
                    rtn.append((val, tuple(pos), dist))
                # Go further in that direction
                dx += xstep
                dist = math.hypot(dy,dx)
    # Return the closest/farther
    rtn.sort(key=operator.itemgetter(2), reverse=not closer_before)
    # Return only the asked number of results
    del rtn[count_max:]
    return rtn
