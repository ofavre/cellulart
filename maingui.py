# -*- coding: utf-8 -*-

import sys

import pygtk
pygtk.require('2.0')
import gtk

from matrixwidget import *
import openglutils
from layerswidget import *



class MainGUI(gtk.Window):
    """ Main GUI showing all the controls to manipulate the simulation.
        Currently, only a test for the MatrixWidget is implemented.
        TODO: Conceive a real GUI, eventually with Glade.
              But make sure every main idea is clearly set before.
    """

    def __init__(self, world):
        gtk.Window.__init__(self)

        self.__world = world

        # Window initialisation
        self.set_title('Cellulart   - - -   By Olivier Favre, Haykel Haddaji, Yassin Patel and Quentin Pradet')
        self.connect('destroy', self.on_destroy)
        self.connect('delete-event', self.on_delete)

        #
        # Components creation
        #

        # Matrix that displays the world
        self.matrix = MatrixWidget(self.__world)
        self.matrix.show()

        # Matrix-layers display control, with scrollbars
        self.scrolledlayers = gtk.ScrolledWindow()
        self.scrolledlayers.set_property("hscrollbar-policy", gtk.POLICY_NEVER)
        self.layers = LayersWidget(self.__world)
        self.layers.show()
        # Listen for display changes, to refresh the display
        self.layers.connect("settings-changed", self.__layers_settings_changed)
        self.scrolledlayers.add(self.layers)
        self.scrolledlayers.show()

        # Step button
        vbox = gtk.VBox()
        self.stepButton = gtk.Button("Step")
        self.stepButton.connect("clicked", self.on_step)
        self.stepButton.show()
        vbox.pack_start(self.stepButton, False, True)
        vbox.pack_start(self.scrolledlayers, True, True)
        vbox.show()

        # Pack everything together
        # Use a resizeable paned split
        box = gtk.HPaned()
        box.pack1(self.matrix, True, False)
        box.pack2(vbox, False, True)
        box.show()
        self.add(box)

        # Special GtkGLExt initialisation stuff
        # May not even be really necessary
        if sys.platform != 'win32':
            # Not to be applied to the window itself, rather to the MatrixWidget's parent (may be the window in that case, yes)
            box.set_resize_mode(gtk.RESIZE_IMMEDIATE)
        # Redraw if the window has been moved
        self.set_reallocate_redraws(True)

    def __layers_settings_changed(self, widget):
        """Fired when some parameter controlling the display changed."""
        # Request a redraw
        self.matrix.queue_draw()

    def on_delete(self, widget, event):
        """Called when the window closes.
        We prefer to destroy it."""
        return False # ask for destroy instead

    def on_destroy(self, widget):
        """Called when the window is destroyed.
        Quit the Gtk main loop."""
        gtk.main_quit()
        return True

    def on_step(self, widget):
        self.__world.step()
        self.matrix.queue_draw()

    def run(self):
        """Shows the window and enters the Gtk main loop until it gets closed."""
        gtk.gdk.threads_init()
        gtk.gdk.threads_enter()
        self.show()
        gtk.main()
        gtk.gdk.threads_leave()
