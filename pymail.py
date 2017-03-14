# email test file

import smtplib
import getpass
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
 
 
myemail = "gorozco@csumb.edu"     # user email address
recip = "gorozco@csumb.edu"       # recipients email address
msg = MIMEMultipart()
msg['From'] = myemail           
msg['To'] = recip
msg['Subject'] = "SUBJECT OF THE MAIL"     # Subject line
 
body = "YOUR MESSAGE HERE"                # message on the e-mail it self
msg.attach(MIMEText(body, 'plain'))

######## Attaching image file ######     


filename = "Amaranth.png"                 #file name to be attached, used for email description
attachment = open("Amaranth.png", "rb")   #opening file from and saving it to attachment, actual file directory. 
 
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)

######################################







try:
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.ehlo()
except:
  print("Something went wrong")


# make connection secure
server.starttls()
print ("Sending mail to "+ recip)

mypwd = getpass.getpass('Enter your password: ') 
server.login(myemail, mypwd)

msg = msg.as_string()

server.sendmail(myemail, recip, msg)
server.quit()