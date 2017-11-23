import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()

	laplacian = cv2.Laplacian(frame, cv2.CV_64F)


	cv2.imshow("original", frame)
	cv2.imshow("laplacian", laplacian)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()

	
