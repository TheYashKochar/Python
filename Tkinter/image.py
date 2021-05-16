# Test program created while learning the image import
from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('Image Test')
root.iconbitmap('Assets\macos.ico')
my_img = ImageTk.PhotoImage(Image.open('Assets\instagram.png'))
my_label = Label(image = my_img).pack()

button_quit = Button(root, text='Exit Program', command=root.quit).pack()

root.mainloop()