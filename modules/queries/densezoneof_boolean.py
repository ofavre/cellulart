# -*- coding: utf-8 -*-

import numpy
import math

cache = {}

def run(world):
    global cache
    # New iteration, free the cache
    cache = {}

def query(world, matrix_name, initial_position, search_radius_in_zones=2, zone_size=8, search_for_max=True, wrap=False, return_value_if_same_zone=None):
    global cache
    matrix = world.get_matrix(matrix_name)
    if (matrix_name, zone_size, wrap) not in cache:
        # Reinterpret cast from bool (stored as uint8) to uint8
        mint = numpy.matrix(matrix, dtype=numpy.uint8, copy=False)
        # Temporary reduction along y axis
        mtmp = numpy.ndarray((matrix.shape[0]/zone_size,matrix.shape[1]),dtype=int)
        mtmp.fill(0)
        # Final reduction
        mout = numpy.ndarray((matrix.shape[0]/zone_size,matrix.shape[1]/zone_size),dtype=int)
        mout.fill(0)
        if wrap == False:
            for offset in xrange(zone_size):
                numpy.add(mtmp,numpy.take(mint,xrange(offset,matrix.shape[0],zone_size),axis=0),mtmp)
            for offset in xrange(zone_size):
                numpy.add(mout,numpy.take(mtmp,xrange(offset,matrix.shape[0],zone_size),axis=1),mout)
        else:
            for offset in xrange(zone_size):
                numpy.add(mtmp,numpy.take(numpy.roll(mint,offset,axis=0),xrange(0,matrix.shape[0],zone_size),axis=0),mtmp)
            for offset in xrange(zone_size):
                numpy.add(mout,numpy.take(numpy.roll(mtmp,offset,axis=1),xrange(0,matrix.shape[0],zone_size),axis=1),mout)
        m = mout
        cache[(matrix_name, zone_size, wrap)] = m
    else:
        m = cache[(matrix_name, zone_size, wrap)]
    # Transform the initial position into the new coordinate system, in zones
    if wrap == False:
        position_in_zone = (int(math.floor(initial_position[0] / float(zone_size))), int(math.floor(initial_position[1] / float(zone_size))))
    else:
        position_in_zone = (int(math.floor(initial_position[0] / float(zone_size))) % (matrix.shape[0]/zone_size), int(math.floor(initial_position[1] / float(zone_size))) % (matrix.shape[1]/zone_size))
    # Search for the optimal value
    # Initialize with the initial position
    bestPos = list(position_in_zone)
    bestValue = m[tuple(bestPos)]
    pos = [0,0]
    # For each possible dy (easy to find : -R,+R, with dx forcefully at 0)
    for dy in xrange(-search_radius_in_zones, search_radius_in_zones+1):
        # Set first coordinate, adjust according to the wrapping
        pos[0] = position_in_zone[0]+dy
        if wrap:
            pos[0] %= (matrix.shape[0]/zone_size)
        elif pos[0] < 0 or pos[0] >= matrix.shape[0]/zone_size:
            # If we cannot wrap and we're outside, skip
            continue
        # Test first with a dx equal to 0
        pos[1] = position_in_zone[1]
        val = m[tuple(pos)]
        if (search_for_max and val > bestValue) or (not search_for_max and val < bestValue):
            bestValue = val
            bestPos = list(pos)
        # Now go as far as possible in 2 directions
        for xstep in -1,1:
            dx = xstep # dx=0 already done
            # Stay in the search radius
            while math.hypot(dy,dx) < search_radius_in_zones:
                # Set second coordinate, adjust according to the wrapping
                pos[1] = position_in_zone[1]+dx
                if wrap:
                    pos[1] %= (matrix.shape[1]/zone_size)
                elif pos[1] < 0 or pos[1] >= matrix.shape[1]/zone_size:
                    # If no wrapping and outside, that's over for this direction
                    break
                # Test the new value
                val = m[tuple(pos)]
                if (search_for_max and val > bestValue) or (not search_for_max and val < bestValue):
                    bestValue = val
                    bestPos = list(pos)
                # Go further in that direction
                dx += xstep
    if bestPos == list(position_in_zone):
        return return_value_if_same_zone
    # Return the position in the original coordinate system, take the center
    rtn = [int(round((bestPos[0]+0.5)*zone_size)), int(round((bestPos[1]+0.5)*zone_size))]
    if wrap:
        rtn[0] %= matrix.shape[0]
        rtn[1] %= matrix.shape[1]
    else:
        rtn[0] = min(rtn[0], matrix.shape[0])
        rtn[1] = min(rtn[1], matrix.shape[1])
    return rtn, bestValue
