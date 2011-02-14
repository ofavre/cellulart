# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk
import gtk.gdkgl

from OpenGL.GL import *
from OpenGL.GLU import *



# Cache the found configuration
__old_glconfig = None

def get_glconfig():
    """Returns a GLConfig to be used for OpenGL widgets initialisation."""
    global __old_glconfig
    if __old_glconfig == None:
        # Query the OpenGL extension version.
        print "OpenGL extension version - %d.%d\n" % gtk.gdkgl.query_version()

        # Configure OpenGL framebuffer.
        # Try to get a double-buffered framebuffer configuration,
        # if not successful then try to get a single-buffered one.
        display_mode = (gtk.gdkgl.MODE_RGB | gtk.gdkgl.MODE_DEPTH | gtk.gdkgl.MODE_DOUBLE)
        try:
            glconfig = gtk.gdkgl.Config(mode=display_mode)
        except gtk.gdkgl.NoMatches:
            display_mode &= ~gtk.gdkgl.MODE_DOUBLE
            glconfig = gtk.gdkgl.Config(mode=display_mode)

        print "is RGBA:",                 glconfig.is_rgba()
        print "is double-buffered:",      glconfig.is_double_buffered()
        print "is stereo:",               glconfig.is_stereo()
        print "has alpha:",               glconfig.has_alpha()
        print "has depth buffer:",        glconfig.has_depth_buffer()
        print "has stencil buffer:",      glconfig.has_stencil_buffer()
        print "has accumulation buffer:", glconfig.has_accum_buffer()
        print

        __old_glconfig = glconfig

    return __old_glconfig
