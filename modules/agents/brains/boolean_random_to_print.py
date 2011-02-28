# -*- coding: utf-8 -*-

required_percepts = ['boolean_random']
required_actions = ['print']

def run(self, percepts, actions):
    actions['print'](percepts['boolean_random']())
