import tkinter as tk

def login_window():
    login_window = tk.Toplevel(root)
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "1234":
        result_label.config(text="Login successful!")
    else:
        result_label.config(text="Login failed!")


# create a tkinter window
root = tk.Tk()
root.title("Login")

# create a label for the username
username_label = tk.Label(root, text="Username:")
username_label.pack()

# create an entry field for the username
username_entry = tk.Entry(root)
username_entry.pack()

# create a label for the password
password_label = tk.Label(root, text="Password:")
password_label.pack()

# create an entry field for the password
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# create a button to login
# login_button = tk.Button(root, text="Login", command=login)
# login_button.pack()
#
# # create a label to display the result of the login attempt
# result_label = tk.Label(root, text="")
# result_label.pack()


# create login window here

def register_window():
    register_window = tk.Toplevel(root)
    # create register window here

root = tk.Tk()

login_button = tk.Button(root, text="Login", command=login_window)
login_button.pack()

register_button = tk.Button(root, text="Register", command=register_window)
register_button.pack()

root.mainloop()