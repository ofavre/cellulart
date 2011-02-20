# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk
import gobject

class LayersWidget(gtk.TreeView):
    __gsignals__ = {
        "settings-changed": (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, tuple()),
    }
    def __init__(self, world):
        gtk.TreeView.__init__(self)
        self.__world = world
        self.model = gtk.ListStore(gobject.TYPE_BOOLEAN,gobject.TYPE_STRING,gobject.TYPE_FLOAT)
        for m in self.__world.get_matrices():
            self.model.append((m.visible,m.get_name(),m.alpha))
        self.model.connect("row-changed", self.__row_changed) # Add the rows before registering this signal, or we will be notified of the insertion as changes
        self.model.connect("row-deleted", self.__row_deleted)
        self.model.connect("row-inserted", self.__row_inserted)
        self.connect("drag-begin", self.__potential_reorder_begin)
        self.connect("drag-end", self.__potential_reorder_end)
        self.__potentially_reordering = False
        self.__potentially_reordering_begin_index = None
        self.__potentially_reordering_end_index = None
        self.set_model(self.model)
        self.set_reorderable(True)
        cell = gtk.CellRendererToggle()
        cell.set_property('activatable', True)
        cell.connect('toggled', self.__toggled_cb)
        col = gtk.TreeViewColumn("", cell, active=0) # Visible
        self.append_column(col)
        self.visibleCellRenderer = cell
        self.visibleColumn = col
        cell = gtk.CellRendererText()
        col = gtk.TreeViewColumn("Matrix", cell, text=1)
        col.set_resizable(True)
        self.append_column(col)
        self.nameCellRenderer = cell
        self.nameColumn = col
        cell = HSliderCellRenderer()
        cell.set_property('activatable', True)
        cell.connect('value-changed', self.__value_changed_cb)
        col = gtk.TreeViewColumn("Opacity", cell, value=2)
        col.set_resizable(True)
        self.append_column(col)
        self.alphaCellRenderer = cell
        self.alphaColumn = col
        self.set_search_column(1)
        self.__motion_activate_alpha_goodstartcolumn = False
        self.connect("button-press-event", self.__motion_activate_alpha_button_press)
        self.connect("button-release-event", self.__motion_activate_alpha_button_release)
        self.connect("motion-notify-event", self.__motion_activate_alpha)
        self.connect("scroll-event", self.__scroll_update_alpha)
    #def __print(self, *args): # for debugging purposes
    #    print args
    def __scroll_update_alpha(self, widget, event):
        info = self.get_path_at_pos(int(event.x), int(event.y))
        if info == None: return False
        path, col, x, y = info
        if not (col is self.alphaColumn): return False
        iter = self.model.get_iter(path)
        self.model.set(iter,2, max(0.0,min(1.0, self.model.get(iter, 2)[0] + 0.05 * (1 if event.direction == gtk.gdk.SCROLL_UP else -1) )))
        return True
    def __motion_activate_alpha_button_press(self, widget, event):
        self.__motion_activate_alpha_goodstartcolumn = False
        if event.button != 1: return False
        info = self.get_path_at_pos(int(event.x), int(event.y))
        if info == None: return False
        path, col, x, y = info
        if not (col is self.alphaColumn): return False
        self.__motion_activate_alpha_goodstartcolumn = True
        return False
    def __motion_activate_alpha_button_release(self, widget, event):
        self.__motion_activate_alpha_goodstartcolumn = False
        return False
    def __motion_activate_alpha(self, widget, event):
        if not self.__motion_activate_alpha_goodstartcolumn or (event.get_state() & gtk.gdk.BUTTON1_MASK == 0): return False
        info = self.get_path_at_pos(int(event.x), int(event.y))
        if info == None: return False
        path, col, x, y = info
        if not (col is self.alphaColumn): return False
        self.alphaCellRenderer.activate(event, self, ":".join([str(i) for i in path]), self.get_background_area(path, col), self.get_cell_area(path, col), gtk.CELL_RENDERER_SELECTED)
        return True
    def __row_changed(self, treemodel, path, iter):
        if self.__potentially_reordering:
            return
        m = self.__world.get_matrix(self.model.get(iter, 1)[0])
        m.visible = self.model.get(iter, 0)[0]
        m.alpha = self.model.get(iter, 2)[0]
        self.emit("settings-changed")
    def __row_inserted(self, treemodel, path, iter):
        if self.__potentially_reordering:
            self.__potentially_reordering_end_index = path[0]
            return
    def __row_deleted(self, treemodel, path):
        if self.__potentially_reordering:
            self.__potentially_reordering_begin_index = path[0]
            return
    def __potential_reorder_begin(self, *args):
        self.__potentially_reordering = True
    def __potential_reorder_end(self, *args):
        if self.__potentially_reordering and self.__potentially_reordering_begin_index != None and self.__potentially_reordering_end_index != None:
            if self.__potentially_reordering_begin_index > self.__potentially_reordering_end_index:
                self.__potentially_reordering_begin_index -= 1
            else:
                self.__potentially_reordering_end_index -= 1
            self.__world.get_matrices()[self.__potentially_reordering_begin_index].index = self.__potentially_reordering_end_index
            self.emit("settings-changed")
        self.__potentially_reordering = False
        self.__potentially_reordering_begin_index = None
        self.__potentially_reordering_end_index = None
    def __toggled_cb(self, cell, path):
        self.model[path][0] = not self.model[path][0]
        return
    def __value_changed_cb(self, cell, path, new_value):
        self.model[path][2] = new_value
        return
