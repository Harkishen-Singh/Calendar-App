class Calendar:
    def get_day(self,y,m,d):
        nd=0
        if y>=2018:
            dy=y-2018
            if dy>2:
                nd=nd+1
            x=dy//4
            nd=nd+(366*x)+(365*(dy-x))
            if (y%4==0):
                if m==1:
                    nd=nd+d
                elif m==2:
                    nd=nd+31+d
                elif m==3:
                    nd=nd+31+29+d
                elif m==4:
                    nd=nd+31+29+31+d
                elif m==5:
                    nd=nd+31+29+31+30+d
                elif m==6:
                    nd=nd+31+29+31+30+31+d
                elif m==7:
                    nd=nd+31+29+31+30+31+30+d
                elif m==8:
                    nd=nd+31+29+31+30+31+30+31+d
                elif m==9:
                    nd=nd+31+29+31+30+31+30+31+31+d
                elif m==10:
                    nd=nd+31+29+31+30+31+30+31+31+30+d
                elif m==11:
                    nd=nd+31+29+31+30+31+30+31+31+30+31+d
                else:
                    nd=nd+31+29+31+30+31+30+31+31+30+31+30+d
            else:
                if m==1:
                    nd=nd+d
                elif m==2:
                    nd=nd+31+d
                elif m==3:
                    nd=nd+31+28+d
                elif m==4:
                    nd=nd+31+28+31+d
                elif m==5:
                    nd=nd+31+28+31+30+d
                elif m==6:
                    nd=nd+31+28+31+30+31+d
                elif m==7:
                    nd=nd+31+28+31+30+31+30+d
                elif m==8:
                    nd=nd+31+28+31+30+31+30+31+d
                elif m==9:
                    nd=nd+31+28+31+30+31+30+31+31+d
                elif m==10:
                    nd=nd+31+28+31+30+31+30+31+31+30+d
                elif m==11:
                    nd=nd+31+28+31+30+31+30+31+31+30+31+d
                else:
                    nd=nd+31+28+31+30+31+30+31+31+30+31+30+d
        else:
            dy=2017-y
            if dy<4:
                nd=nd+1
            x=dy//4
            nd=nd+(366*x)+(365*(dy-x))
            if y%4==0:
                if m==1:
                    nd=nd+31+30+31+30+31+31+30+31+30+31+29+31-d
                elif m==2:
                    nd=nd+31+30+31+30+31+31+30+31+30+31+29-d
                elif m==3:
                    nd=nd+31+30+31+30+31+31+30+31+30+31-d
                elif m==4:
                    nd=nd+31+30+31+30+31+31+30+31+30-d
                elif m==5:
                    nd=nd+31+30+31+30+31+31+30+31-d
                elif m==6:
                    nd=nd+31+30+31+30+31+31+30-d
                elif m==7:
                    nd=nd+31+30+31+30+31+31-d
                elif m==8:
                    nd=nd+31+30+31+30+31-d
                elif m==9:
                    nd=nd+31+30+31+30-d
                elif m==10:
                    nd=nd+31+30+31-d
                elif m==11:
                    nd=nd+31+30-d
                else:
                    nd=nd+31-d
            else:
                if m==1:
                    nd=nd+31+30+31+30+31+31+30+31+30+31+28+31-d
                elif m==2:
                    nd=nd+31+30+31+30+31+31+30+31+30+31+28-d
                elif m==3:
                    nd=nd+31+30+31+30+31+31+30+31+30+31-d
                elif m==4:
                    nd=nd+31+30+31+30+31+31+30+31+30-d
                elif m==5:
                    nd=nd+31+30+31+30+31+31+30+31-d
                elif m==6:
                    nd=nd+31+30+31+30+31+31+30-d
                elif m==7:
                    nd=nd+31+30+31+30+31+31-d
                elif m==8:
                    nd=nd+31+30+31+30+31-d
                elif m==9:
                    nd=nd+31+30+31+30-d
                elif m==10:
                    nd=nd+31+30+31-d
                elif m==11:
                    nd=nd+31+30-d
                else:
                    nd=nd+(31-d)
        day=nd%7
        if y>=2018:
            if day==0:
                print("sun")
            if day==1:
                print("mon")
            if day==2:
                print("tue")
            if day==3:
                print("wed")
            if day==4:
                print("thur")
            if day==5:
                print("fri")
            if day==6:
                print("sat")
        else:
            day=7-day
            if day==0:
                print("sun")
            if day==1:
                print("mon")
            if day==2:
                print("tue")
            if day==3:
                print("wed")
            if day==4:
                print("thur")
            if day==5:
                print("fri")
            if day==6:
                print("sat")




obj = Calendar()
y = int(input("Year : "))
m = int(input("month :"))
d = int(input("date : "))
obj.get_day(y,m,d)
