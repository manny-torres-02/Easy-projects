# Importing tkinter module 
from tkinter import *
# import tkinter as tk - newer themed widgets 
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

# Set up main app window, give title 
root = Tk()
root.title("Feet to Meters")

# frame widget - holds contents of the user interface 
# once frame is created, gird places it directly inside the main application window
# columnfonfigure/rowconfigure - tells tk That the fram should expand to fill any extra space if window is resized
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# First widget created is an entry field, which is a single line text field 
# asks for an input of feet, and stores it in a variable called feet
# each widget will ask for a frame and a position in the frame
# In Python and Ruby, the parent is passed as the first parameter when instantiating a widget object.
feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

# This tells python to enter into the venet loop and allow for user interaction

root.mainloop()