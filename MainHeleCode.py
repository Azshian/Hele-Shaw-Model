#Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
import sys
import time
import os
from PIL import Image, ImageOps
from collections import defaultdict

#Set File
file  = sys.argv[1]
with open(file) as myfile:
    head = [next(myfile) for x in range(5)]
if (head[0][0:5]) == 'ascii':               #check if there's header information
    df = pd.read_csv(file, sep = ' ', header=None, skiprows = 4)
elif (head[0][0] == str(0) or head[0][0] ==  str(1)):
    df = pd.read_csv(file, sep = ' ', header=None)
df = df.iloc[:, :-1]
print( 'File Dimensions:', df.shape[0], 'by', df.shape[1] )
X = df.to_numpy()
del df
isize = len(X[0])

#Extract values from slider
def takeValues():
    input1,input2,input3,input4,input5 = w1.get(),w2.get(),w3.get(),w4.get(),w5.get()
    return input1, input2, input3, input4, input5

#Show Image
def showImage():
    plt.close('all')
    inp = takeValues()
    y_top,y_bot,x_left,x_right = inp[0],inp[1],inp[2],inp[3]
    islice  = inp[4]

    X2 = X[isize*islice:isize*islice+isize,:]
    plt.matshow(X2[0:isize, 0:isize], origin = 'lower')
    plt.gca().xaxis.tick_bottom()
    
    width  = abs(x_right - x_left)
    length = abs(y_top - y_bot)
    print('Z Level:', '\t', islice)
    print('Width:', '\t', '\t', width)
    print('Length:', '\t', length)
    if (width != length):
        print('WARNING: NOT SQUARE')
    print('')
    plt.text(-30, isize+25, 'Width: ' + str(width))
    plt.text(-30, isize+10, 'Length:' + str(length))

    plt.hlines(y_bot,    x_left, x_right-1, 'r', linewidth = 2)
    plt.hlines(y_top-1,  x_left, x_right-1, 'r', linewidth = 2)
    plt.vlines(x_left,   y_bot,  y_top-1,   'r', linewidth = 2)
    plt.vlines(x_right-1,y_bot,  y_top-1,   'r', linewidth = 2)
    plt.title('Height Level:'+str(islice))
    plt.show()

#Cut Image
def cutImage():
    inp = takeValues()
    y_top   = inp[0]
    y_bot   = inp[1]
    x_left  = inp[2]
    x_right = inp[3]
    islice  = inp[4]
    plt.close('all')
    X3 = X[isize*islice:isize*islice+isize,:]

    if (y_top > y_bot) and (x_right > x_left):
        plt.matshow(X3[y_bot: y_top, x_left  : x_right], origin = 'lower')
    if (y_top < y_bot) and (x_right > x_left):
        plt.matshow(X3[y_top: y_bot, x_left  : x_right], origin = 'lower')
    elif (y_top < y_bot) and (x_right < x_left):
        plt.matshow(X3[y_top: y_bot, x_right : x_left], origin = 'lower')
    elif (y_top > y_bot) and (x_right < x_left):
        plt.matshow(X3[y_bot: y_top, x_right : x_left], origin = 'lower')

    plt.gca().xaxis.tick_bottom()
    plt.axis('off')
    plt.show()

def saveImage():
    print('Saving')
    plt.savefig('CroppedImage.png',bbox_inches='tight', pad_inches=0)
    plt.close('all')
    
    img    = Image.open('CroppedImage.png')
    pixels = img.load()
    by_color = defaultdict(int)
    for pixel in img.getdata():
        by_color[pixel] += 1

    for i in range(img.size[0]):
            for j in range(img.size[1]):
                    if pixels[i,j][0] == 68 and pixels[i,j][1] == 1 and pixels[i,j][2] == 84:
                            pixels[i,j] = (0,0,0,255)
                    elif pixels[i,j][0] == 253 and pixels[i,j][1] == 231 and pixels[i,j][2] == 36:
                            pixels[i,j] = (255,255,255,255)
                            
    newimg = ImageOps.expand(img, border=1, fill='black') 
    newimg.show()
    imgsize = newimg.size
    print(imgsize)
    newimg.save("FinalImage.png")
    os.remove('CroppedImage.png')

    
#Tinker GUI
while 1:
    m = tk.Tk()
    m.title('Area Selection')
    m.configure(bg='tan')

    stop_button = tk.Button(m, width=25, command=m.destroy, bg = 'orangered', text='Stop').pack()
    w1 = tk.Scale(m, from_=1, to=isize, length=400, orient=tk.HORIZONTAL, bg= 'beige', label='Y Top')
    w1.set(isize)
    w1.pack()
    w2 = tk.Scale(m, from_=0, to=isize-1, length=400, orient=tk.HORIZONTAL, bg = 'beige', label='Y Bottom')
    w2.pack()
    w3 = tk.Scale(m, from_=0, to=isize-1, length=400, orient=tk.HORIZONTAL, bg = 'beige', label='X Left')
    w3.pack()
    w4 = tk.Scale(m, from_=1, to=isize, length=400, orient=tk.HORIZONTAL, bg = 'beige', label='X Right')
    w4.set(isize)
    w4.pack()
    w5 = tk.Scale(m, from_=0, to=isize-1, length=400, orient=tk.HORIZONTAL, bg = 'skyblue', label='Height')
    w5.set(0)
    w5.pack()
    show_button    = tk.Button(m, width=15, text='Show', command=showImage, bg = 'gold').pack()
    produce_button = tk.Button(m, width=15, text='Cut',  command=cutImage,  bg = 'gold').pack()
    save_button    = tk.Button(m, width=15, text='Save', command=saveImage, bg = 'gold').pack()
    
    m.mainloop()
    break
