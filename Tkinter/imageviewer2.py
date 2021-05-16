from tkinter import *
# Basic Image Viewer/ Gallery Program
from PIL import ImageTk,Image

root = Tk()
root.title('Image Test')
root.iconbitmap('Assets\macos.ico')
root.geometry("1280x720")

my_img = ImageTk.PhotoImage(Image.open('Assets\instagram.png'))
my_img1 = ImageTk.PhotoImage(Image.open('Assets\img (1).jpg'))
my_img2 = ImageTk.PhotoImage(Image.open('Assets\img (2).jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('Assets\img (3).jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('Assets\img (4).jpg'))
my_img5 = ImageTk.PhotoImage(Image.open('Assets\img (5).jpg'))

img_list = [my_img,my_img1,my_img2,my_img3,my_img4,my_img5]
status = Label(root, text='Image 1 of ' + str(len(img_list)), bd=1, relief = SUNKEN, anchor =E)

frame = LabelFrame(root, padx=5,pady=5,width=640,height=480)
frame.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

my_label = Label(frame,image = my_img)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_back
    global button_forward
    my_label.grid_forget()
    my_label = Label(frame,image= img_list[image_number-1])
    button_forward = Button(root, text='>>', command = lambda: forward(image_number+1))
    button_back = Button(root, text='<<', command = lambda: back(image_number-1))
    if image_number == 6:
        button_forward = Button(root,text=">>",state = DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column = 0)
    button_exit.grid(row=1, column = 1)
    button_forward.grid(row=1, column = 2)
    status = Label(root, text='Image '+ str(image_number) +' of ' + str(len(img_list)), bd=1, relief = SUNKEN, anchor =E)
    status.grid(row=2, column = 0, columnspan = 3, sticky = W+E)


def back(image_number):
    global my_label
    global button_back
    global button_forward
    my_label.grid_forget()
    my_label = Label(frame,image= img_list[image_number-1])
    button_forward = Button(root, text='>>', command = lambda: forward(image_number+1))
    button_back = Button(root, text='<<', command = lambda: back(image_number-1))
    if image_number == 1:
        button_back = Button(root,text="<<",state = DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column = 0)
    button_exit.grid(row=1, column = 1)
    button_forward.grid(row=1, column = 2)

button_back = Button(root, text='<<', command = back, state = DISABLED)
button_exit = Button(root, text='EXIT PROGRAM',command = root.quit)
button_forward = Button(root, text='>>', command = lambda: forward(2))

button_back.grid(row=1, column = 0)
button_exit.grid(row=1, column = 1)
button_forward.grid(row=1, column = 2, pady = 10)
status.grid(row=2, column = 0, columnspan = 3, sticky = W+E)

root.mainloop()