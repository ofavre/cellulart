# -*- coding: utf-8 -*-

import sys
import threading

import pygtk
pygtk.require('2.0')
import gtk
import gobject

from matrixwidget import *
import openglutils
from layerswidget import *



class MainGUI(gtk.Window):
    """ Main GUI showing all the controls to manipulate the simulation.
        Currently, only a test for the MatrixWidget is implemented.
        TODO: Conceive a real GUI, eventually with Glade.
              But make sure every main idea is clearly set before.
    """

    # Constants for display mode (self.__timer_mode)
    SECONDS_BETWEEN_FRAMES = 0 # wait between frames : calculate a new frame, wait, draw, loop
    FULL_SPEED = 1             # no wait, display all frames : calculate a new frame, draw, loop
    FRAMES_EVERY_SECONDS = 2   # display a frame regularly : calculate new frames in background, in parallel wait then draw and loop

    def __init__(self, world):
        gtk.Window.__init__(self)

        self.__world = world

        # Timer for frame calculation and drawing initialisation
        self.__timer_running = False
        self.__timer_stopEvent = threading.Event()
        self.__timer_drawEvent = threading.Event()
        self.__timer_interval = 0.0 # in seconds, ms accuracy. Display modes: 0 is full speed, positive is seconds between frames and negative is frames every seconds
        self.__timer_mode = self.SECONDS_BETWEEN_FRAMES if self.__timer_interval > 0 else self.FULL_SPEED if self.__timer_interval == 0 else self.FRAMES_EVERY_SECONDS
        self.__timer_interval = abs(self.__timer_interval)

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

        # Control buttons
        controlsBox = gtk.HBox()
        # Play button
        self.playButton = gtk.Button()
        img = gtk.Image()
        img.set_from_file("media-play.png")
        self.playButton.set_image(img)
        self.playButton.connect("clicked", self.on_play)
        self.playButton.show()
        # Pause/Step button
        self.pauseStepButton = gtk.Button()
        img = gtk.Image()
        img.set_from_file("media-pause-step.png")
        self.pauseStepButton.set_image(img)
        self.pauseStepButton.connect("clicked", self.on_pauseStep)
        self.pauseStepButton.show()
        # Timing spinner
        self.speedSpin = DualSpinner(value=abs(int(self.__timer_interval*1000)), limit=10000, increment=10, page_increment=100, up_label="ms/frame", down_label="frame every ms", middle_label="(full speed)", initial_position=DualSpinner.UP if self.__timer_mode == self.SECONDS_BETWEEN_FRAMES else DualSpinner.MIDDLE if self.__timer_mode == self.FULL_SPEED else DualSpinner.DOWN)
        self.speedSpin.connect("value-changed", self.on_speed_value_changed)
        self.speedSpin.connect("position-changed", self.on_speed_position_changed)
        self.speedSpin.show()
        # Pack it up together
        controlsBox.pack_start(self.playButton, False, False)
        controlsBox.pack_start(self.pauseStepButton, False, False)
        controlsBox.pack_start(self.speedSpin, False, True)
        controlsBox.show()

        # Right pane
        vbox = gtk.VBox()
        vbox.pack_start(controlsBox, False, True)
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
        # Stop any timer
        self.__timer_stopEvent.set()
        # Block the world and for it to be free
        self.__world.teardown(wait=True)
        return False # ask for destroy instead

    def on_destroy(self, widget):
        """Called when the window is destroyed.
        Quit the Gtk main loop."""
        gtk.main_quit()
        return True

    def on_speed_value_changed(self, widget, value):
        """Update the timer interval value, in seconds."""
        self.__timer_interval = value/1000.0

    def on_speed_position_changed(self, widget, position):
        """Update the timer mode, and restart running timers (re-applies parameters if timer mode has changed)."""
        old_mode = self.__timer_mode
        if position == DualSpinner.UP:
            self.__timer_mode = self.SECONDS_BETWEEN_FRAMES
        elif position == DualSpinner.DOWN:
            self.__timer_mode = self.FRAMES_EVERY_SECONDS
        elif position == DualSpinner.MIDDLE:
            self.__timer_mode = self.FULL_SPEED
        if self.__timer_running and old_mode != self.__timer_mode:
            self.on_play()

    def on_play(self, widget=None):
        """Sets up timers according to new configuration."""
        # No attempt is made to kill already running threads
        self.__timer_running = True
        # Clean the events
        self.__timer_stopEvent.clear()
        self.__timer_drawEvent.clear()
        # Start the right threads according to timer mode
        if self.__timer_mode == self.SECONDS_BETWEEN_FRAMES:
            th = threading.Thread(target=self.play_interval)
            th.daemon = True
            th.start()
        elif self.__timer_mode == self.FRAMES_EVERY_SECONDS:
            th = threading.Thread(target=self.draw_interval)
            th.daemon = True
            th.start()
            th = threading.Thread(target=self.play_continuously)
            th.daemon = True
            th.start()
        elif self.__timer_mode == self.FULL_SPEED:
            th = threading.Thread(target=self.play_and_draw_continuously)
            th.daemon = True
            th.start()

    def play_interval(self):
        """Waits between each frame calculation and drawing."""
        while not self.__timer_stopEvent.isSet():
            if self.__timer_mode != self.SECONDS_BETWEEN_FRAMES:
                break
            self.__timer_stopEvent.wait(self.__timer_interval)
            if self.__timer_stopEvent.isSet():
                break
            self.step_and_draw()

    def play_continuously(self):
        """Calculates frames continuously, when the drawing event is set, draw the last frame."""
        while not self.__timer_stopEvent.isSet():
            if self.__timer_mode != self.FRAMES_EVERY_SECONDS:
                break
            self.step()
            if self.__timer_drawEvent.isSet():
                self.draw()
                self.__timer_drawEvent.clear()
    def draw_interval(self):
        """Sets the draw event at regular intervals. Works along with play_continuously()."""
        while not self.__timer_stopEvent.isSet():
            if self.__timer_mode != self.FRAMES_EVERY_SECONDS:
                break
            self.__timer_stopEvent.wait(self.__timer_interval)
            if self.__timer_stopEvent.isSet():
                break
            self.__timer_drawEvent.set()

    def play_and_draw_continuously(self):
        """Calculates frames continuously, and draws each of them."""
        while not self.__timer_stopEvent.isSet():
            if self.__timer_mode != self.FULL_SPEED:
                break
            self.step_and_draw()

    def on_pauseStep(self, widget):
        """Stops the running timers, or calculates one step if none is running."""
        if self.__timer_running:
            self.__timer_running = False
            if self.__timer_stopEvent != None:
                self.__timer_stopEvent.set()
        else:
            self.step_and_draw()

    def step(self):
        """Calculates a frame."""
        self.__world.step()
    def draw(self):
        """Draws a frame."""
        self.__world.wait_for_drawing_to_be_done()
        self.matrix.queue_redraw()
    def step_and_draw(self):
        """Calculates and draws a frame."""
        self.__world.step()
        self.__world.wait_for_drawing_to_be_done()
        self.matrix.queue_redraw()

    def run(self):
        """Shows the window and enters the Gtk main loop until it gets closed."""
        gtk.gdk.threads_init()
        gtk.gdk.threads_enter()
        self.show()
        gtk.main()
        gtk.gdk.threads_leave()



