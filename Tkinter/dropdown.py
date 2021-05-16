# Test program created while learning the use of Dropdown
from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('Drop Down Menu Test')
root.geometry('400x400')

def show():
    my_label=Label(root, text=clicked.get()).pack()

options = [
   'Monday','Tuesday','Wednesday','Thursday','Friday'
]

clicked = StringVar()
#clicked.set("Monday")
clicked.set(options[0])

#drop = OptionMenu(root, clicked, "Monday","Tuesday","Wednesday","Thurday","Friday")
drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection",command = show).pack()

root.mainloop()