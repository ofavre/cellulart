# -*- coding: utf-8 -*-

required_states = ['position', 'color']
required_matrices = ['coloredtrace']



def color_mix(colorSrc, colorDst, dstAlpha):
    return tuple([colorDst[i]*dstAlpha + colorSrc[i]*(1-dstAlpha) for i in xrange(4)])

def run(name, world, matrices, states, y=None, x=None, color=None, opacity=1.0):
    if color == None:
        color = states['color']
    if y == None:
        pos = states['position']
        y = pos[0]
        if x == None:
            x = pos[1]
    elif x == None:
        x = states['position'][1]
    opacity = max(0.0,min(1.0,opacity))
    iy = int(y)
    ix = int(x)
    rx = x % 1.0
    ry = y % 1.0
    if rx > 0.5:
        dx = 1
        rx = 1-rx
    else:
        dx = -1
    if ry > 0.5:
        dy = 1
        ry = 1-ry
    else:
        dy = -1
    matrice = matrices['coloredtrace']
    matrice[iy,   ix   ] = color_mix(matrice[iy,   ix   ], color, (ry+0.5)*(rx+0.5)*opacity)
    matrice[iy,   ix+dx] = color_mix(matrice[iy,   ix+dx], color, (ry+0.5)*(0.5-rx)*opacity)
    matrice[iy+dy,ix   ] = color_mix(matrice[iy+dy,ix   ], color, (0.5-ry)*(rx+0.5)*opacity)
    matrice[iy+dy,ix+dx] = color_mix(matrice[iy+dy,ix+dx], color, (0.5-ry)*(0.5-rx)*opacity)
