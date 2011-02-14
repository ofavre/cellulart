# -*- coding: utf-8 -*-

from matrix import Matrix

import numpy



class World:
    """ The world is responsible for the life and states.
        The world is composed of multiple superposed named matrices of different data types,
        as well as some objects such as agents."""

    def __init__(self, shape):
        """Creates a new, empty world, with a fixed given shape (2D-size)."""
        self.__shape = shape
        self.__matrices = {}

    def get_shape(self):
        """Returns the shape (2D-size) of the world."""
        return self.__shape.__class__(self.__shape) # return a copy

    def add_matrix(self, name, dtype, track_updates=False):
        """ Creates a new named matrix with a given type, if the name is unique.
            Returns False if the matrix already exists.
            Returns the newly created matrix otherwise."""
        # Check for existance of such a named matrix
        if self.__matrices.has_key(name):
            return False
        # Create the new matrix
        m = Matrix(name, self.__shape, dtype, track_updates)
        self.__matrices[name] = m
        return m

    def get_matrix(self, name):
        """Returns the matrix of a given name."""
        return self.__matrices[name]

    def get_matrices(self):
        """Returns the known matrices."""
        return dict(self.__matrices) # return a copy of the matrices dictionnary (but a reference to the true matrices)
