# -*- coding: utf-8 -*-
# License: See LICENSE file.

import pygtk
pygtk.require('2.0')
import gtk
import gobject

class LayersWidget(gtk.TreeView):
    """Lists all matrices and permits to adjust their display settings."""
    __gsignals__ = {
        # Fired when the MatrixWidget should be refreshed due to a change in the display settings
        "settings-changed": (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, tuple()),
    }
    def __init__(self, world):
        gtk.TreeView.__init__(self)
        self.__world = world

        # Create and populate the model
        self.model = gtk.ListStore(gobject.TYPE_BOOLEAN,gobject.TYPE_STRING,gobject.TYPE_FLOAT)
        for m in self.__world.get_matrices_list():
            self.model.append((m.visible,m.get_name(),m.alpha))
        self.set_model(self.model)
        self.set_reorderable(True)
        self.set_search_column(1)
        # Create the columns
        # Visibility
        cell = gtk.CellRendererToggle()
        cell.set_property('activatable', True)
        cell.connect('toggled', self.__toggled_cb)
        col = gtk.TreeViewColumn("", cell, active=0) # Visible
        self.append_column(col)
        self.visibleCellRenderer = cell
        self.visibleColumn = col
        # Matrix name
        cell = gtk.CellRendererText()
        col = gtk.TreeViewColumn("Matrix", cell, text=1)
        col.set_resizable(True)
        self.append_column(col)
        self.nameCellRenderer = cell
        self.nameColumn = col
        # Alpha
        cell = HSliderCellRenderer()
        cell.set_property('activatable', True)
        cell.connect('value-changed', self.__value_changed_cb)
        col = gtk.TreeViewColumn("Opacity", cell, value=2)
        col.set_resizable(True)
        self.append_column(col)
        self.alphaCellRenderer = cell
        self.alphaColumn = col

        # Register signals
        # Add the rows before registering this signal, or we will be notified of the insertion as changes
        self.model.connect("row-changed", self.__row_changed)
        # Detects properly a drag and drop reorder (sequence: drag begin, row inserted, row deleted, drag end)
        self.connect("drag-begin", self.__potential_reorder_begin)
        self.model.connect("row-deleted", self.__row_deleted)
        self.model.connect("row-inserted", self.__row_inserted)
        self.connect("drag-end", self.__potential_reorder_end)
        # State variables for tracking changes during a drad and drop reorder
        self.__potentially_reordering = False
        self.__potentially_reordering_begin_index = None
        self.__potentially_reordering_end_index = None
        # Tweaks for better interaction with the alpha column
        self.connect("button-press-event", self.__motion_activate_alpha_button_press)
        self.connect("button-release-event", self.__motion_activate_alpha_button_release)
        self.connect("motion-notify-event", self.__motion_activate_alpha)
        self.connect("scroll-event", self.__scroll_update_alpha)
        self.__motion_activate_alpha_goodstartcolumn = False

    #def __print(self, *args): # for debugging purposes
    #    print args

    def __scroll_update_alpha(self, widget, event):
        """The scroll-wheel over the alpha column adds/removes 0.05 to the alpha value."""
        # Get the cell under the pointer
        info = self.get_path_at_pos(int(event.x), int(event.y))
        # Invalid position, ignore
        if info == None: return False
        path, col, x, y = info
        # Make sure the event is on the alpha column, otherwise ignore
        if not (col is self.alphaColumn): return False
        # Update the value
        iter = self.model.get_iter(path)
        self.model.set(iter,2, max(0.0,min(1.0, self.model.get(iter, 2)[0] + 0.05 * (1 if event.direction == gtk.gdk.SCROLL_UP else -1) )))
        return True # event consumed

    def __motion_activate_alpha_button_press(self, widget, event):
        """Tracks a click on the alpha column, to interpret pointer motion only if initiated on that column."""
        # By default, we did not identify the alpha column as the source object for the event
        self.__motion_activate_alpha_goodstartcolumn = False
        # Only left click
        if event.button != 1: return False
        # Get the clicked column
        info = self.get_path_at_pos(int(event.x), int(event.y))
        if info == None: return False
        path, col, x, y = info
        # Make sure it's the alpha column
        if not (col is self.alphaColumn): return False
        # Good, raise the flag so that pointer motion can adjust the alpha values (no spam motion)
        self.__motion_activate_alpha_goodstartcolumn = True
        # Let the event be consumed normally by subsequent signal handlers, so that the activation will happen on the alpha cells
        return False

    def __motion_activate_alpha_button_release(self, widget, event):
        """End of tracking for a pointer motion after a click on the alpha column."""
        self.__motion_activate_alpha_goodstartcolumn = False
        return False

    def __motion_activate_alpha(self, widget, event):
        """ Simulates additional activate events on the alpha cell below the pointer.
            This way the user can drag the cursor fluidly to the desired position instead of repeatedly clicking."""
        # Skip spam clicks (not initiated on the alpha column, or not left click)
        # NOTE: This permits to adjust multiple alpha cells by moving hovering them.
        #       To restrict to the single cell, the path should also be noted.
        #       One can then filter for mouse exits (like buttons), or permit flexibility with regards to the Y axis (like scrollbars).
        if not self.__motion_activate_alpha_goodstartcolumn or (event.get_state() & gtk.gdk.BUTTON1_MASK == 0): return False
        info = self.get_path_at_pos(int(event.x), int(event.y))
        if info == None: return False
        path, col, x, y = info
        if not (col is self.alphaColumn): return False
        # Generate a fake activation event
        self.alphaCellRenderer.activate(event, self, ":".join([str(i) for i in path]), self.get_background_area(path, col), self.get_cell_area(path, col), gtk.CELL_RENDERER_SELECTED)
        # Consume the event
        return True

    def __row_changed(self, treemodel, path, iter):
        """Tracks changes on a row. Updates the display settings in the corresponding matrix, and requests display update."""
        # This event is fired when drag and drop reordering because a new row is inserted. Simply ignore that.
        if self.__potentially_reordering:
            return False
        # Get the corresponding matrix
        m = self.__world.get_matrix(self.model.get(iter, 1)[0])
        # Update all attributes (we don't know which one has been modified)
        m.visible = self.model.get(iter, 0)[0]
        m.alpha = self.model.get(iter, 2)[0]
        # Request display update
        self.emit("settings-changed")

    def __row_inserted(self, treemodel, path, iter):
        """Should only be taken care of when drag and drop reordering. Tracks the destination location."""
        if self.__potentially_reordering:
            self.__potentially_reordering_end_index = path[0]
        return False

    def __row_deleted(self, treemodel, path):
        """Should only be taken care of when drag and drop reordering. Tracks the origin location."""
        if self.__potentially_reordering:
            self.__potentially_reordering_begin_index = path[0]
            return

    def __potential_reorder_begin(self, *args):
        """Start to keep tracks of potential drag and drop reordering."""
        self.__potentially_reordering = True

    def __potential_reorder_end(self, *args):
        """Update the world's matrix list according to the new row order."""
        # Make sure we had a successful and complete drag and drop reorder
        if self.__potentially_reordering and self.__potentially_reordering_begin_index != None and self.__potentially_reordering_end_index != None:
            # Adjust the indices
            if self.__potentially_reordering_begin_index > self.__potentially_reordering_end_index:
                self.__potentially_reordering_begin_index -= 1
            else:
                self.__potentially_reordering_end_index -= 1
            # Set the new index of the moved matrix, the rest will be updated accordingly
            self.__world.get_matrices_list()[self.__potentially_reordering_begin_index].index = self.__potentially_reordering_end_index
            # Request display update
            self.emit("settings-changed")
        # End of tracking
        self.__potentially_reordering = False
        self.__potentially_reordering_begin_index = None
        self.__potentially_reordering_end_index = None
        # Let normal signal handler do their work
        return False

    def __toggled_cb(self, cell, path):
        """Fired when a CellRendererToggle has been toggled. Update the model (the matrices will be updated by the subsequent row-changed signal)."""
        self.model[path][0] = not self.model[path][0]
        return
    def __value_changed_cb(self, cell, path, new_value):
        """Fired when a HSliderCellRenderer has been modified. Update the model (the matrices will be updated by the subsequent row-changed signal)."""
        self.model[path][2] = max(0.0, min(1.0, new_value))
        return

