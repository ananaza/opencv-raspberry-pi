import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# https://docs.opencv.org/3.3.0/db/d5c/tutorial_py_bg_subtraction.html
fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
 
    cv2.imshow('frame',frame)
    cv2.imshow('fgmask',fgmask)

    # lopetetaan nappulalla esc
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    

cap.release()
cv2.destroyAllWindows()