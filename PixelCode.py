#Libraries
import os
from PIL import Image
from collections import defaultdict
import numpy

#Set File
#user = 'adria'
user = 'Adriann Liceralde'
os.chdir('C:\\Users\\'+str(user)+'\\Desktop\\Repository\\HeleShaw\\CoreSamples')
img = Image.open('CroppedImage.png')
pixels = img.load()
s = img.size
img
