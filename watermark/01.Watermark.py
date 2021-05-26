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

# def save4Images(img):
    


def applyWatermark(imgName):
    # im1 = Image.open(resize_folder_output_path+'/'+imgName)
    # watermark = Image.open('21.gif')
    # im1 =  im1.paste(watermark)
    # im1.save('abc.jpg')
    # return img
    im1 = Image.open(resize_folder_output_path+'/'+imgName)
    imTemp = Image.open(resize_folder_output_path+'/'+imgName)
    im2 = Image.open('33.png')
    ximg,yimg=im1.size[0],im1.size[1]
    ximg2,yimg2=im2.size[0],im2.size[1]

    margin = 35

    areaBox = (margin, margin)  
    im1.paste(im2,areaBox,im2)
    im1.save(resize_folder_output_path+'/'+imgName+"a.jpg")

    im1 = Image.open(resize_folder_output_path+'/'+imgName)
    areaBox = (margin, yimg - margin - yimg2)  
    im1.paste(im2,areaBox,im2)
    im1.save(resize_folder_output_path+'/'+imgName+"b.jpg")

    im1 = Image.open(resize_folder_output_path+'/'+imgName)
    areaBox = (ximg - margin - ximg2, margin)  
    im1.paste(im2,areaBox,im2)
    im1.save(resize_folder_output_path+'/'+imgName+"c.jpg")


    im1 = Image.open(resize_folder_output_path+'/'+imgName)
    areaBox = (ximg - margin - ximg2, yimg - margin - yimg2)  
    im1.paste(im2,areaBox,im2)
    im1.save(resize_folder_output_path+'/'+imgName+"d.jpg")

# 1. Resize Orignal Image ........................................

ctr = 0
for img_name in imageList:
    ctr = ctr + 1
    print("Processing "+str(ctr)+" : "+str(img_name))
    image = Image.open(resize_folder_path+'/'+img_name)
    # image = getResizedValues(image)  
    image = getResizedValues(image)
    image.save(resize_folder_output_path+'/'+img_name, 'JPEG', quality=quality_val)
    applyWatermark(img_name)




# 2. Resize logo according to the image dimenstoins
# 3. Lower the image qulaty value for save
# 4. Run program in loop for all images in X folder generates output in X_resize folder