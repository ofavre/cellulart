# -*- coding: utf-8 -*-

def border_check(shape,x,y):
    xq = int(x / shape[1])
    xr = x % shape[1]
    yq = int(y / shape[0])
    yr = y % shape[0]
    if xq % 2 == 1:
        if yq % 2 == 1:
            return (xr, yr)
        else:
            return (xr, shape[0]-1 - yr)
    else:
        if yq % 2 == 1:
            return (shape[1]-1 - xr, yr)
        else:
            return (xr, yr)
