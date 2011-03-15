# -*- coding: utf-8 -*-

required_percepts = ['boolean_random']
required_actions = ['print','getolder']

def run(world, percepts, actions):
    pvalue = percepts['boolean_random']()
    actions['getolder']()
    actions['print'](pvalue)
    return True
