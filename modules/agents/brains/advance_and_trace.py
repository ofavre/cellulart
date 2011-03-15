# -*- coding: utf-8 -*-

required_percepts = ['get_age']
required_actions = ['advance','turnabit','trace','getolder','slowdownwithage']

def run(world, percepts, actions):
    # Do we die now?
    age = percepts['get_age']()
    if age <= 0:
        # Die
        return False
    # Draw a trace
    actions['trace']()
    # Go on to next position
    actions['advance']()
    # Add a random turn
    actions['turnabit']()
    # Slow down as we get older
    actions['slowdownwithage']()
    # Get older
    actions['getolder']()
    # Survive
    return True