class DualSpinner(gtk.HBox):
    """ A special gtk.SpinButton with three modes.
        It has one maximum value, and can pass from one mode to the other by spinning down to the negatives.
        No negative value is actually permitted (in this implementation), rather the spinner changes modes and makes values increase again.
        This way you can continue to scroll/spin the values in the same direction to go down to 0 and go up to the desired value in the other mode.
        One mode is for the "positives", one for the "negatives", and one last is for the 0 value. Modes are also called positions (like a switch's position).
        The spinner is actually a gtk.HBox that contains a gtk.Label along the gtk.SpinButon used to display the current mode."""
    # Positions constants
    UP = 1     # "positives" mode
    MIDDLE = 0 # middle, "0" mode
    DOWN = -1  # "negatives" mode
    # Signals for value and position restitution
    __gsignals__ = {
        "value-changed": (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, (int,)),
        "position-changed": (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, (int,))
    }

    def __init__(self, value=0, limit=100, increment=1, page_increment=10, up_label="up", down_label="down", middle_label="middle", initial_position=MIDDLE):
        """ Creates a DualSpinner, see .__class__.__doc__.
            value:              The start value
            limit:              The maximum value allowed (for "positives" and "negatives" modes)
            increment:          The default increment
            page_increment:     The large increment
            up_label:           The label for the "positives" modes
            down_label:         The label for the "negatives" modes
            middle_label:       The label for the "0" modes
            initial_position:   The initial mode"""
        # The spinner works with a gtk.Adjustment that ranges from -limit to limit (even though only negative values are allowed, so that we can detect when it changes modes).
        # We can also use a negative increment to reverse the direction of scroll/spin to use the same direction for decreasing the values for "positives" mode and increaseing the values inside "negatives" mode.
        self.__position = (DualSpinner.DOWN if initial_position < 0 else DualSpinner.UP if initial_position > 0 else DualSpinner.MIDDLE)
        self.__adj = gtk.Adjustment(value=value, lower=-limit, upper=limit, step_incr=(-increment if initial_position < 0 else increment), page_incr=page_increment, page_size=0)
        self.__spin = gtk.SpinButton(self.__adj)
        self.__spin.connect("value-changed", self.__on_value_changed)
        self.__spin.show()
        self.__up_label = up_label
        self.__middle_label = middle_label
        self.__down_label = down_label
        # A label doesn't receive any events, we have to use a EventBox
        self.__eventbox = gtk.EventBox()
        self.__eventbox.connect("button-press-event", self.__on_double_click_label)
        self.__eventbox.show()
        self.__label = gtk.Label(down_label if initial_position < 0 else middle_label if initial_position == 0 else up_label)
        self.__label.show()
        self.__eventbox.add(self.__label)
        gtk.HBox.__init__(self)
        self.pack_start(self.__spin, False, False)
        self.pack_start(self.__eventbox, False, True)

    def __on_value_changed(self, widget):
        """Handles the change of value and eventually change the position, adjustment's direction and sign of the value."""
        # 0 mode
        if widget.get_value() == 0:
            self.__label.set_text(self.__middle_label)
            self.__position = DualSpinner.MIDDLE
            self.emit("position-changed", DualSpinner.MIDDLE)
        # (Eventual) Change of mode: getting negative, or reincreasing from 0
        elif widget.get_value() < 0 or (self.__position == DualSpinner.MIDDLE and widget.get_value() > 0):
            widget.set_value(abs(widget.get_value()))
            # Detect the mode from the adjustement's increment sign
            if self.__adj.get_step_increment() < 0:
                self.__adj.set_step_increment(-self.__adj.get_step_increment())
                self.__label.set_text(self.__up_label)
                self.__position = DualSpinner.UP
                self.emit("position-changed", DualSpinner.UP)
            elif self.__adj.get_step_increment() > 0:
                self.__adj.set_step_increment(-self.__adj.get_step_increment())
                self.__label.set_text(self.__down_label)
                self.__position = DualSpinner.DOWN
                self.emit("position-changed", DualSpinner.DOWN)
        # Transmit the value-changed event
        self.emit("value-changed", widget.get_value())

    def __on_double_click_label(self, widget, event):
        """Handles a double-click on the label to switch position between "positives" and "negatives"."""
        if event.type == gtk.gdk._2BUTTON_PRESS:
            self.__adj.set_step_increment(-self.__adj.get_step_increment())
            if self.__position == DualSpinner.UP:
                self.__label.set_text(self.__down_label)
                self.check_resize()
                self.__position = DualSpinner.DOWN
                self.emit("position-changed", DualSpinner.DOWN)
            elif self.__position == DualSpinner.DOWN:
                self.__label.set_text(self.__up_label)
                self.check_resize()
                self.__position = DualSpinner.UP
                self.emit("position-changed", DualSpinner.UP)

# Register the new GObject so that it's signals work properly
gobject.type_register(DualSpinner)
