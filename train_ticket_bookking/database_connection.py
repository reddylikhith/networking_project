import pymongo
import threading
from  pymongo import MongoClient
from tkinter import *
from tkinter import messagebox
class Booktrain():
    def _init_(self):
        self.cl=MongoClient("mongodb+srv://josetellis2018:dHmjZHB5MZgPsH0f@cluster0.ghrj9wz.mongodb.net/?retryWrites=true&w=majority")
        self.db=self.cl['hcl_data']
        self.col=self.db['train_data']
        self.lock=threading.Lock()
    def read(self):
        self.lock.acquire()
        try:
            result=self.col.find({},{"_id":0})
            for r in result:
                print(r)
        finally:
            self.lock.release()
    def update_tkt(self,seats,tnum):
        # aqcquire the lock before accessing the shared resource
        self.lock.acquire()
        try:
            # access the shared resource
            r=self.col.find_one({},{"_id":0})
            avail=r["No_of_seats"]
            if seats<=avail:
                avail = avail - seats
                messagebox.showinfo('Status',"Seats are booked")
            else:
                print("Seats are not available")
                messagebox.showinfo('Status',"Seats are not available")


            up_qury={"$set":{"No_of_seats":avail}}
            fil_cd={"Train_no":tnum}
            self.col.update_one(fil_cd,up_qury)
        finally:
            # release the lock after accessing the shared resource
            self.lock.release()
# update_tkt(101)