#!/usr/bin/python
# -*- coding: utf-8 -*-
# License: See LICENSE file.

from world import *
from maingui import *
from colors import *

import numpy
import sys

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

demos = [
        'moo',
        'conway',
        'thefts and guards',
        'flocking birds'
    ]

demo = 'flocking birds'


if demo == 'moo':
    # Create a n rows by m columns world
    world = World((256,256)) #FIXME: Some platform (ATI on Kubuntu 10.10 with Compiz, weird) require a power of 2 here!

    # Adding matrices, first are top most, latter are displayed behind

    # Add a named module matrix
    world.create_matrix("pixels")
    world.create_matrix("trace")
    world.create_matrix("cellular_binary_grass")

    # Add a named module cellular automaton
    world.create_cellularautomaton("grass")
    world.create_cellularautomaton("evaporate_trace")

    # Add agents
    world.create_agents("cow", 100)


elif demo == 'conway':
    # Create a n rows by m columns world
    world = World((256,256)) #FIXME: Some platform (ATI on Kubuntu 10.10 with Compiz, weird) require a power of 2 here!

    # Adding matrices, first are top most, latter are displayed behind

    # Add a named module matrix
    world.create_matrix("cellular_binary_life")

    # Add a named module cellular automaton
    world.create_cellularautomaton("life")


elif demo == 'thefts and guards':
    # Create a n rows by m columns world
    world = World((256,256)) #FIXME: Some platform (ATI on Kubuntu 10.10 with Compiz, weird) require a power of 2 here!

    # Adding matrices, first are top most, latter are displayed behind

    # Add a named module matrix
    world.create_matrix("pixels")
    world.create_matrix("coloredtrace")

    # Add a named module cellular automaton
    world.create_cellularautomaton("evaporate_coloredtrace")

    # Add agents
    world.create_agents("treasure_theft", 50)
    world.create_agents("treasure_guard", 100)

    # Add a treasure at the center of the map!
    world.create_objects("treasure", 30)


elif demo == 'flocking birds':
    # Create a n rows by m columns world
    world = World((512,512)) #FIXME: Some platform (ATI on Kubuntu 10.10 with Compiz, weird) require a power of 2 here!

    # Adding matrices, first are top most, latter are displayed behind

    # Add a named module matrix
    world.create_matrix("pixels")
    world.create_matrix("coloredtrace")

    # Add a named module cellular automaton
    #world.create_cellularautomaton("evaporate_trace")

    # Add agents
    world.create_agents("flocking_bird", 42)


else:
    print >> sys.stderr, "Desired demo not available!"
    sys.exit(1)



# Create and launch the main GUI
gui = MainGUI(world)
gui.run()
