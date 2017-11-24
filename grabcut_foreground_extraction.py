#https://docs.opencv.org/trunk/d8/d83/tutorial_py_grabcut.html

import cv2
import numpy as np
import matplotlib.pyplot as plt 

img = cv2.imread("grabcut_foreground_extraction.jpg")
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)


rect = (1500, 1500, 200, 200)

# grabcut
cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where(np.logical_or(mask==2,mask==0), 0, 1).astype("uint8")
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show() 