# Register the new GObject so that it's signals work properly
gobject.type_register(LayersWidget)



class HSliderCellRenderer(gtk.GenericCellRenderer, gobject.GObject):
    """Custom CellRenderer that should ideally look like a HSlider, at least like a ProgressBar, a level."""
    __gproperties__ = {
        # The displayed value, the floating point percentage, between 0.0 and 1.0
        'value' : (gobject.TYPE_FLOAT, # type
            'Display value', # nick name
            'The value to be displayed. Should be floating between 0.0 and 1.0.', # description
            0.0, # min value
            1.0, # max value
            0.0, # default value
            gobject.PARAM_READWRITE), # flags
        # Whether or not the cell is activatable (modifiable by a single click, easier than editing)
        'activatable': (gobject.TYPE_BOOLEAN,
            'Activatable cell', # nick name
            'Whether or not the cell responds to a click.', # description
            False, # default value
            gobject.PARAM_READWRITE), # flags
        # The editable way is a bit more complicated to code, and potentially less practical at use, drop it
        #'editable': (gobject.TYPE_BOOLEAN,
        #    'sdf','sdf',False,gobject.PARAM_READWRITE)
    }
    __gsignals__ = {
        # Fired to notify the model (in fact, any listener) that the value has been (in fact, should be) changed.
        "value-changed": (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, (object, float)),
    }

    def __init__(self):
        #gobject.GObject.__init__(self) # which initialization is the best?
        gobject.GObject.__gobject_init__(self)
        gtk.CellRenderer.__init__(self)
        # Initialize properties
        self.value = 0.0
        self.activatable = False
        #self.editable = False

    def do_get_property(self, property):
        """Called by the GObject interface to get the value of a given named property."""
        if property.name == 'value':
            return self.value
        elif property.name == 'activatable':
            return self.activatable
        #elif property.name == 'editable':
        #    return self.editable
        else:
            raise AttributeError, 'unknown property %s' % property.name

    def do_set_property(self, property, value): 
        """Called by the GObject interface to set the value of a given named property."""
        if property.name == 'value':
            self.value = value
        elif property.name == 'activatable':
            self.activatable = value
            if value:
                #self.editable = False
                self.set_property('mode', gtk.CELL_RENDERER_MODE_ACTIVATABLE)
        #elif property.name == 'editable':
        #    self.editable = value
        #    if value:
        #        self.activatable = False
        #        self.set_property('mode', gtk.CELL_RENDERER_MODE_EDITABLE)
        else:
            raise AttributeError, 'unknown property %s' % property.name

    def on_get_size(self, widget, cell_area):
        """Returns the desired size of the render area."""
        if cell_area != None:
            # If given a clue, use it blindly
            return (cell_area.x, cell_area.y, cell_area.width, cell_area.height)
        return (0,0,50,24) # some reasonable value, smaller (particularly in height) will make the cell not to expand, but it will always fill the finally available render area

    def on_render(self, window, widget, background_area, cell_area, expose_area, flags):
        """Called when the drawing should be performed on the given window (gtk.gdk.DrawingArea) on the given area (cell_area intersect expose_area)"""
        # This code is copied/inspired from the CellRendererProgress
        is_rtl = widget.get_direction() == gtk.TEXT_DIR_RTL;
        gc = gtk.gdk.GC(window)
        x = cell_area.x + self.get_property('xpad');
        y = cell_area.y + self.get_property('ypad');

        w = cell_area.width - self.get_property('xpad') * 2;
        h = cell_area.height - self.get_property('ypad') * 2;

        gc.set_rgb_fg_color(widget.get_style().fg[gtk.STATE_NORMAL]);
        window.draw_rectangle(gc, True, x, y, w, h);

        x += widget.get_style().xthickness;
        y += widget.get_style().ythickness;
        w -= widget.get_style().xthickness * 2;
        h -= widget.get_style().ythickness * 2;
        gc.set_rgb_fg_color(widget.get_style().bg[gtk.STATE_NORMAL]);
        window.draw_rectangle(gc, True, x, y, w, h);

        gc.set_rgb_fg_color(widget.get_style().bg[gtk.STATE_SELECTED]);
        perc_w = w * max(0, self.value);
        window.draw_rectangle(gc, True, int(x + w - perc_w) if is_rtl else int(x), int(y), int(perc_w), int(h));

        layout = widget.create_pango_layout("%.1f"%(100*self.value));
        logical_rect = layout.get_pixel_extents()[1];
        logical_rect = gtk.gdk.Rectangle(*logical_rect)

        pos = (w - logical_rect.width)/2;

        clip = gtk.gdk.Rectangle()
        clip.x = x;
        clip.y = y;
        clip.width = w - perc_w if is_rtl else perc_w;
        clip.height = h;

        if window.__class__ is gtk.gdk.Window: #FIXME: Some hack to avoid an error in the console (not disturbing)
            widget.get_style().paint_layout(window,
                gtk.STATE_NORMAL if is_rtl else gtk.STATE_SELECTED,
                False, clip, widget, "progressbar",
                x + pos, y + (h - logical_rect.height)/2,
                layout);

        clip.x = clip.x + clip.width;
        clip.width = w - clip.width;

        if window.__class__ is gtk.gdk.Window: #FIXME: Some hack to avoid an error in the console (not disturbing)
            widget.get_style().paint_layout(window,
                gtk.STATE_SELECTED if is_rtl else gtk.STATE_NORMAL,
                False, clip, widget, "progressbar",
                x + pos, y + (h - logical_rect.height)/2,
                layout);

    def on_activate(self, event, widget, path, background_area, cell_area, flags):
        """Called when the cell has been clicked. Change the value so that the users selected a percentage to display."""
        if event == None: return False # Hack for a situation caused when pressing Space or Enter while keyboard navigation on the displayed cells. (We need a pointer position, unlike CellRendererToggle).
        value = max(0.0,min(1.0, (event.x - cell_area.x)/cell_area.width ))
        # Notify the model (in fact, any listener) that our value should be changed
        self.emit('value-changed', path, value)
        return True

    #def on_start_editing(self, event, widget, path, background_area, cell_area, flags):
    #    pass

# Register the new GObject so that it's signals work properly
gobject.type_register(HSliderCellRenderer)
