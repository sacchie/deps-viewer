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
    context.paint()

area = Gtk.DrawingArea()
win.add(area)
area.connect("draw", on_draw)

win.show_all()
Gtk.main()
