import cv2
import numpy as np

img1 = cv2.imread("image1.jpg")
img2 = cv2.imread("logo.jpg")
#img2 = cv2.imread("image2.jpg")

rows, cols, channels = img2.shape

#region of image
roi = img1[0:rows, 0:cols]

#luodaan logosta harmaasavyinen
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

##maskaus - jos pixeliarvo on yli 220 niin se muutetaan 255
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

#https://docs.opencv.org/3.2.0/d0/d86/tutorial_py_image_arithmetics.html
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow("mask",mask_inv)
cv2.imshow("mask_inv", mask_inv)
cv2.imshow("img1_bg", img1_bg)
cv2.imshow("img2_fg", img2_fg)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

#alkutestailua
#add = img1 + img2
#add = cv2.add(img1, img2)
#Suluissa kuva, kuvanPaino, kuva2, kuvan2Paino, gamma)
#weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

