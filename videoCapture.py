import cv2
import numpy as np

#cap = cv2.VideoCapture("/home/pi/Desktop/output.jpg")
cap = cv2.VideoCapture(0)

if cap.isOpened() == False:
    print ("VideoCapture failed")

while True:
    ret, frame = cap.read()
    if ret == False:
        print("Frame is empty")
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



