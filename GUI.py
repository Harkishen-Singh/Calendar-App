from main_app.py import Calendar
import gi
from gi.repository import Gtk
gi.require_version('Gtk', '3.0')

class Gui(Gtk.Window, Calendar):

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

        if self.month == 1 OR self.month==3 OR self.month==5 OR self.month == 7 OR self.month==8 OR self.month== 10 OR self.month==12:
            self.last=31
        elif self.month != 2:
            self.last = 30
        elif self.month == 2:
            if self.year % 4 == 0 :
                self.last = 29
            else :
                self.last = 28
        '''r = 0 # represents the row of the Widget
        c = 0 # represents the row of the Widget'''

        # where self.last represents the last day on that specified Month
        layout = Gtk.Window()
        layout.set_title("Calender of " + self.month + ", "+ self.year)
        layout.set_border_width(10)
        layout.set_default_size(800, 800)

        grid = Gtk.Grid()
        layout.add(grid)

        #default date Buttons Below

        date_1 = Gtk.Button(label="1")
        date_2 = Gtk.Button(label="2")
        date_3 = Gtk.Button(label="3")
        date_4 = Gtk.Button(label="4")
        date_5 = Gtk.Button(label="5")
        date_6 = Gtk.Button(label="6")
        date_7 = Gtk.Button(label="7")
        date_8 = Gtk.Button(label="8")
        date_9 = Gtk.Button(label="9")
        date_10 = Gtk.Button(label="10")
        date_11 = Gtk.Button(label="11")
        date_12 = Gtk.Button(label="12")
        date_13 = Gtk.Button(label="13")
        date_14 = Gtk.Button(label="14")
        date_15 = Gtk.Button(label="15")
        date_16 = Gtk.Button(label="16")
        date_17 = Gtk.Button(label="17")
        date_18 = Gtk.Button(label="18")
        date_19 = Gtk.Button(label="19")
        date_20 = Gtk.Button(label="20")
        date_21 = Gtk.Button(label="21")
        date_22 = Gtk.Button(label="22")
        date_23 = Gtk.Button(label="23")
        date_24 = Gtk.Button(label="24")
        date_25 = Gtk.Button(label="25")
        date_26 = Gtk.Button(label="26")
        date_27 = Gtk.Button(label="27")
        date_28 = Gtk.Button(label="28")
        date_29 = Gtk.Button(label="29")
        date_30 = Gtk.Button(label="30")
        date_31 = Gtk.Button(label="31")    # till 31 buttons in order to avoid errors

        #end of declaring buttons for date
        r = []
        c = []
        r.append(0) # initialising so that the following values starts from index 1
        c.append(0)

        for i in range(1, self.last +1):    # row allocation OR Day allocation
            self.day = get_day(self.year, self.month, i)

            if self.day == "Sunday":
                r.append(1)
            elif self.day == "Monday":
                r.append(2)
            elif self.day == "Tuesday":
                r.append(3)
            elif self.day == "Wednesday":
                r.append(4)
            elif self.day == "Thursday":
                r.append(5)
            elif self.day == "Friday":
                r.append(6)
            elif self.day == "Saturday":
                r.append(7)

        # column allotment begis Below

        col = 0
        if r[1] == "Sunday":
            k =0
            for i in range(1, self.last +1):
                k = k + 1
                if k % 7 == 1 :
                    col = col + 1
                    c.append(col)
                else :
                    c.append(col)
        elif r[1] == "Monday":
            k = 1
            col = 1
            for i in range(1, self.last + 1):
                k = k + 1
                if k % 7 == 1:
                    col = col + 1
                    c.append(col)
                else :
                    c.append(col)
        elif r[1] == "Tuesday":
            k = 2
            col = 1
            for i in range(1, self.last + 1):
                k = k + 1
                if k % 7 == 1:
                    col = col + 1
                    c.append(col)
                else :
                    c.append(col)
        elif r[1] == "Wednesday":
            k = 3
            col = 1
            for i in range(1, self.last + 1):
                k = k + 1
                if k % 7 == 1:
                    col = col + 1
                    c.append(col)
                else :
                    c.append(col)
        elif r[1] == "Thursday":
            k = 4
            col = 1
            for i in range(1, self.last + 1):
                k = k + 1
                if k % 7 == 1:
                    col = col + 1
                    c.append(col)
                else :
                    c.append(col)
        elif r[1] == "Friday":
            k = 5
            col = 1
            for i in range(1, self.last + 1):
                k = k + 1
                if k % 7 == 1:
                    col = col + 1
                    c.append(col)
                else :
                    c.append(col)
        elif r[1] == "Saturday":
            k = 6
            col = 1
            for i in range(1, self.last + 1):
                k = k + 1
                if k % 7 == 1:
                    col = col + 1
                    c.append(col)
                else :
                    c.append(col)
         # column allotment finished


        #for i in range(1, self.last + 1): # column allocation based on maximum catching limit




obj = Gui()
#obj.show_all()
#obj.connect("delete-event", Gtk.main_quit)
obj.startup()
Gtk.main()
