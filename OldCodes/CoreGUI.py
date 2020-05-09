#This program makes selecting a slice of a CT scan easyier with a small GUI to help select the right slice
#It uses the GUI library, tkinter, to create a simple GUI.
#It also uses the numpy library for
#and it uses matplotlib to create an image of the CT scans
#To use, run the code in a terminal in the format of: python GUItest.py (filename)
#select the file number you want with the slider, save the file if you want to, close the matplotlib image, then continue as you wish
#to close, either ctr + c or type n when the program askls to continue after you close the GUI.


import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import sys


isize = 300
#loads information from the dat file
X = np.loadtxt(sys.argv[1], skiprows = 4)

#These variables can also be changed to match wehat the user wants in terms of dimensions of the network
x_top    = int(0)
x_bottom = int(300)
y_left   = int(0)
y_right  = int(300)
inpute = 0
islice = 0

#basically just takes the values from the slider with the .get() function
def take_values():

    inpute = w.get()
    print(inpute)
    return inpute

#takes the input from the user and selects the file based on that input
def whatever():
    #uses the input
    islice = take_values()
    X2 = X[isize*islice:isize*islice+isize,:]
    print(islice)
    #creates an image of the network
    plt.matshow(X2[x_top : x_bottom, y_left : y_right])
    plt.show()




while 1:

    #m is the frame of a gui, the master. we can add a title with .add
    m = tk.Tk()
    m.title('Selecting Slice')
    #b is a button, witht the command of stoping the gui when you click it
    b = tk.Button(m, width=25, command=m.destroy, text='Stop')
    b.pack()
    #The pack function formats the widgets for you
    #w is our scale
    w = tk.Scale(m, from_=1, to=300, length=400, orient=tk.HORIZONTAL, label="Slice Number")
    w.pack()
    #s is the show value and image button
    s = tk.Button(m, text='Show Slider Input', command=whatever).pack()
    m.mainloop()

    print("Continue?", end=' ')
    end = input()
    if end == "y":
        continue
    else:
        break