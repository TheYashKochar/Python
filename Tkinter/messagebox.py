# Test program created while learning the use of MessageBox
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
root = Tk()
root.title('Image Test')
root.iconbitmap('Assets\macos.ico')

# showinfo, showwarning, showerror, askquestion,  askokcancel, askyesno
def popup():
    response = messagebox.askyesno("This is my popup!", "Hello World")
    #Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked Yes!").pack()
    else :
        Label(root, text="No was clicked!").pack()

Button(root,text='Popup', command= popup).pack()

root.mainloop()