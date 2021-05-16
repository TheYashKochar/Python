# Program to Generate a Frame using Tkinter
from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('Image Test')
root.iconbitmap('Assets\macos.ico')
frame = LabelFrame(root, padx=5,pady=5) #,text='This is my Frame...')
frame.pack(padx=10,pady=10)
b = Button(frame, text='Don\'t click here')
b.pack()
#b.grid(row=2,column =4)

root.mainloop()