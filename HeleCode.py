import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import os

user = 'Adriann Liceralde'
file = 'F42A.dat' 
os.chdir('C:\\Users\\'+str(user)+'\\Desktop\\Repository\\HeleShaw\\CoreSamples')

isize = 300 #Do Not Change from 300
X = np.loadtxt(file, skiprows = 4)

islice = 250
X2 = X[isize*islice:isize*islice+isize,:]

def take_values():
    inpute = w.get()
    print(inpute)
    return inpute

#takes the input from the user and selects the file based on that input
def whatever():
    #creates an image of the network
    plt.close('all')
    x_top    = 0
    x_bottom = 300
    y_left   = 0
    y_right  = 300

    plt.matshow(X2[x_top : x_bottom, y_left : y_right], origin = 'lower')
    plt.gca().xaxis.tick_bottom()
    
    y_bot = take_values()
    y_top = 200
    x_left  = 10
    x_right = 200

    plt.hlines(y_bot, 0, 299, 'r')
    plt.hlines(y_top, 0, 299, 'r')
    plt.vlines(x_left, 0, 299, 'r')
    plt.vlines(x_right, 0, 299, 'r')
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