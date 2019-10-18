import numpy as np
import cv2

cap =  cv2.VideoCapture(1)
hand_cascade = cv2.CascadeClassifier('hand.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
fist_cascade = cv2.CascadeClassifier('fist.xml')
palm_cascade = cv2.CascadeClassifier('palm.xml')

while (True):

    ret, img=cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    fists = fist_cascade.detectMultiScale(gray, 1.3, 5)
        
    for (x,y,w,h) in fists:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
    
    
    