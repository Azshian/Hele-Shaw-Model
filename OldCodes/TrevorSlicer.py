import numpy as np
import matplotlib.pyplot as plt 
import sys

X = np.loadtxt( sys.argv[1], skiprows=4 )

X2 = np.reshape(X, [400,400,400] , order='F')

plt.matshow(X2[50:250,150:350,30]) 
plt.show()
exit()