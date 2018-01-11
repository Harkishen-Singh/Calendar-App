#from main_app.py import Calendar
from gi.repository import Gtk
#gi.require_version("Gtk", "3.0")

class Gui(Gtk.Window):

    def startup(self):
        start = Gtk.Window()
        start.set_title("Input Values")
        start.set_border_width(10)
        start.set_default_size(300, 300)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 10 )
        start.add(box)

        l_month = Gtk.Label()
        l_month.set_label("Enter the Month Below")
        box.add(l_month)
        self.in_month = Gtk.Entry()
        self.in_month.set_text("Month Name")
        box.add(self.in_month)

        l_year = Gtk.Label()
        l_year.set_label("Enter the Year Below")
        box.add(l_year)
        self.in_year = Gtk.Entry()
        self.in_year.set_text("Complete Year Number")
        box.add(self.in_year)

        button = Gtk.Button(label = "Submit")
        box.add(button)
        button.connect("clicked", self.gotinput)
        button.connect("clicked", Gtk.main_quit)
        start.show_all()
        start.connect("delete-event", Gtk.main_quit)
        print("Reached here")

    def gotinput(self, Widget):
        self.month = self.in_month.get_text()
        self.year = self.in_year.get_text()
        print("month :" + self.month)
        print("year  :" + str(self.year))
obj = Gui()
#obj.show_all()
#obj.connect("delete-event", Gtk.main_quit)
obj.startup()
Gtk.main()
