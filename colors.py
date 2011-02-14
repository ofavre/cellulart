# -*- coding: utf-8 -*-



class Colormap(object):
    """ Base class, and dummy implementation, of a colormap.
        A colormap is responsible for converting a value to a quadruple of colors"""

    def __init__(self):
        pass

    def __call__(self, value):
        """Returns a fully transparent black color."""
        return (0, 0, 0, 0)

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
        self.min = value_min
        self.color_min = color_min
        self.max = value_max
        self.color_max = color_max

    def __call__(self, value):
        v = ( max(self.min, min(self.max, value)) - self.min ) / (self.max - self.min)
        return (
            int(v*self.color_max[0]+(1-v)*self.color_min[0]),
            int(v*self.color_max[1]+(1-v)*self.color_min[1]),
            int(v*self.color_max[2]+(1-v)*self.color_min[2]),
            int(v*self.color_max[3]+(1-v)*self.color_min[3])
        )

    def is_opaque(self):
        return self.color_min[3] == 255 and self.color_max[3] == 255
