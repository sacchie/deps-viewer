import gi
import random

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

win = Gtk.Window()
win.connect("destroy", Gtk.main_quit)

rand = random.Random()

def on_draw(area, context):
    context.scale(area.get_allocated_width(), area.get_allocated_height())    
    context.set_source_rgb(rand.random(), 0.5, 0.7)
    context.fill()
    context.move_to(0,0)
    context.show_text("aaa")
    context.paint()
    

    # layout = area.create_pango_layout("HELLO")
    # # layout.show_in_cairo_context(context)
    # print(dir(layout))

    # cr = win.cairo_create()
    # cr.set_source_rgb(0.1, 0.1, 0.1)
    # cr.set_font_size(13)
    # cr.move_to(20, 30)
    # cr.show_text("Most relationships seem so transitory")

area = Gtk.DrawingArea()
win.add(area)
area.connect("draw", on_draw)

win.show_all()
Gtk.main()
