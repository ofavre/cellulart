# -*- coding: utf-8 -*-

class Agent(object):
    """Represents an agent, with a bunch of brains."""
    def __init__(self, world, default_states, brains):
        self.world = world
        self.states = dict([(name, state.init(world)) for name,state in default_states.iteritems()])
        self.brains = brains
    def run(self, world, percepts, actions):
        # Action and percepts wrapper for world, matrices and agent's states additions
        def return_state_wrapper(runnable_object, *wrapper_args):
            def state_wrapper(*args, **kwargs):
                return runnable_object.run(*(wrapper_args+args), **kwargs)
            return state_wrapper
        # Wrap percepts
        percept_wrappers = {}
        for n,p in percepts.iteritems():
            #TODO: Implement a mean of the arguments, before calling the actions
            percept_wrappers[n] = return_state_wrapper(p, world, world.get_matrices_dict(), self.states)
        # Wrap actions
        action_wrappers = {}
        for n,a in [(n,a) for n,a in actions.iteritems()]:
            action_wrappers[n] = return_state_wrapper(a, world, world.get_matrices_dict(), self.states)
        # Run brains
        dies = False
        for b in self.brains:
            if not b.run(world, percept_wrappers, action_wrappers):
                dies = True
        return not dies

class State(object):
    """Represents a state, with a method to get an initial value."""
    def __init__(self, init):
        self.init = init
    def init(self, world):
        """ Returns a new initial value for the represented state.
            Overridden in the constructor."""
        raise NotImplemented()

class Percept(object):
    """Represents a percept, with a method to get its value."""
    def __init__(self, run):
        self.run = run
    def run(self, world, matrices, states, *args, **kwargs):
        """ Returns a value.
            Overridden in the constructor."""
        raise NotImplemented()

class Brain(object):
    """ Represents a brain, with a method to make it do stuff."""
    def __init__(self, run):
        self.run = run
    def run(self, world, percepts, actions):
        """ Asks percepts, takes actions.
            Overridden in the constructor."""
        raise NotImplemented()

class Action(object):
    """Represents an action, with a method to take the action."""
    def __init__(self, run):
        self.run = run
    def run(self, world, matrices, states, *args, **kwargs):
        """ Takes the action.
            Overridden in the constructor."""
        raise NotImplemented()
