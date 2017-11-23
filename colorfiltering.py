import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	# hue saturation value
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_red = np.array([150,150,50])
	upper_red = np.array([180,255,150])

	#maskataan parametrien perusteella
	mask = cv2.inRange(hsv, lower_red, upper_red)
	res = cv2.bitwise_and(frame, frame, mask = mask)

	cv2.imshow("frame", frame)
	cv2.imshow("res", res)
	cv2.imshow("mask", mask)



	if(cv2.waitKey(0)):
		break

cv2.destroyAllWindows()
cap.release()

	