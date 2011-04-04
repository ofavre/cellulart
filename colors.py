# -*- coding: utf-8 -*-
# License: See LICENSE file.

import numpy



class Colormap(object):
    """ Base class, and dummy implementation, of a colormap.
        A colormap is responsible for converting a value to a quadruple of colors"""

    def __init__(self):
        pass

    def get_color(self, value):
        """Returns a 4-tuple of values between 0 and 255 representing the RGBA color associated with the given value."""
        raise NotImplemented()

    def convert_matrix(self, matrix, colormatrix):
        """ Converts each value of the matrix to the corresponding color inside the colormatrix.
            The default implementation calls get_color on every item of the matrices"""
        for y in xrange(matrix.shape[0]):
            for x in xrange(matrix.shape[1]):
                colormatrix[y,x] = self.get_color(matrix.flat[y,x])

    def is_opaque(self):
        """ Returns whether or not this colormap can generate translucent pixels.
            This information is used to speed up the drawing process by ignoring
            shown matrices under a fully opaque one."""
        return False



class LinearGradientColormap(Colormap):
    """ A basic RGBA gradient with two colors, for numerical values.
        The output is a linear gradient (component by component, in RGBA) between
        two colors, each attached to a bound value."""

    def __init__(self, value_min=0, value_max=1, color_min=(0,0,0,255), color_max=(255,255,255,255)):
        """ value_min: The lower bound of the values to be converted to colors.
            value_max: The upper bound of the values to be converted to colors.
            color_min: The color corresponding to the lower bound, a 4-tuple of RGBA components.
            color_max: The color corresponding to the upper bound, a 4-tuple of RGBA components."""
        Colormap.__init__(self)
        self.value_min = value_min
        self.color_min = color_min
        self.value_max = value_max
        self.color_max = color_max

    def get_color(self, value):
        v = ( max(self.value_min, min(self.value_max, value)) - self.value_min ) / (self.value_max - self.value_min)
        return (
            int(v*self.color_max[0]+(1-v)*self.color_min[0]),
            int(v*self.color_max[1]+(1-v)*self.color_min[1]),
            int(v*self.color_max[2]+(1-v)*self.color_min[2]),
            int(v*self.color_max[3]+(1-v)*self.color_min[3])
        )

    def convert_matrix(self, matrix, colormatrix):
        # Using NumpPy's ufunc is much faster than iterating over each cell, but also a bit more complicated
        tmp = numpy.subtract(matrix, self.value_min)
        numpy.divide(tmp, self.value_max-self.value_min, tmp)
        numpy.minimum(tmp, 1.0, tmp)
        numpy.maximum(tmp, 0.0, tmp)
        tmp2 = numpy.multiply.outer(tmp, self.color_max)
        numpy.negative(tmp, tmp)
        numpy.add(tmp, 1, tmp)
        tmp3 = numpy.multiply.outer(tmp, self.color_min)
        numpy.add(tmp2, tmp3, colormatrix)

    def is_opaque(self):
        return self.color_min[3] == 255 and self.color_max[3] == 255



class BinaryBooleanColormap(Colormap):
    """ A basic RGBA colormap with two colors, for boolean values."""

    def __init__(self, color_false=(0,0,0,255), color_true=(255,255,255,255)):
        """ color_false: The color corresponding to the False value, a 4-tuple of RGBA components.
            color_true:  The color corresponding to the True value, a 4-tuple of RGBA components."""
        Colormap.__init__(self)
        self.color_false = color_false
        self.color_true  = color_true

    def get_color(self, value):
        if value == True:
            return self.color_true
        else:
            return self.color_false

    def convert_matrix(self, matrix, colormatrix):
        choice = numpy.matrix((self.color_false, self.color_true), dtype=numpy.uint8)
        # Better way (no intermediate storage), but raising "shape mismatch: objects cannot be broadcast to a single shape"
        #matrix.reshape((matrix.shape[0], matrix.shape[1], 1)).choose((choice[0], choice[1]), colormatrix)
        colormatrix.data[:] = numpy.where(matrix.reshape((matrix.shape[0], matrix.shape[1], 1)), choice[1], choice[0]).data

    def is_opaque(self):
        return self.color_false[3] == 255 and self.color_true[3] == 255



class CopyColormap(Colormap):
    """ A basic colormap that can only work with a special input matrix,
        formed by the dtype "(4,)uint8" (or equivalent), that simply "copies" the values
        as they should already form RGBA colors.
        Remark: It actually replaces colormatrix's data pointer by the original matrix's data pointer,
                this way no copy is needed, but we may loose a bit of memory and loose any chance to undo the operation."""

    def __init__(self):
        Colormap.__init__(self)

    def get_color(self, value):
        return value

    def convert_matrix(self, matrix, colormatrix):
        # No need to perform a real copy, simply replace the memory pointers!
        colormatrix.data[:] = matrix.data

    def is_opaque(self):
        return False # cannot tell True for sure, so say False
