# -*- coding: utf-8 -*-
# License: See LICENSE file.

class CellularAutomaton(object):
    """Represents a cellular automaton, with a method to update over a given cell."""
    def __init__(self, run):
        self.run = run
    def run(self, world, matrices):
        """ Reads matrices and write into outputs.
            A standard implementation can loop over each cell to process an update rule.
            Optimized implementation may want to do more optimized stuff, so the loop is up to the implementor!
            Overridden in the constructor."""
        raise NotImplemented()
