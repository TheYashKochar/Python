# Test program created while learning the use of image in Program
from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('Image Test')
root.iconbitmap('Assets\macos.ico')
my_img = ImageTk.PhotoImage(Image.open('Assets\instagram.png'))
my_img = my_img.resize((200, 200), Image.ANTIALIAS)
my_label = Label(image = my_img).pack()

button_quit = Button(root, text='Exit Program', command=root.quit).pack()

root.mainloop()