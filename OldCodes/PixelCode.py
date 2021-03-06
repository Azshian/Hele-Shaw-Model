#Libraries
from PIL import Image, ImageOps
from collections import defaultdict

img    = Image.open('CroppedImage.png')
pixels = img.load()
s = img.size

by_color = defaultdict(int)
for pixel in img.getdata():
    by_color[pixel] += 1
print(by_color)

counter_1 = 0
counter_2 = 0
for i in range(img.size[0]):
	for j in range(img.size[1]):
		if pixels[i,j][0] == 68 and pixels[i,j][1] == 1 and pixels[i,j][2] == 84:
			counter_1 += 1
			pixels[i,j] = (0,0,0,255)
		elif pixels[i,j][0] == 253 and pixels[i,j][1] == 231 and pixels[i,j][2] == 36:
			counter_2 += 1
			pixels[i,j] = (255,255,255,255)
newimg = ImageOps.expand(img, border=1, fill='black') 
newimg.show()

imgsize = newimg.size
print(imgsize)
newimg.save("FinalImage.png")
