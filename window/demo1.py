import tkinter as tk
from tkinter import messagebox


# Define a function to handle button click events
def book_ticket():
    # Get the values entered in the input fields
    name = name_entry.get()
    source = source_entry.get()
    destination = dest_entry.get()
    date = date_entry.get()
    class_type = class_var.get()

    # Check if any of the fields are empty
    if not (name and source and destination and date and class_type):
        error_label.config(text="Please fill all fields")
        return

    # Create a ticket string to display to the user
    ticket_str = f"Name: {name}\nSource: {source}\nDestination: {destination}\nDate: {date}\nClass: {class_type}"
    ticket_label.config(text=ticket_str)


# Create the main window
root = tk.Tk()
root.title("Train Ticket Booking System")

# Create the input fields and labels
name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry.grid(row=0, column=1, padx=5, pady=5)

source_label = tk.Label(root, text="Source:")
source_entry = tk.Entry(root)
source_label.grid(row=1, column=0, padx=5, pady=5)
source_entry.grid(row=1, column=1, padx=5, pady=5)

dest_label = tk.Label(root, text="Destination:")
dest_entry = tk.Entry(root)
dest_label.grid(row=2, column=0, padx=5, pady=5)
dest_entry.grid(row=2, column=1, padx=5, pady=5)

date_label = tk.Label(root, text="Date:")
date_entry = tk.Entry(root)
date_label.grid(row=3, column=0, padx=5, pady=5)
date_entry.grid(row=3, column=1, padx=5, pady=5)

class_label = tk.Label(root, text="Class:")
class_label.grid(row=4, column=0, padx=5, pady=5)

# Create radio buttons for the class type
class_var = tk.StringVar()
class_var.set("Economy")
economy_rb = tk.Radiobutton(root, text="Economy", variable=class_var, value="Economy")
business_rb = tk.Radiobutton(root, text="Business", variable=class_var, value="Business")
economy_rb.grid(row=4, column=1, padx=5, pady=5)
business_rb.grid(row=4, column=2, padx=5, pady=5)

# Create a button to book the ticket
book_button = tk.Button(root, text="Book Ticket", command=book_ticket)
book_button.grid(row=5, column=1, padx=5, pady=5)

# Create a label to display errors
error_label = tk.Label(root, fg="red")
error_label.grid(row=6, column=1, padx=5, pady=5)

# Create a label to display the ticket information
ticket_label = tk.Label(root, fg="green")
ticket_label.grid(row=7, column=1, padx=5, pady=5)


# Start the main loop
root.mainloop()