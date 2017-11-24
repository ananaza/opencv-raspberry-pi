import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()

	# hue saturation value
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_red = np.array([150,150,50])
	upper_red = np.array([180,255,255])

	#maskataan parametrien perusteella
	mask = cv2.inRange(hsv, lower_red, upper_red)
	res = cv2.bitwise_and(frame, frame, mask = mask)

	kernel = np.ones ((15,15), np.float32)/225
	smoothed = cv2.filter2d(res)

	cv2.imshow("frame", frame)
	cv2.imshow("res", res, -1, ke)
	#cv2.imshow("mask", mask)



	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()

	