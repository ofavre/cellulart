# -*- coding: utf-8 -*-

import sys

import pygtk
pygtk.require('2.0')
import gtk

from matrixwidget import *
import openglutils



class MainGUI(gtk.Window):
    """ Main GUI showing all the controls to manipulate the simulation.
        Currently, only a test for the MatrixWidget is implemented.
        TODO: Conceive a real GUI, eventually with Glade.
              But make sure every main idea is clearly set before.
        TODO: Have a Gimp-like layer control where each matrix has:
               - an ordered position, for drawing order
               - a in/visible toggle button
               - an alpha slider
    """

    def __init__(self, world):
        gtk.Window.__init__(self)

        self.__world = world

        # Special GtkGLExt initialisation stuff
        if sys.platform != 'win32':
            self.set_resize_mode(gtk.RESIZE_IMMEDIATE)
        self.set_reallocate_redraws(True)

        # Window initialisation
        self.set_title('Cellulart   - - -   By Olivier Favre, Haykel Haddaji, Yassin Patel and Quentin Pradet')
        self.connect('destroy', self.on_destroy)
        self.connect('delete-event', self.on_delete)

        #
        # Components creation
        #

        # Matrix that displays the world
        matrix = MatrixWidget(self.__world, 1)
        matrix.show()

        # Pack everything together
        box = gtk.HBox()
        box.pack_start(matrix)
        box.show()
        self.add(box)

    def on_delete(self, widget, event):
        """Called when the window closes.
        We prefer to destroy it."""
        return False # ask for destroy instead

    def on_destroy(self, widget):
        """Called when the window is destroyed.
        Quit the Gtk main loop."""
        gtk.main_quit()
        return True

    def run(self):
        """Shows the window and enters the Gtk main loop until it gets closed."""
        gtk.gdk.threads_init()
        gtk.gdk.threads_enter()
        self.show()
        gtk.main()
        gtk.gdk.threads_leave()
