# -*- coding: utf-8 -*-

import numpy

import colors



class Matrix(numpy.ndarray):
    """ A matrix is used to store a state for each cell of the world.
        It is actually a two dimensional array of a given fixed type."""

    # See http://docs.scipy.org/doc/numpy/user/basics.subclassing.html
    def __new__(subclass, world, index, name, shape, dtype, track_updates=False):
        """ Constructs and initialises a new matrix.
            track_updates: Whether or not to update the colored pixels while modifying the matrix,
                           or only once it is needed (for heavily modified matrices)"""
        # Create a new ndarray
        self = numpy.ndarray.__new__(subclass, shape, dtype)
        # Set local fields
        self.__world = world
        self.__name = name
        self.__colormap = colors.Colormap()
        self.__colormatrix = numpy.ndarray((shape[0],shape[1],4), numpy.uint8)
        self.__colormatrix_uptodate = False
        self.track_updates = track_updates
        self.visible = False
        self.alpha = 1.0
        self.__index = index
        return self
    # See http://docs.scipy.org/doc/numpy/user/basics.subclassing.html
    def __array_finalize__(self, obj):
        """?"""
        if obj is None: return
        # Not sure what to do here
        # I guess we are to copy attributes and functions from the main object (obj)
        # to a new view of it (self), for example constructed by a slice.
        self.visible = getattr(obj, 'visible', None)

    @property
    def colormap(self):
        """Defines the colormap used to transform the values in colored pixels."""
        return self.__colormap
    @colormap.setter
    def colormap(self, colormap):
        self.__colormatrix_uptodate = False
        self.__colormap = colormap

    @property
    def index(self):
        """Defines the index of the matrix in the matrix stack."""
        return self.__index
    @index.setter
    def index(self, index):
        index = self.__world._matrix_index_changed(self, self.__index, index)
        self.__index = index

    def get_name(self):
        """Returns the name of the matrix."""
        return str(self.__name) # return a copy

    def __setitem__(self, key, value):
        if self.__colormatrix_uptodate:
            if self.track_updates:
                self.__colormatrix[key] = self.__colormap(value)
            else:
                self.__colormatrix_uptodate = False
        return numpy.ndarray.__setitem__(self, key, value)

    def get_pixels(self):
        if not self.__colormatrix_uptodate:
            for y in xrange(self.shape[0]):
                for x in xrange(self.shape[1]):
                    self.__colormatrix[y,x] = self.__colormap(self[y,x])
            self.__colormatrix_uptodate = True
        return self.__colormatrix
