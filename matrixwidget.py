# -*- coding: utf-8 -*-

import random
import math

import pygtk
pygtk.require('2.0')
import gtk
import gtk.gtkgl
import gtk.gtkgl.apputils

from OpenGL.GL import *
from OpenGL.GLU import *

import openglutils

class MatrixWidget(gtk.DrawingArea, gtk.gtkgl.Widget):
    """OpenGL widget drawing the view of the matrices of the world."""
    default_max_width  = 1024
    default_max_height = 768
    default_min_width  = 200
    default_min_height = 150

    def __init__(self, world, pointsize=None, offset=None):
        gtk.DrawingArea.__init__(self)
        #gtk.gtkgl.Widget.__init__(self) # (abstract class)

        # Object initialisation
        self.__world = world
        self.__original_pointsize = pointsize
        self.__pointsize_power = 0
        self.__pointsize_power_min = -50
        self.__pointsize_power_max = +50
        self.__pointsize_factor = 1.1
        self.__pointsize = pointsize # self.__original_pointsize * self.__pointsize_factor ** self.__pointsize_power
        self.offset = list(offset) if not offset == None else None
        self.__is_panning = None
        self.__needs_reconfigure = False

        # Widget initialisation
        # If no pointsize is given, find a good one
        if self.__original_pointsize == None:
            self.__original_pointsize = 1
            w = self.default_max_width  / float(world.get_shape()[1])
            h = self.default_max_height / float(world.get_shape()[0])
            pw = math.log(w) / math.log(self.__pointsize_factor)
            ph = math.log(h) / math.log(self.__pointsize_factor)
            if pw > 0: pw = int(math.ceil(pw))
            else: pw = int(math.floor(pw))
            if ph > 0: ph = int(math.ceil(ph))
            else: ph = int(math.floor(ph))
            self.__pointsize_power = max(self.__pointsize_power_min, min(self.__pointsize_power_max, min(pw,ph)))
            self.__pointsize = self.__original_pointsize * self.__pointsize_factor ** self.__pointsize_power
        # Request a default size
        reqw, reqh = int(math.ceil(max(self.default_min_width,min(self.default_max_width,world.get_shape()[1]*self.__pointsize)))), int(math.ceil(max(self.default_min_height,min(self.default_max_height,world.get_shape()[0]*self.__pointsize))))
        self.set_size_request(reqw, reqh)
        # Calculate an offset to center the matrices, assuming the default size is the actual size
        if self.offset == None:
            mw = reqw/self.__pointsize - world.get_shape()[1]
            mh = reqh/self.__pointsize - world.get_shape()[0]
            self.offset = [-mh/2, -mw/2]
        # Set OpenGL-capability to the drawing area
        self.set_gl_capability(openglutils.get_glconfig(), share_list=None, direct=True, render_type=gtk.gdkgl.RGBA_TYPE)

        # Connect the relevant signals for the drawing
        self.connect_after('realize',   self.__on_realize)
        self.connect('configure-event', self.__on_configure_event)
        self.connect('expose-event',    self.__on_expose_event)
        # Connect additionnal events for the manipulation of the view
        self.set_events(gtk.gdk.ALL_EVENTS_MASK)
        self.connect('scroll-event',    self.__on_scroll)
        self.connect('motion-notify-event', self.__on_motion_notify)
        self.connect('button-press-event',  self.__on_button_press)
        self.connect('button-release-event',  self.__on_button_release)

    def get_pointsize(self):
        """ Returns the size of a cell, in pixels."""
        return self.__pointsize
    def set_pointsize(self,pointsize):
        """ Sets the size of a cell, in pixels.
        Requests a redraw."""
        self.__pointsize = pointsize
        self.queue_redraw(True)

    def queue_redraw(self,needs_reconfigure=False):
        """ Requests a redraw of the widget.
            needs_reconfigure: set to True if the offset or the point size has changed."""
        self.__needs_reconfigure = needs_reconfigure
        self.queue_draw()

    def __on_scroll(self, widget, event):
        """Handles the mousewheel events and zooms the view accordingly."""
        # Pan to get the origin at the mouse position's point
        self.offset[0] += (widget.get_allocation().height-event.y) / self.__pointsize
        self.offset[1] += event.x / self.__pointsize
        # Zoom
        if event.direction == gtk.gdk.SCROLL_UP:
            self.__pointsize_power = min(self.__pointsize_power_max, self.__pointsize_power+1)
        elif event.direction == gtk.gdk.SCROLL_DOWN:
            self.__pointsize_power = max(self.__pointsize_power_min, self.__pointsize_power-1)
        self.__pointsize = self.__original_pointsize * self.__pointsize_factor ** self.__pointsize_power
        # Pan back to get the mouse position's point back under the pointer on the screen
        self.offset[0] -= (widget.get_allocation().height-event.y) / self.__pointsize
        self.offset[1] -= event.x / self.__pointsize
        self.queue_redraw(True)

    def __on_button_press(self, widget, event):
        """Handles a button press and starts a panning operation."""
        self.__is_panning = (event.y, event.x)
        self.queue_redraw(True)

    def __on_motion_notify(self, widget, event):
        """Handles the pointer motion and pans accordingly if in a panning operation."""
        if self.__is_panning != None:
            self.offset[0] += (event.y - self.__is_panning[0]) / self.__pointsize
            self.offset[1] -= (event.x - self.__is_panning[1]) / self.__pointsize
            self.__is_panning = (event.y, event.x)
            self.queue_redraw(True)

    def __on_button_release(self, widget, event):
        """Handles a button release and stops a panning operation."""
        self.__is_panning = None

    def __on_realize(self, *args):
        """A one time widget setup. Initialises the OpenGL drawable."""
        gldrawable = self.get_gl_drawable()
        glcontext = self.get_gl_context()
        if not gldrawable.gl_begin(glcontext):
            return

        # Generate (one) texture #TODO: Test if one texture by matrix is better
        self.iTex = glGenTextures(1)
        # Configure use of textures
        glEnable(GL_TEXTURE_2D)
        glDisable(GL_TEXTURE_GEN_S)
        glDisable(GL_TEXTURE_GEN_T)
        glBindTexture(GL_TEXTURE_2D, self.iTex)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)

        # As we're in 2D, we don't need any depth test
        glDisable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        # Set opaque black as background color
        glClearColor(0.0, 0.0, 0.0, 1.0)
        # Refresh the view configuration
        self.__reconfigure()

        gldrawable.gl_end()
        return True

    def __on_configure_event(self, *args):
        """Called whenever the widget changes in size. Refreshes the view configuration."""
        gldrawable = self.get_gl_drawable()
        glcontext = self.get_gl_context()
        if not gldrawable.gl_begin(glcontext):
            return False

        # Refresh the view configuration
        self.__reconfigure()

        gldrawable.gl_end()
        return True

    def __reconfigure(self):
        """Configures the view origin, size and viewport.
        To be called inside gl_begin() and gl_end()."""
        # Get the widget's size
        width, height = self.allocation.width, self.allocation.height
        # Tell OpenGL to draw onto the same size
        glViewport(0, 0, width, height)
        # Set the view origin and extent
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(self.offset[1]+0.0, self.offset[1]+width/float(self.__pointsize), self.offset[0]+0.0, self.offset[0]+height/float(self.__pointsize), -1.0, 1.0)
        # Reset any 3D transform
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def __on_expose_event(self, *args):
        gldrawable = self.get_gl_drawable()
        glcontext = self.get_gl_context()
        if not gldrawable.gl_begin(glcontext):
            return False

        # Do differed view configuration updates, now that we are in a drawing context
        if self.__needs_reconfigure:
            self.__reconfigure()
            self.__needs_reconfigure = False

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT) #(and depth buffer, when we'll need it) | GL_DEPTH_BUFFER_BIT)

        self.__world.lock_for_drawing()
        # Draw every matrix
        for m in reversed(self.__world.get_matrices_list()): # paint back to front #TODO: Filter for obstructed matrices by an opaque one
            # Skip invisible matrices
            if m.visible != True:
                continue
            pixels = m.get_pixels()

            # Draw every cell
            # (fast) Moderately good texture way (glTexSubImage2D should be used)
            glColor4f(1,1,1,m.alpha) # custom alpha is really simple!
            glTexImage2Dub(GL_TEXTURE_2D, 0, GL_RGBA, 0, GL_RGBA, pixels)
            #glTexSubImage2Dub(GL_TEXTURE_2D, 0, 0, 0, GL_RGBA, pixels) # only if glTexImage2D has already initialised the texture
            glBegin(GL_QUADS)
            glTexCoord2i(0, 0)
            glVertex2i(0, 0)
            glTexCoord2i(1, 0)
            glVertex2i(0, m.shape[0])
            glTexCoord2i(1, 1)
            glVertex2i(m.shape[1], m.shape[0])
            glTexCoord2i(0, 1)
            glVertex2i(m.shape[1], 0)
            glEnd()
            #glDisable(GL_TEXTURE_2D)
            #glBindTexture(GL_TEXTURE_2D, 0)
        self.__world.unlock_for_drawing()

        # Display the drawing
        if gldrawable.is_double_buffered():
            gldrawable.swap_buffers()
        else:
            glFlush()

        # OpenGL end
        gldrawable.gl_end()
        return True
