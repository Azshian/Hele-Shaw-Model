#Libraries
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import os

#Set File
user = 'Adriann Liceralde'
file = 'F42A.dat' 
os.chdir('C:\\Users\\'+str(user)+'\\Desktop\\Repository\\HeleShaw\\CoreSamples')
isize = 300                             #Do Not Change from 300
X = np.loadtxt(file, skiprows = 4)

#Extract values from slider
def take_values():
    input1 = w1.get()
    input2 = w2.get()
    input3 = w3.get()
    input4 = w4.get()
    input5 = w5.get()
    return input1, input2, input3, input4, input5

#Show Image
def whatever():
    plt.close('all')
    x_top    = 0
    x_bottom = 300
    y_left   = 0
    y_right  = 300

    inp = take_values()
    y_top   = inp[0]
    y_bot   = inp[1]
    x_left  = inp[2]
    x_right = inp[3]
    islice  = inp[4]
    print("X Left:", "\t", x_left)
    print("X Right:","\t", x_right)
    print("Y Top:", "\t", "\t", y_top)
    print("Y Bot:", "\t", "\t", y_bot)
    print("Z Level:" "\t", islice)

    X2 = X[isize*islice:isize*islice+isize,:]
    plt.matshow(X2[x_top : x_bottom, y_left : y_right], origin = 'lower')
    plt.gca().xaxis.tick_bottom()
    
    width = x_right - x_left
    length = y_top - y_bot
    print("Width:", "\t", "\t", width)
    print("Length:", "\t", length)
    print("")
    plt.text(-30, 325, "Width: " + str(width))
    plt.text(-30, 310, "Length:" + str(length))

    #plt.hlines(y_bot, 0, 299, 'r')
    #plt.hlines(y_top, 0, 299, 'r')
    #plt.vlines(x_left, 0, 299, 'r')
    #plt.vlines(x_right, 0, 299, 'r')

    plt.hlines(y_bot, x_left, x_right, 'r')
    plt.hlines(y_top, x_left, x_right, 'r')
    plt.vlines(x_left, y_bot, y_top, 'r')
    plt.vlines(x_right, y_bot, y_top, 'r')
    plt.title('Height Level:'+str(islice))
    plt.show()


#Tinker GUI
while 1:
    m = tk.Tk()
    m.title('Area Selection')
    m.configure(bg='tan')

    b = tk.Button(m, width=25, command=m.destroy, bg = "orangered", text='Stop').pack()

    w1 = tk.Scale(m, from_=-1, to=300, length=400, orient=tk.HORIZONTAL,bg= "beige", label="Y Top")
    w1.set(299)
    w1.pack()
    w2 = tk.Scale(m, from_=-1, to=300, length=400, orient=tk.HORIZONTAL,bg = "beige", label="Y Bottom")
    w2.pack()
    w3 = tk.Scale(m, from_=-1, to=300, length=400, orient=tk.HORIZONTAL, bg = "beige", label="X Left")
    w3.pack()
    w4 = tk.Scale(m, from_=-1, to=300, length=400, orient=tk.HORIZONTAL, bg = "beige", label="X Right")
    w4.set(299)
    w4.pack()

    w5 = tk.Scale(m, from_=0, to=299, length=400, orient=tk.HORIZONTAL, bg = "skyblue", label="Height")
    w5.set(1)
    w5.pack()

    s = tk.Button(m, text='Show Area', command=whatever).pack()
    m.mainloop()
    break
