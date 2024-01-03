import time

import cv2
import threading as tr
import time as t
from emailing import send_mail

frommail = 'akis.pwdchecker@gmail.com'
tomail = "k.akashkumar@gmail.com"

# send_mail('pfp.png', frommail, tomail)

video = cv2.VideoCapture(0)
time.sleep(1)
while True:
    check, frame = video.read()
    cv2.imshow("MyVideo", frame)

    key = cv2.waitKey(1)
# code here
    if key == ord("q"):
        break

video.release()
