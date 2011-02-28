# -*- coding: utf-8 -*-

class Agent(object):
    """Represents an agent, with a bunch of brains."""
    def __init__(self, default_states, brains):
        #TODO: Workout what to do with the states
        self.states = dict(default_states)
        self.brains = brains
    def run(self, percepts, actions):
        # Action wrapper for agent's states
        action_wrappers = {}
        for n,a in enumerate(actions):
            #TODO: Implement a mean of the arguments, before calling the actions
            def state_wrapper(*args, **kwargs):
                a(self.world.get_matrices_dict(), self.states, *args, **kwargs)
            action_wrappers[n] = state_wrapper
        percept_wrappers = {}
        for n,p in enumerate(actions):
            def state_wrapper(*args, **kwargs):
                p(self.world.get_matrices_dict(), self.states, *args, **kwargs)
            percept_wrappers[n] = state_wrapper
        for b in self.brains:
            b.run(percept_wrappers, action_wrappers)

class State(object):
    """Represents a state, with a method to get an initial value."""
    def __init__(self, init):
        self.init = init
    def init(self):
        """ Returns a new initial value for the represented state.
            Overridden in the constructor."""
        raise NotImplemented()

class Percept(object):
    """Represents a percept, with a method to get its value."""
    def __init__(self, run):
        self.run = run
    def run(self, matrices, states):
        """ Returns a value.
            Overridden in the constructor."""
        raise NotImplemented()

class Brain(object):
    """ Represents a brain, with a method to make it do stuff."""
    def __init__(self, run):
        self.run = run
    def run(self, percepts, actions):
        """ Asks percepts, takes actions.
            Overridden in the constructor."""
        raise NotImplemented()

class Action(object):
    """Represents an action, with a method to take the action."""
    def __init__(self, run):
        self.run = run
    def run(self, matrices, states, *args, **kwargs):
        """ Takes the action.
            Overridden in the constructor."""
        raise NotImplemented()
