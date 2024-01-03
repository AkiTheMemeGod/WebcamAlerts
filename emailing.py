import smtplib as sm
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os
import time


def send_mail(ImgFileName, From, To):
    with open(ImgFileName, 'rb') as f:
        img_data = f.read()

    msg = MIMEMultipart()
    msg['Subject'] = 'Movement detected !'
    msg['From'] = 'e@mail.cc'
    msg['To'] = 'e@mail.cc'

    text = MIMEText(f"Movement detected in webcam at {time.strftime('%I:%M %p - %d %B %Y')}")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)

    s = sm.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("akis.pwdchecker@gmail.com", "tjjqhaifdobuluhg")
    s.sendmail(From, To, msg.as_string())
    s.quit()



