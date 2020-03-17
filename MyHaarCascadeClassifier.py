# File name: MyHaarCascadeClassifier.py
# Python version: Python 3.7.0
# Author: Roman Mukosieiev
# Program Description: Tracks my face using the deep learning algorithm Haar Cascade.
#                      The dataset contained 324 pictures of my face(positive),
#                      as well as 3,184 pictures that did not contain my face (negative).
#
# Input:        1) Video from the frontal web camera.
#
# Processing:   1) Turn on the camera and gather the video from it.
#               2) Convert the video to black and white.
#               3) Detect the objects on the videostream using the trained image classifier
#               4) Once the object is detected, draw the square around the detected object, and write "Roman".
#
# Output:       1) The detected object.

import numpy as np
import cv2
# CHANGE THE ROUTE ACCORDING TO YOUR MACHINE.
my_cascade = cv2.CascadeClassifier('C:\\Users\\Roman\\Desktop\\Python\\cv2\\myhaar.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detection = my_cascade.detectMultiScale(gray,4,10)
    for (x, y, w, h) in detection:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
        cv2.putText(img, "Roman", (x, y), cv2.FONT_HERSHEY_DUPLEX, 0.9, (0, 255, 255), 1)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()