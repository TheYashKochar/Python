# Test program created while learning the use of Checkbox
from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('Checkbox Test')
root.iconbitmap('Assets\macos.ico')

def show():
    my_label=Label(root,text=var.get()).pack()


#var = IntVar()
var = StringVar()

#c = Checkbutton(root,text='Check this box',variable = var,onvalue='On',offvalue='Off')
c = Checkbutton(root,text='Do you want supersize ?',variable = var,onvalue='Supersize',offvalue='Regular Size')
c.deselect()
c.pack()

myButton = Button(root, text="Show Selection", command = show).pack()

root.mainloop()