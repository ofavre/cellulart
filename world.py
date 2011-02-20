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
        self.__matrices_list = []
        self.__matrices_are_updating_index = False

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
        m = Matrix(self, len(self.__matrices_list), name, self.__shape, dtype, track_updates)
        self.__matrices[name] = m
        self.__matrices_list.append(m)
        return m

    def get_matrix(self, name):
        """Returns the matrix of a given name."""
        return self.__matrices[name]

    def get_matrices(self):
        """Returns the known matrices."""
        return list(self.__matrices_list) # return a copy of the matrices list (but a reference to the true matrices)

    def set_matrix_index(self, name, index):
        self.__matrices[name].index = index
    def _matrix_index_changed(self, matrix, old_index, new_index):
        new_index = max(0,min(len(self.__matrices_list)-1,int(new_index)))
        if old_index == new_index or self.__matrices_are_updating_index:
            return new_index
        else:
            self.__matrices_are_updating_index = True
        if old_index < new_index:
            for i in xrange(old_index+1,new_index+1):
                self.__matrices_list[i].index -= 1
            self.__matrices_list.insert(new_index, self.__matrices_list.pop(old_index))
        else:
            for i in xrange(new_index,old_index):
                self.__matrices_list[i].index += 1
            self.__matrices_list.insert(new_index, self.__matrices_list.pop(old_index))
        self.__matrices_are_updating_index = False
        return new_index
