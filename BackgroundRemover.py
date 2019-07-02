#Import Libraries
import sys 
from PIL import Image

#Setup System Arguments
filename = str(sys.argv[1])
save     = int(sys.argv[2])

#Open Image and Crop out top and left sides of background
img = Image.open(filename)
pixels = img.load()
search = False
for i in range(img.size[0]):
        for j in range(img.size[1]): 
            if search == False:
                if 200 <= pixels[i,j][0] <= 255 and 200 <= pixels[i,j][1] <= 255 and 0 <= pixels[i,j][2] <= 100:
                    left_side = i
                    top_side = j
                    search = True   
                elif 60 <= pixels[i,j][0] <= 150 and 0 <= pixels[i,j][1] <= 10 and 75 <= pixels[i,j][2] <= 125:
                    left_side = i
                    top_side = j
                    search = True
  
crop_img = img.crop((left_side+1, top_side+1, img.size[0], img.size[1]))    
crop_pixels = crop_img.load()

#Crop out right and bottom sides of background
search = False
j = 0
for i in range(crop_img.size[0]):
    if search == False:
        if 200 <= crop_pixels[i,j][0] <= 255 and 200 <= crop_pixels[i,j][1] <= 255 and 200 <= crop_pixels[i,j][2] <= 255:
            right_side = i
            search = True
        elif 0 <= crop_pixels[i,j][0] <= 30 and 0 <= crop_pixels[i,j][1] <= 30 and 0 <= crop_pixels[i,j][2] <= 30:
            right_side = i
            search = True
            
search = False
i = 0
for j in range(crop_img.size[1]):
    if search == False:   
        if 200 <= crop_pixels[i,j][0] <= 255 and 200 <= crop_pixels[i,j][1] <= 255 and 200 <= crop_pixels[i,j][2] <= 255:
            bottom_side = j
            search = True
        elif 0 <= crop_pixels[i,j][0] <= 30 and 0 <= crop_pixels[i,j][1] <= 30 and 0 <= crop_pixels[i,j][2] <= 30:
            bottom_side = j
            search = True
recrop_img = crop_img.crop((0, 0, right_side-1, bottom_side-1))    


#Show image and print size
print("Width: ", recrop_img.size[0], " Length: ", recrop_img.size[1])
recrop_img.show()

#Save File
if save == 1:
    recrop_img.save('FirstCrop.jpeg')
