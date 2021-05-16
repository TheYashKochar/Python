# Test program created while learning the use of Window
from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('Window Test')
root.iconbitmap('Assets\macos.ico')
def open():
    global my_img
    top = Toplevel()
    top.iconbitmap('Assets\macos.ico')
    top.title('Another One')
    #my_label = Label(top,text ='Hello World').pack()
    my_img = ImageTk.PhotoImage(Image.open('Assets\instagram.png'))
    my_label = Label(top,image = my_img).pack()
    btn2 = Button(top, text='Close Window',command=top.destroy).pack()

btn = Button(root, text='Open Second Window',command=open).pack()

root.mainloop()