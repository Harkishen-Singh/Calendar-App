#from main_app.py import Calendar
import gi
from gi.repository import Gtk
gi.require_version('Gtk', '3.0')

class Gui(Gtk.Window):

    def startup(self):
        start = Gtk.Window()
        start.set_title("Input Values")
        start.set_border_width(10)
        start.set_default_size(300, 300)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing = 10 )
        start.add(box)

        l_year = Gtk.Label()
        l_year.set_label("Enter the Year Below")
        box.add(l_year)
        self.in_year = Gtk.Entry()
        self.in_year.set_text("Complete Year Number")
        box.add(self.in_year)

        l_month = Gtk.Label()
        l_month.set_label("Select Month")
        box.add(l_month)


        # radio button Below

        self.r1 = Gtk.RadioButton.new_with_label_from_widget(None, "Click Any One")

        box.pack_start(self.r1, False, False, 0 )
        self.r11 = Gtk.RadioButton.new_with_label_from_widget(self.r1, "January")

        box.pack_start(self.r11, False, False, 0 )

        r2 = Gtk.RadioButton.new_from_widget(self.r1)
        r2.connect("toggled", self.gotinput, "February")
        r2.set_label("February")
        box.pack_start(r2, False, False, 0 )
        r3 = Gtk.RadioButton.new_from_widget(self.r1)
        r3.set_label("March")
        r3.connect("toggled", self.gotinput, "March")
        box.pack_start(r3, False, False, 0 )
        r4 = Gtk.RadioButton.new_from_widget(self.r1)
        r4.set_label("April")
        r4.connect("toggled", self.gotinput, "April")
        box.pack_start(r4, False, False, 0 )

        r5 = Gtk.RadioButton.new_from_widget(self.r1)
        r5.set_label("May")
        r5.connect("toggled", self.gotinput, "May")
        box.pack_start(r5, False, False, 0 )

        r6 = Gtk.RadioButton.new_from_widget(self.r1)
        r6.set_label("June")
        r6.connect("toggled", self.gotinput, "June")
        box.pack_start(r6, False, False, 0 )

        r7 = Gtk.RadioButton.new_from_widget(self.r1)
        r7.set_label("July")
        r7.connect("toggled", self.gotinput, "March")
        box.pack_start(r7, False, False, 0 )

        r8 = Gtk.RadioButton.new_from_widget(self.r1)
        r8.set_label("August")
        r8.connect("toggled", self.gotinput, "August")
        box.pack_start(r8, False, False, 0 )

        r9 = Gtk.RadioButton.new_from_widget(self.r1)
        r9.set_label("September")
        r9.connect("toggled", self.gotinput, "September")
        box.pack_start(r9, False, False, 0 )

        self.r10 = Gtk.RadioButton.new_from_widget(self.r1)
        self.r10.set_label("October")

        box.pack_start(self.r10, False, False, 0 )

        r11 = Gtk.RadioButton.new_from_widget(self.r1)
        r11.set_label("November")
        r11.connect("toggled", self.gotinput, "November")
        box.pack_start(r11, False, False, 0 )
        self.r12 = Gtk.RadioButton.new_from_widget(self.r1)
        self.r12.set_label("December")
        box.pack_start(self.r12, False, False, 0)
        self.r12.connect("toggled", self.gotinput, "December")
        self.r10.connect("toggled", self.gotinput, "October")

        button = Gtk.Button(label = "Close")
        box.add(button)
        button.connect("clicked", Gtk.main_quit)

        start.show_all()
        start.connect("delete-event", Gtk.main_quit)
        print("Reached here")

    def gotinput(self, Widget, mon):
        self.month = mon
        self.year = self.in_year.get_text()
        print("month :" + self.month)
        print("year  :" + str(self.year))

    def Calender_design_layout(self):
        



obj = Gui()
#obj.show_all()
#obj.connect("delete-event", Gtk.main_quit)
obj.startup()
Gtk.main()
