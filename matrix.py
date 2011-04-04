# -*- coding: utf-8 -*-
# License: See LICENSE file.

import numpy

import colors



class Matrix(numpy.ndarray):
    """ A matrix is used to store a state for each cell of the world.
        It is actually a two dimensional array of a given fixed type."""

    # See http://docs.scipy.org/doc/numpy/user/basics.subclassing.html
    def __new__(subclass, world, index, name, shape, dtype, track_updates, border):
        """ Constructs and initialises a new matrix.
            track_updates: Whether or not to update the colored pixels while modifying the matrix,
                           or only once it is needed (for heavily modified matrices)"""
        # Create a new ndarray
        self = numpy.ndarray.__new__(subclass, shape, dtype)
        # Set local fields
        self.__world = world
        self.__index = index
        self.__name = name
        self.__colormap = colors.Colormap()
        self.__colormatrix = numpy.ndarray((shape[0],shape[1],4), numpy.uint8)
        self.__colormatrix_uptodate = False
        self.__writes_deferred = False
        self.track_updates = track_updates
        self.visible = False
        self.alpha = 1.0
        self.border_check = border
        return self
    """# See http://docs.scipy.org/doc/numpy/user/basics.subclassing.html
    def __array_finalize__(self, obj):
        " " " ? " " "
        if obj is None: return
        # Not sure what to do here
        # I guess we are to copy attributes and functions from the main object (obj)
        # to a new view of it (self), for example constructed by a slice.
        self.visible = getattr(obj, 'visible', None)"""

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
        # Asks the world to change our index, and update the other's
        index = self.__world._matrix_index_changed(self, self.__index, index)
        self.__index = index

    def get_name(self):
        """Returns the name of the matrix."""
        return str(self.__name) # return a copy

    def set_modified(self):
        self.__colormatrix_uptodate = False

    def __getitem__(self, key):
        try:
            # If key is iterable, we are using the [y,x] notation, use border_check
            it = iter(key)
            return numpy.ndarray.__getitem__(self, self.border_check(self.shape, *key))
        except TypeError:
            # Otherwise, we may be inside a call to str(self) and we should not interfere
            return numpy.ndarray.__getitem__(self, key)


    def __setitem__(self, key, value):
        """ Updates the given cell for the given value.
            This methods spies on the modifications on the matrix,
            and updates the colormatrix accordingly if changes are tracked.
            This methods also takes care of deferred writes by recording them."""
        key = self.border_check(self.shape, *key)
        # Are writes deferred?
        if self.__writes_deferred:
            # Are updates tracked?
            if self.track_updates:
                # Record this update (replace any previous update for the same cell)
                try:
                    # If an update has already been recorder, update if it differs (we have it's value at hand anyway)
                    if self.__updates[key] != value:
                        self.__updates[key] = value
                except KeyError:
                    # If not, record only if it differs from the original value
                    if numpy.ndarray.__getitem__(self, key) != value:
                        self.__updates[key] = value
                return value
            else:
                # Update the updated copy of the matrix
                self.__updates[key] = value
                return value
        # No deferred writes
        else:
            # No need to track anything if we're not up to date
            if self.__colormatrix_uptodate:
                # If we're tracking every single change
                if self.track_updates:
                    # Make sure the value has indeed changed
                    if self.__getitem__(key) == value:
                        # Skip any updates (including the last, return line)
                        return value
                    # Update the colormatrix accordingly
                    self.__colormatrix[key] = self.__colormap.get_color(value)
                # Otherwise, we are now no longer up to date
                else:
                    self.__colormatrix_uptodate = False
            # Perform the real value update
            return numpy.ndarray.__setitem__(self, key, value)

    def get_pixels(self):
        """ Returns the associated colormatrix.
            Performs a lazy update of changes have not been tracked."""
        # Update the colormatrix if need to
        if not self.__colormatrix_uptodate:
            self.__colormap.convert_matrix(self, self.__colormatrix)
            # We are now up to date
            self.__colormatrix_uptodate = True
        return self.__colormatrix

    def defer_writes_begin(self):
        """Start to defer writes to the matrix."""
        self.__writes_deferred = True
        # Are updates tracked?
        if self.track_updates:
            # Dictionnary of key:value, with key as defined in __setitem__
            self.__updates = {}
        else:
            # New matrix hosting every changes
            # In case of few cells not being updated, we are creating a full copy
            self.__updates = numpy.ndarray(self.shape, self.dtype)
            self.__updates.data[:] = self.data

    def defer_writes_end(self):
        """Stop deferring the writes to the matrix and apply the recorded writes."""
        if not self.__writes_deferred:
            return
        self.__writes_deferred = False
        # Are updates tracked?
        if self.track_updates:
            # If so, process them individually
            for key,value in self.__updates.iteritems():
                numpy.ndarray.__setitem__(self, key, value)
                self.__colormatrix[key] = self.__colormap.get_color(value)
        else:
            # If not, copy the updated matrix back to the matrix
            self.data[:] = self.__updates.data
            self.__colormatrix_uptodate = False
