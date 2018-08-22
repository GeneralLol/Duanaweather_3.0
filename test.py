import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("DuanaweatherUI.glade")
window = builder.get_object("window_0")
window.show_all()