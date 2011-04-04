# -*- coding: utf-8 -*-
# License: See LICENSE file.

class Query(object):
    """Represents query."""
    def __init__(self, run, query):
        self.run = run
        self.query = query
    def run(self, world, *args, **kwargs):
        """ Reinitializes the object.
            Overridden in the constructor."""
        raise NotImplemented()
    def query(self, world, *args, **kwargs):
        """ Launches a query.
            Overridden in the constructor."""
        raise NotImplemented()
