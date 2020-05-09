#Import Libraries
import sys 
from PIL import Image

#Setup System Arguments
filename = str(sys.argv[1])

left_axis = int(sys.argv[2])
top_axis = int(sys.argv[3])
right_axis = int(sys.argv[4])
bottom_axis = int(sys.argv[5])

save = int(sys.argv[6])

#Open Image and Crop out
img = Image.open(filename)
pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]): 
        if 180 <= pixels[i,j][0] <= 255 and 180 <= pixels[i,j][1] <= 255 and 0 <= pixels[i,j][2] <= 255:
            pixels[i,j] = (255,255,255,255)
        
        elif 200 <= pixels[i,j][0] <= 255 and 150 <= pixels[i,j][1] <= 180 and 0 <= pixels[i,j][2] <= 150:
            pixels[i,j] = (255,255,255,255)

for i in range(img.size[0]):
    for j in range(img.size[1]): 
        if 0 <= pixels[i,j][0] <= 180 and 0 <= pixels[i,j][1] <= 180 and 0 <= pixels[i,j][2] <= 255:
            pixels[i,j] = (0, 0, 0, 255)
        elif 200 <= pixels[i,j][0] <= 255 and 150 <= pixels[i,j][1] <= 180 and 150 <= pixels[i,j][2] <= 255:
            pixels[i,j] = (0, 0, 0, 255)

recrop_img = img.crop((left_axis, top_axis, right_axis, bottom_axis))


#Show Image and Print size
print("Width: ", recrop_img.size[0], " Length: ", recrop_img.size[1])
recrop_img.show()

#Save File
if save == 1:
    recrop_img.save("NetworkSlice.png")
    
    


