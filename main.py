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
world = World((32,32)) #FIXME: Some platform (ATI on Kubuntu 10.10 with Compiz, weird) require a power of 2 here!

# Adding matrices, first are top most, latter are displayed behind

# Add a named module matrix
m = world.get_or_create_matrix("cellular_binary_life")
m = world.get_or_create_matrix("trace")

# Add a named module cellular automaton
c = world.get_or_create_cellularautomaton("life")
c = world.get_or_create_cellularautomaton("mean_and_evaporate_trace")

# Add agents
a = world.get_or_create_agents("random_walker", 5)

# Create and launch the main GUI
gui = MainGUI(world)
gui.run()
