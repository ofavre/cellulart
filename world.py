# -*- coding: utf-8 -*-

import matrix
import modulesreader

import numpy



class World:
    """ The world is responsible for the life and states.
        The world is composed of multiple superposed named matrices of different data types,
        as well as some objects such as agents."""

    def __init__(self, shape):
        """Creates a new, empty world, with a fixed given shape (2D-size)."""
        self.__shape = shape
        self.__matrices = {} # name to matrix
        self.__matrices_list = [] # front to back matrix drawing order
        self.__matrices_are_updating_index = False # flag indicating whether a grouped index update is being performed
        self.__agents = {}
        self.__cellularautomata = {}
        self.__lsystems = {}

    def get_shape(self):
        """Returns the shape (2D-size) of the world."""
        return self.__shape.__class__(self.__shape) # return a copy

    def get_or_create_matrix(self, name):
        try:
            return self.__matrices[name]
        except KeyError:
            matrix = modulesreader.ModulesReaderInstance.create_matrix(self, len(self.__matrices_list), name, self.__shape)
            return self.add_matrix(name, matrix)
    def add_matrix(self, name, matrix):
        self.__matrices_list.append(matrix)
        if matrix.index != len(self.__matrices_list)-1:
            matrix.index = len(self.__matrices_list)-1
        self.__matrices[name] = matrix
        return matrix

    def get_matrix(self, name):
        """Returns the matrix of a given name."""
        return self.__matrices[name]

    def get_matrices_list(self):
        """Returns the known matrices."""
        return list(self.__matrices_list) # return a copy of the matrices list (but a reference to the true matrices)

    def get_matrices_dict(self):
        """Returns the known matrices."""
        return dict(self.__matrices) # return a copy of the matrices dict (but a reference to the true matrices)

    def set_matrix_index(self, name, index):
        """ Modifies the index of a matrix, reodering the necessary ones.
            Equivalent to directly setting the index property on the corresponding matrix."""
        self.__matrices[name].index = index
    def _matrix_index_changed(self, matrix, old_index, new_index):
        """ Notified (or rather called as it is not a signal), when a matrix has been changed its index value.
            Changes the drawing list order accordindly and shifts the necessary other matrices.
            Returns the new index the matrix should set internally (for potential range ensurance)."""
        # Ensure the new index is correct
        new_index = max(0,min(len(self.__matrices_list)-1,int(new_index)))
        # Skip if no real change, or if a batch update is already going on
        if old_index == new_index or self.__matrices_are_updating_index:
            return new_index
        else:
            # Flag a batch update
            self.__matrices_are_updating_index = True
        # Shift the other matrices between the old and the new position accordingly to the direction of the initial change (bring to front, send to back)
        if old_index < new_index:
            for i in xrange(old_index+1,new_index+1):
                self.__matrices_list[i].index -= 1
        else:
            for i in xrange(new_index,old_index):
                self.__matrices_list[i].index += 1
        # Also impact the changes on the drawing list
        self.__matrices_list.insert(new_index, self.__matrices_list.pop(old_index))
        # End of batch update
        self.__matrices_are_updating_index = False
        return new_index

    def get_or_create_agent(self,name):
        try:
            return self.__agents[name]
        except KeyError:
            agent = modulesreader.ModulesReaderInstance.create_agent(name)
            return self.add_agent(name, agent)
    def add_agent(self, name, agent):
        self.__agents[name] = agent
        return agent

    def get_or_create_cellularautomaton(self,name):
        try:
            return self.__cellularautomata[name]
        except KeyError:
            cellularautomaton = modulesreader.ModulesReaderInstance.create_cellularautomaton(name)
            return self.add_cellularautomaton(name, cellularautomaton)
    def add_cellularautomaton(self, name, cellularautomaton):
        self.__cellularautomata[name] = cellularautomaton
        return cellularautomaton

    def step(self):
        for matrix in self.__matrices_list:
            matrix.defer_writes_begin()
        for name,cellularautomaton in self.__cellularautomata.iteritems():
            for y in xrange(self.__shape[0]):
                for x in xrange(self.__shape[1]):
                    cellularautomaton.run(self, x, y, self.__matrices)
        for matrix in self.__matrices_list:
            matrix.defer_writes_end()
