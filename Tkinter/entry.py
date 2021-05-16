# Test program created while learning the use of Entry
from tkinter import *
root = Tk()
e = Entry(root, width = 50, borderwidth=5) #bg="blue", fg="white")
e.pack()
e.insert(0,'Enter Your Name: ')
def myClick():
    Hello = 'Hello '+ e.get()
    myLabel = Label(root, text= Hello).pack() #'Hello ' + e.get()).pack()
myButton = Button(root, text="Enter Name",command= myClick, fg="blue", bg="#000000") #padx = 50, pady = 50)   #, state = DISABLED)
myButton.pack()
root.mainloop()
