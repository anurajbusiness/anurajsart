from PIL import Image, ImageDraw, ImageFont
import os
# create Image object with the input image

# resize_folder_path = 'C:/Users/tanan/Google Drive/Insta Pics/1RawPics'
resize_folder_path = '2021'
resize_folder_output_path = 'Output'
quality_val = 35
rez4k = 2163

def getResizedValues(tempImage):
    x,y=tempImage.size[0],tempImage.size[1]
    if x < y:
        y = y/x*rez4k
        x = rez4k
    else:
        x = x/y*rez4k
        y = rez4k
    return tempImage.resize((int(x), int(y)), Image.ANTIALIAS)

# def getResizedValues(tempImage):
#     aspectRatio = 2.01653333333
#     aspectWidth = rez4k/aspectRatio
#     tempImage=getResizedValues(tempImage)
#     x,y=tempImage.size[0],tempImage.size[1]
#     print(x,y)

#     #Give Top Left Corner
#     left = (rez4k-aspectWidth)/2
#     top = 0
    
#     #Give Bottom Right Corner
#     right = left + aspectWidth
#     bottom = rez4k
    
#     tempImage = tempImage.crop((int(left), int(top), int(right), int(bottom)))
#     return tempImage

imageList = [];
for file in os.listdir(resize_folder_path):
    if file.endswith(".jpg") or file.endswith(".jpeg"):
        # print("Filename : ", file)
        # print(os.path.join("/mydir", file))
        imageList.append(file)

# 1. Resize Orignal Image ........................................

ctr = 0
for img_name in imageList:
    ctr = ctr + 1
    print("Processing "+str(ctr)+" : "+str(img_name))
    image = Image.open(resize_folder_path+'/'+img_name)
    # image = getResizedValues(image)  
    image = getResizedValues(image)
    image.save(resize_folder_output_path+'/'+img_name, 'JPEG', quality=quality_val)





# 2. Resize logo according to the image dimenstoins
# 3. Lower the image qulaty value for save
# 4. Run program in loop for all images in X folder generates output in X_resize folder