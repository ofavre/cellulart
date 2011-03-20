#!/usr/bin/python
# -*- coding: utf-8 -*-

from world import *
from maingui import *
from colors import *

import numpy

try:
    # i386-only optimization with Psyco
    # NOT TESTED: May be a memory hog and compilation may be a time hog as well!
    import psyco
    psyco.full()
except ImportError:
    pass



"""
The main entry point of the simulator.
For now, it creates a test world and launches the main GUI.
"""

# Create a n rows by m columns world
world = World((256,256)) #FIXME: Some platform (ATI on Kubuntu 10.10 with Compiz, weird) require a power of 2 here!

# Adding matrices, first are top most, latter are displayed behind

# Add a named module matrix
world.create_matrix("pixels")
world.create_matrix("trace")
#world.create_matrix("cellular_binary_life")

# Add a named module cellular automaton
#world.create_cellularautomaton("life")
world.create_cellularautomaton("evaporate_trace")

# Add agents
world.create_agents("treasure_theft", 5)
world.create_agents("treasure_guard", 10)

# Add a treasure at the center of the map!
world.create_objects("treasure", 3)

# Create and launch the main GUI
gui = MainGUI(world)
gui.run()
