import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkcalendar import DateEntry
import tkinter as tktt
from tkinter import messagebox
from tkinter.ttk import Combobox
from subprocess import call


from pymongo import MongoClient
class details():
    def validate_details(self,name,tnum,date,src,dst,tkts):
        self.name=name
        self.tnum = tnum
        self.date = date
        self.src=src
        self.dst=dst
        self.tkts=tkts
        cl = MongoClient(
            "mongodb+srv://josetellis2018:dHmjZHB5MZgPsH0f@cluster0.ghrj9wz.mongodb.net/?retryWrites=true&w=majority")
        db = cl['hcl_data']
        col = db['tkt_book']
        col.insert_one({"Train Number:":self.tnum,"date:":self.date, "source":self.src,"destination":self.dst,"Tickets":self.tkts})
        from mongodbconnection import Booktrain
        obj=Booktrain()
        obj.update_tkt(tkts,tnum)
    def details_func(self):
        base=tktt.Tk()
        base.geometry('400x500')
        labl_1 = Label(base, text="WELCOME TO TRAIN BOOKING", width=40, font=("bold", 15),fg="brown")
        labl_1.place(x=0, y=10)

        labl_0 = Label(base, text="Name", width=20, font=("bold", 10))
        labl_0.place(x=1, y=50)
        self.name = tktt.StringVar()

        entry_0 = Entry(base, textvariable=self.name)
        entry_0.place(x=100, y=50)

        labl_1 = Label(base, text="Train Number", width=20, font=("bold", 10))
        labl_1.place(x=2, y=80)
        self.tnum = tktt.IntVar()

        entry_01 = Entry(base, textvariable=self.tnum)
        entry_01.place(x=130, y=80)

        date_label=Label(base, text="Select a date:")
        date_label.place(x=50,y=120)
        self.date=tktt.StringVar()
        date_entry=DateEntry(base,textvariable=self.date,width=12,background='darkblue',foreground='white',borderwidth=2)
        date_entry.place(x=130, y=120)
        labl_2 = Label(base, text="Source", width=20, font=("bold", 10))
        labl_2.place(x=10, y=160)
        self.src = tktt.StringVar()
        options=["vijayawada","hyderabad","bangalore","chennai"]
        combo_01 = Combobox(base,textvariable=self.src, values=options)
        combo_01.place(x=130, y=160)
        #combo_01.current(0)
        labl_3 = Label(base, text="Destination", width=20, font=("bold", 10))
        labl_3.place(x=4, y=200)
        self.dst = tktt.StringVar()

        combo_02 = Combobox(base, textvariable=self.dst, values=options)
        combo_02.place(x=130, y=200)



        labl_4 = Label(base, text="No of Tickets", width=20, font=("bold", 10))
        labl_4.place(x=0, y=240)
        self.tkts = tktt.IntVar()

        entry_04 = Entry(base, textvariable=self.tkts)
        entry_04.place(x=130, y=240)

        Button(base, text='Submit', width=10, bg='brown', fg='white',command=lambda :self.validate_details(self.name.get(),self.tnum.get(),self.date.get(),self.src.get(),self.dst.get(),self.tkts.get())).place(x=120, y=280)
        base.mainloop()

obj=details()
obj.details_func()