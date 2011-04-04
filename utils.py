# -*- coding: utf-8 -*-
# License: See LICENSE file.

import math



CLASSIC = 0
WRAP = 1
#MOBIUS = 2



def distance(world_shape, type=CLASSIC):
    def distance_classic(a,b):
        val = 0.0
        for ad,bd in zip(a,b):
            val += (ad-bd)**2
        return math.sqrt(val)
    def distance_wrap(a,b):
        val = 0.0
        i = 0
        for ad,bd in zip(a,b):
            di = world_shape[i]
            ad %= di
            bd %= di
            dist = abs(ad-bd)
            if ad < bd:
                dist2 = abs(ad+di-bd)
                if dist2 < dist:
                    dist = dist2
            else:
                dist2 = abs(ad-(bd+di))
                if dist2 < dist:
                    dist = dist2
            val += dist**2
            i += 1
        return math.sqrt(val)
    if type == CLASSIC:
        return distance_classic
    elif type == WRAP:
        return distance_wrap
    else:
        return None



def weighted_sum_wrap(value1, weight1, value2, weight2, wrap_length):
    if value1 < value2 and (value1+wrap_length)-value2 < value2-value1:
        value1 += wrap_length
    elif value2 < value1 and (value2+wrap_length)-value1 < value1-value2:
        value2 += wrap_length
    return (  (weight1*value1 + weight2*value2) / (weight1+weight2)  ) % wrap_length
