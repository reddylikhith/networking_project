import tkinter as tk
from tkinter import *
window = tk.Tk()
window.geometry("500x600")
window.title("ONLINE TRAIN TICKET BOOKING")
Label(text="TRAIN TICKET BOOKING",width=30,height=3,font=("Arial",20),bg="white").pack()
Label(text="").pack()
#login_label = tk.Label(text="Click the login button to log in:")
#login_label.pack()
login_button = tk.Button(text="LOGIN",bg="white",fg="black",font=10,height=2,width=10)
login_button.pack()
Label(text="").pack()
#register_label = tk.Label(text="Click the register button to register:")
#register_label.pack()
signup_button = tk.Button(text="REGISTER",bg="white",fg="black",font=10,height=2,width=10)
signup_button.pack()
Label(text="").pack()
window.mainloop()