gobject.type_register(LayersWidget)

class HSliderCellRenderer(gtk.GenericCellRenderer, gobject.GObject):
    __gproperties__ = {
        'value' : (gobject.TYPE_FLOAT, # type
            'Display value', # nick name
            'The value to be displayed. Should be floating between 0.0 and 1.0.', # description
            0.0, # min value
            1.0, # max value
            0.0, # default value
            gobject.PARAM_READWRITE), # flags
        'activatable': (gobject.TYPE_BOOLEAN,
            'Activatable cell', # nick name
            'Whether or not the cell responds to a click.', # description
            False, # default value
            gobject.PARAM_READWRITE), # flags
        #'editable': (gobject.TYPE_BOOLEAN,
        #    'sdf','sdf',False,gobject.PARAM_READWRITE)
    }
    __gsignals__ = {
        "value-changed": (gobject.SIGNAL_RUN_FIRST, gobject.TYPE_NONE, (object, float)),
    }
    def __init__(self):
        #gobject.GObject.__init__(self)
        gobject.GObject.__gobject_init__(self)
        gtk.CellRenderer.__init__(self)
        self.value = 0.0
        self.activatable = False
        #self.editable = False
    def do_get_property(self, property): 
        if property.name == 'value':
            return self.value
        elif property.name == 'activatable':
            return self.activatable
        #elif property.name == 'editable':
        #    return self.editable
        else:
            raise AttributeError, 'unknown property %s' % property.name
    def do_set_property(self, property, value): 
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
        if cell_area != None:
            return (cell_area.x, cell_area.y, cell_area.width, cell_area.height)
        return (0,0,1,1)
    def on_render(self, window, widget, background_area, cell_area, expose_area, flags):
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

        if window.__class__ is gtk.gdk.Window:
            widget.get_style().paint_layout(window,
                gtk.STATE_NORMAL if is_rtl else gtk.STATE_SELECTED,
                False, clip, widget, "progressbar",
                x + pos, y + (h - logical_rect.height)/2,
                layout);

        clip.x = clip.x + clip.width;
        clip.width = w - clip.width;

        if window.__class__ is gtk.gdk.Window:
            widget.get_style().paint_layout(window,
                gtk.STATE_SELECTED if is_rtl else gtk.STATE_NORMAL,
                False, clip, widget, "progressbar",
                x + pos, y + (h - logical_rect.height)/2,
                layout);
    def on_activate(self, event, widget, path, background_area, cell_area, flags):
        if event == None: return False
        value = max(0.0,min(1.0, (event.x - cell_area.x)/cell_area.width ))
        self.emit('value-changed', path, value)
        return True
    #def on_start_editing(self, event, widget, path, background_area, cell_area, flags):
    #    print "editing"
    #    print event
gobject.type_register(HSliderCellRenderer)
