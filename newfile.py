from pytesseract import image_to_string
from PIL import Image
from PIL import ImageEnhance

import smtplib
import getpass
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

#Image resizing based on percentage
basewidth = 500
image = Image.open('slide5.jpg')
width_percent = (basewidth/float(image.size[0]))
height_size = int((float(image.size[1])*float(width_percent)))
image = image.resize((basewidth,height_size), Image.ANTIALIAS)
image.save('new2slide5.jpg')

#greyscale
img1 = Image.open('slide1.jpg').convert('L')
img1.save('newslide1.jpg')

#pictures to try
an = Image.open("coloured-slides-template-background-powerpoint_1.jpg")
en = Image.open("Swiss-Style-Google-Slides-Template.jpg")
on = Image.open("powerpoint-presentation-ma-thesis-defence-6-728.jpg")
me = Image.open("powerpoint-presentation-ma-thesis-defence-13-728.jpg")

yo = Image.open("slide1.jpg")
hi = Image.open("slide2.jpg")
botw = Image.open("slide3.jpg")
hey = Image.open("slide4.jpg")
low = Image.open("slide5.jpg")
newlow = Image.open("newslide5.jpg")
new2low = Image.open("new2slide5.jpg")
new3low = Image.open("new3slide5.jpg")
newyo = Image.open("newslide1.jpg")

#contrast
const = ImageEnhance.Contrast(newyo)
im = const.enhance(1.8)
im.save('new2slide1.jpg')

#pictures
new4low = Image.open("new4slide5.jpg")
new2yo = Image.open("new2slide1.jpg")
#tests for printing to see accuracy

# print(image_to_string(low))
# print " "
# print(image_to_string(newlow))
# print " "
# print(image_to_string(new2low))
# print(image_to_string(an))
#print(image_to_string(new4low))
print(image_to_string(yo))
print ' '
print(image_to_string(newyo))
print " "
print(image_to_string(new2yo))


#read to file
f = open("text.txt","w")
f.write(image_to_string(newyo))
f.write(image_to_string(new2yo))
f.close()


#email
fromaddr = "whutt@csumb.edu"
toaddr = "whutt@csumb.edu"
 
msg = MIMEMultipart()
 
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Text from picture"
 
body = "Here is your text."
 
msg.attach(MIMEText(body, 'plain'))
 
filename = "text.txt"
attachment = open("text.txt", "rb")
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
print ("Sending mail to "+ toaddr)
mypwd = getpass.getpass('Enter your password: ') 
server.login(fromaddr, mypwd)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
print "Message sent"
server.quit()