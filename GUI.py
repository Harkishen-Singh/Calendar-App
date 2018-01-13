from main_app import Calendar
import gi
from gi.repository import Gtk
gi.require_version('Gtk', '3.0')

class Gui(Gtk.Window, Calendar):

    def __init__(self):
        self.month = 0
        self.year = 0

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
        self.Calender_design_layout()

    def Calender_design_layout(self):

        if self.month == 1 or self.month==3 or self.month==5 or self.month == 7 or self.month==8 or self.month== 10 or self.month==12:
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
        layout.set_title("Calender of " + str(self.month) + ", "+ str(self.year))
        layout.set_border_width(10)
        layout.set_default_size(400, 400)

        grid = Gtk.Grid()
        layout.add(grid)

        #default date Buttons Below
        print("Reached part 1")
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
        p=0
        for i in range(1, self.last +1):    # row allocation OR Day allocation
            self.day = self.get_day(int(self.year), self.month, i)
            p = p+ 1
            if self.day == "Sunday":
                print("reached r sunday" + str(p))
                r.append(1)
            elif self.day == "Monday":
                print("reached r monday" + str(p))
                r.append(2)
            elif self.day == "Tuesday":
                print("reached r Tuesday" + str(p))
                r.append(3)
            elif self.day == "Wednesday":
                print("reached r Wednesday" + str(p))
                r.append(4)
            elif self.day == "Thursday":
                print("reached r Thursday" + str(p))
                r.append(5)
            elif self.day == "Friday":
                print("reached r Friday" + str(p))
                r.append(6)
            elif self.day == "Saturday":
                print("reached r Saturday" + str(p))
                r.append(7)

        # column allotment begis Below
        print("Reached part 2")
        col = 0
        if r[1] == 1:
            k =0
            for i in range(1, self.last +1):
                k = k + 1
                if k % 7 == 1 :
                    col = col + 1
                    c.append(col)
                else :
                    c.append(col)
        elif r[1] == 2:
            k = 1
            col = 1
            for i in range(1, self.last + 1):
                k = k + 1
                if k % 7 == 1:
                    col = col + 1
                    c.append(col)
                else :
                    c.append(col)
        elif r[1] == 3:
            k = 2
            col = 1
            for i in range(1, self.last + 1):
                k = k + 1
                if k % 7 == 1:
                    col = col + 1
                    c.append(col)
                else :
                    c.append(col)
        elif r[1] == 4:
            k = 3
            col = 1
            for i in range(1, self.last + 1):
                k = k + 1
                if k % 7 == 1:
                    col = col + 1
                    c.append(col)
                else :
                    c.append(col)
        elif r[1] == 5:
            print("\nREACHED Thursday C1 \n ")
            k = 4
            col = 1
            for i in range(1, self.last + 1):
                k = k + 1
                if k % 7 == 1:
                    col = col + 1
                    c.append(col)
                else :
                    c.append(col)
        elif r[1] == 6:
            k = 5
            col = 1
            for i in range(1, self.last + 1):
                k = k + 1
                if k % 7 == 1:
                    col = col + 1
                    c.append(col)
                else :
                    c.append(col)
        elif r[1] == 7:
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

        b_sun = Gtk.Button(label="Sunday")
        b_mon = Gtk.Button(label="Monday")
        b_tue = Gtk.Button(label="Tuesday")
        b_wed = Gtk.Button(label="Wednesday")
        b_thu = Gtk.Button(label="Thursday")
        b_fri = Gtk.Button(label="Friday")
        b_sat = Gtk.Button(label="Saturday")

        grid.attach(b_sun, 0, 0, 1,1)
        grid.attach(b_mon, 0, 1, 1,1)
        grid.attach(b_tue, 0, 2, 1,1)
        grid.attach(b_wed, 0, 3, 1,1)
        grid.attach(b_thu, 0, 4, 1,1)
        grid.attach(b_fri, 0, 5, 1,1)
        grid.attach(b_sat, 0, 6, 1,1)
        print(" values of r1, r2, r3 \n")
        print(str(r[2]) + " " )

        # adding the buttons to the grid layout

        grid.attach(date_1, 2 + c[1], r[1] - 1, 1 , 1)
        grid.attach(date_2, 2 + c[2], r[2] - 1, 1 , 1)
        grid.attach(date_3, 2 + c[3], r[3] - 1, 1 , 1)
        grid.attach(date_4, 2 + c[4], r[4] - 1, 1 , 1)
        grid.attach(date_5, 2 + c[5], r[5] - 1, 1 , 1)
        grid.attach(date_6, 2 + c[6], r[6] - 1, 1 , 1)
        grid.attach(date_7, 2 + c[7], r[7] - 1, 1 , 1)
        grid.attach(date_8, 2 + c[8], r[8] - 1, 1 , 1)
        grid.attach(date_9, 2 + c[9], r[9] - 1, 1 , 1)
        grid.attach(date_10, 2 + c[10], r[10] - 1, 1 , 1)
        grid.attach(date_11, 2 + c[11], r[11] - 1, 1 , 1)
        grid.attach(date_12, 2 + c[12], r[12] - 1, 1 , 1)
        grid.attach(date_13, 2 + c[13], r[13] - 1, 1 , 1)
        grid.attach(date_14, 2 + c[14], r[14] - 1, 1 , 1)
        grid.attach(date_15, 2 + c[15], r[15] - 1, 1 , 1)
        grid.attach(date_16, 2 + c[16], r[16] - 1, 1 , 1)
        grid.attach(date_17, 2 + c[17], r[17] - 1, 1 , 1)
        grid.attach(date_18, 2 + c[18], r[18] - 1, 1 , 1)
        grid.attach(date_19, 2 + c[19], r[19] - 1, 1 , 1)
        grid.attach(date_20, 2 + c[20], r[20] - 1, 1 , 1)
        grid.attach(date_21, 2 + c[21], r[21] - 1, 1 , 1)
        grid.attach(date_22, 2 + c[22], r[22] - 1, 1 , 1)
        grid.attach(date_23, 2 + c[23], r[23] - 1, 1 , 1)
        grid.attach(date_24, 2 + c[24], r[24] - 1, 1 , 1)
        grid.attach(date_25, 2 + c[25], r[25] - 1, 1 , 1)
        grid.attach(date_26, 2 + c[26], r[26] - 1, 1 , 1)
        grid.attach(date_27, 2 + c[27], r[27] - 1, 1 , 1)
        grid.attach(date_28, 2 + c[28], r[28] - 1, 1 , 1)
        if self.last == 29:
            grid.attach(date_29, 2 + c[29], r[29] - 1, 1 , 1)
        elif self.last == 30:
            grid.attach(date_29, 2 + c[29], r[29] - 1, 1 , 1)
            grid.attach(date_30, 2 + c[30], r[30] - 1, 1 , 1)
        elif self.last == 31:
            grid.attach(date_29, 2 + c[29], r[29] - 1, 1 , 1)
            grid.attach(date_30, 2 + c[30], r[30] - 1, 1 , 1)
            grid.attach(date_31, 2 + c[31], r[31] - 1, 1 , 1)
        layout.show_all()
        layout.connect("delete-event", Gtk.main_quit)


obj = Gui()
#obj.show_all()
#obj.connect("delete-event", Gtk.main_quit)
obj.startup()
Gtk.main()
