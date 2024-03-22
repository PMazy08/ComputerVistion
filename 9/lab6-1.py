import cv2
import numpy as np

img=cv2.imread(r'D:\junior_3\Term2_2566\ComputerVision\1\Image4Otsu\text-line.jpg',0)
thr, bin_img = cv2.threshold(img,0,1, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

cv2.namedWindow('Binary', cv2.WINDOW_NORMAL) 
cv2.imshow('Binary', bin_img*255)

kernel = np.ones((3,3), np.uint8)
print(kernel)

dst_dilate=cv2.dilate (bin_img, kernel, iterations=1) 
print(dst_dilate)
cv2.namedWindow('Dilation', cv2.WINDOW_NORMAL) 
cv2.imshow('Dilation', dst_dilate*255)


dst_erode=cv2.erode (bin_img,kernel, iterations=1)
print(dst_erode)
cv2.namedWindow('Erosion', cv2.WINDOW_NORMAL)
cv2.imshow('Erosion',dst_erode*255)

cv2.waitKey(0)
cv2.destroyAllWindows()