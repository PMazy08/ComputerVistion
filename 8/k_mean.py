import numpy as np
import cv2

img = cv2.imread(r'D:\junior_3\Term2_2566\ComputerVision\1\ImageFromOpenCV\opencv-logo-white.png')
z = img.reshape((-1,3))
print(z.shape)

z = np.float32(z)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

k = 4
ret,label,center = cv2.kmeans(z,k,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imshow('original', img)
cv2.imshow('res2', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
