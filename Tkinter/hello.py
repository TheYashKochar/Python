# First Tinker Program
from tkinter import *
root = Tk()
myLabel = Label(root, text="Hello World!").grid(row=0, column=0)
myLabel2 = Label(root, text="Hello World Again!").grid(row=1, column=0)

#myLabel.grid(row=0, column=0)
#myLabel2.grid(row=1, column=0)
#myLabel.pack()
root.mainloop()
