from pytesseract import image_to_string
from PIL import Image
from PIL import ImageEnhance
#Image resizing
#not liking this one it stretches
"""
img = Image.open("slide5.jpg") # image extension *.png,*.jpg
new_width  = 600
new_height = 600
img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save("newslide5.jpg") # format may what u want ,*.png,*jpg,*.gif
"""
#Image resizing based on percentage

#thinking this one
basewidth = 500
image = Image.open('slide7.png')
width_percent = (basewidth/float(image.size[0]))
height_size = int((float(image.size[1])*float(width_percent)))
image = image.resize((basewidth,height_size), Image.ANTIALIAS)
image.save('new2slide7.jpg')

#greyscale
img1 = Image.open('new2slide7.jpg').convert('L')
img1.save('new3slide7.jpg')

#pictures to try
#an = Image.open("coloured-slides-template-background-powerpoint_1.jpg")
#en = Image.open("Swiss-Style-Google-Slides-Template.jpg")
#on = Image.open("powerpoint-presentation-ma-thesis-defence-6-728.jpg")
#me = Image.open("powerpoint-presentation-ma-thesis-defence-13-728.jpg")
#yo = Image.open("slide1.jpg")
#hi = Image.open("slide2.jpg")
#botw = Image.open("slide3.jpg")
#hey = Image.open("slide4.jpg")
#low = Image.open("slide5.jpg")
#newlow = Image.open("newslide5.jpg")
#new2low = Image.open("new2slide5.jpg")
#new3low = Image.open("new3slide5.jpg")
txttest = Image.open("new3slide7.jpg")

#enchancing
const = ImageEnhance.Contrast(txttest)
im = const.enhance(2.5)
#im.save('new4slide5.jpg')
#new4low = Image.open("new4slide5.jpg")

#tests for printing to see accuracy
# print(image_to_string(low))
# print " "
# print(image_to_string(newlow))
# print " "
# print(image_to_string(new2low))
# print(image_to_string(an))
print(image_to_string(txttest))

#read to file
f = open("text.txt","w")
f.write(image_to_string(txttest))
f.close()