# Program to Generate Random Graph
from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib as plt

root = Tk()
root.title('Matplot Test')
root.geometry('400x200')

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()

my_btn = Button(root,text='Graph It!',command=graph)
my_btn.pack()

root.mainloop()