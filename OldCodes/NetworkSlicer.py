#Import Libraries
import sys 
import numpy as np
import matplotlib.pyplot as plt 

#Setup File Viewing
isize = 300 #Do Not Change from 300
X = np.loadtxt(sys.argv[1], skiprows = 4)
islice = int(sys.argv[2])
X2 = X[isize*islice:isize*islice+isize,:]

#System Arguments for file
x_top    = int(sys.argv[3])
x_bottom = int(sys.argv[4])
y_left   = int(sys.argv[5])
y_right  = int(sys.argv[6])

#Show image
plt.matshow(X2[x_top : x_bottom, y_left : y_right])
plt.show()
