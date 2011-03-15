# -*- coding: utf-8 -*-

class CellularAutomaton(object):
    """Represents a cellular automaton, with a method to update over a given cell."""
    def __init__(self, run):
        self.run = run
    def run(self, world, x, y, matrices):
        """ Called over each x,y couple, reads matrices and write into outputs.
            Overridden in the constructor."""
        raise NotImplemented()