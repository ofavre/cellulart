#!/usr/bin/python
# -*- coding: utf-8 -*-

from world import *
from maingui import *
from colors import *

import numpy



"""
The main entry point of the simulator.
For now, it creates a test world and launches the main GUI.
"""

# Create a n rows by m columns world
world = World((240,320))

# Add a test matrix of float
m = world.add_matrix("test",numpy.float, track_updates=True)
# Initialise it
for y in xrange(m.shape[0]):
    for x in xrange(m.shape[1]):
        m[y,x] = numpy.random.random()**2
# Give it a colormap
m.colormap = LinearGradientColormap(value_min=0, value_max=1, color_min=(255,255,0,255), color_max=(255,0,0,255))
# Set it to visible
m.visible = True

# Add a hidden matrix
m = world.add_matrix("hidden",numpy.float)
for y in xrange(m.shape[0]):
    for x in xrange(m.shape[1]):
        m[y,x] = numpy.random.random()**2
# Give it a colormap
m.colormap = LinearGradientColormap(value_min=0, value_max=1, color_min=(0,0,0,255), color_max=(0,255,0,255))
# Set it to invisible
m.visible = False

# Add a second matrix of booleans
m = world.add_matrix("boolean",numpy.bool, track_updates=True)
# Initialise it
for y in xrange(m.shape[0]):
    for x in xrange(m.shape[1]):
        m[y,x] = numpy.random.random() >= 0.5
# Give it a colormap with a lower bound (False) set to full transparency
m.colormap = LinearGradientColormap(value_min=False, value_max=True, color_min=(0,0,0,0), color_max=(0,0,255,255))
# Set it to visible
m.visible = True
# Let it be translucent
m.alpha = 0.5

# Create and launch the main GUI
gui = MainGUI(world)
gui.run()
