#Libraries
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import os

#Set File
user = 'Adriann Liceralde'
file = 'F42A.dat' 
os.chdir('C:\\Users\\'+str(user)+'\\Desktop\\Repository\\HeleShaw\\CoreSamples')
isize = 300 #Do Not Change from 300
X = np.loadtxt(file, skiprows = 4)

#Extract values from slider
def take_values():
    input1,input2,input3,input4,input5 = w1.get(),w2.get(),w3.get(),w4.get(),w5.get()
    return input1, input2, input3, input4, input5

#Show Image
def whatever():
    plt.close('all')
    inp = take_values()
    y_top,y_bot,x_left,x_right = inp[0],inp[1],inp[2],inp[3]
    islice  = inp[4]
    print('X Left:', '\t',  x_left)
    print('X Right:','\t',  x_right)
    print('Y Top:', 2*'\t', y_top)
    print('Y Bot:', 2*'\t', y_bot)
    print('Z Level:', '\t', islice)

    X2 = X[isize*islice:isize*islice+isize,:]
    plt.matshow(X2[0:300, 0:300], origin = 'lower')
    plt.gca().xaxis.tick_bottom()
    
    width  = x_right - x_left
    length = y_top - y_bot
    print('Width:', '\t', '\t', width)
    print('Length:', '\t', length)
    print('')
    plt.text(-30, 325, 'Width: ' + str(width))
    plt.text(-30, 310, 'Length:' + str(length))

    plt.hlines(y_bot,    x_left, x_right-1, 'r', linewidth = 2)
    plt.hlines(y_top-1,  x_left, x_right-1, 'r', linewidth = 2)
    plt.vlines(x_left,   y_bot,  y_top-1,   'r', linewidth = 2)
    plt.vlines(x_right-1,y_bot,  y_top-1,   'r', linewidth = 2)
    plt.title('Height Level:'+str(islice))
    plt.show()

#Cut Image
def finalize():
    inp = take_values()
    y_top   = inp[0]
    y_bot   = inp[1]
    x_left  = inp[2]
    x_right = inp[3]
    islice  = inp[4]

    plt.close('all')
    X3 = X[isize*islice:isize*islice+isize,:]
    plt.matshow(X3[y_bot: y_top, x_left : x_right], origin = 'lower')
    plt.gca().xaxis.tick_bottom()
    plt.axis('off')
    plt.show()

#Tinker GUI
while 1:
    m = tk.Tk()
    m.title('Area Selection')
    m.configure(bg='tan')

    stop_button = tk.Button(m, width=25, command=m.destroy, bg = 'orangered', text='Stop').pack()
    w1 = tk.Scale(m, from_=0, to=300, length=400, orient=tk.HORIZONTAL,bg= 'beige', label='Y Top')
    w1.set(300)
    w1.pack()
    w2 = tk.Scale(m, from_=0, to=300, length=400, orient=tk.HORIZONTAL,bg = 'beige', label='Y Bottom')
    w2.pack()
    w3 = tk.Scale(m, from_=0, to=300, length=400, orient=tk.HORIZONTAL, bg = 'beige', label='X Left')
    w3.pack()
    w4 = tk.Scale(m, from_=0, to=300, length=400, orient=tk.HORIZONTAL, bg = 'beige', label='X Right')
    w4.set(300)
    w4.pack()
    w5 = tk.Scale(m, from_=0, to=298, length=400, orient=tk.HORIZONTAL, bg = 'skyblue', label='Height')
    w5.set(0)
    w5.pack()
    show_button = tk.Button(m, width=15, text='Show Area', command=whatever, bg = 'gold').pack()
    produce_button = tk.Button(m, width=15, text = 'Cut', command = finalize, bg = 'gold').pack()
    
    m.mainloop()
    break
