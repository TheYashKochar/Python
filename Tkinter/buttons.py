# Test program created while learning the use of Button
from tkinter import *
root = Tk()
def myClick():
    myLabel = Label(root, text="Button Clicked !!").pack()
myButton = Button(root, text="Click Me!",command= myClick, fg="blue", bg="#000000") #padx = 50, pady = 50)   #, state = DISABLED)
myButton.pack()
root.mainloop()
