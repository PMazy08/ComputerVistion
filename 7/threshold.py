import cv2
import numpy as np
import matplotlib.pyplot as plt
image1 = cv2.imread(r'D:\junior_3\Term2_2566\ComputerVision\1\Image4Otsu\Scan0036.TIF')
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

ret, thr1 = cv2. threshold (img, 127, 255, cv2.THRESH_BINARY) 
ret, thr2 = cv2.threshold (img, 127, 255, cv2.THRESH_BINARY_INV) 
ret, thr3 = cv2.threshold (img, 150, 255, cv2.THRESH_TRUNC)  
ret, thr4 = cv2.threshold (img, 150, 255, cv2.THRESH_TOZERO)
ret, thr5 = cv2.threshold (img, 150, 255, cv2.THRESH_TOZERO_INV) 
ret, thr6 = cv2.threshold (img, 0, 255, cv2.THRESH_OTSU)
print (ret)
ret, thr7 = cv2. threshold (img, 0, 255, cv2.THRESH_TOZERO+cv2.THRESH_OTSU)

# De-allocate any associated memory usage
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO INV', 'Otsu', 'TOZERO+OTSU']
    
images = [img, thr1, thr2, thr3, thr4, thr5, thr6, thr7]

for i in range(6):
    plt.subplot (2,4,i+1), plt.imshow(images [i], 'gray') 
    plt.title(titles [i]),plt.xticks([]), plt.yticks([])
plt.show()
