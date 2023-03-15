from tkinter import *

root = Tk() #creates main window
root.title("ETERNITY CALCULATOR")

entry = Entry(root, width=50, borderwidth=5, relief=RIDGE, fg="Black", bg="White")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=15)#pushes into window
root.mainloop() #runs window continuously unless u exit


