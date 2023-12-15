import cv2
import numpy as np

# Average filter
filename= "NoiseImg/airplane_sp.png"
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
cv2.imshow('Grayscale', img)
w, h = img.shape

out1 = np.zeros(img.shape, dtype=np.uint8)
for i in range(1,h-1):
    for j in range(1, w-1):
        out1.itemset((i,j), np.median(img[i-1:i+2,j-1:j+2]))
cv2.imshow('Medain 3x3', out1)

out2 = np.zeros(img.shape, dtype=np.uint8)
for i in range(2,h-2):
    for j in range(2, w-2):
        out2.itemset((i,j), np.median(img[i-2:i+3,j-2:j+3]))
cv2.imshow('Medain 5x5', out2)

out3 = np.zeros(img.shape, dtype=np.uint8)
for i in range(3,h-3):
    for j in range(3, w-3):
        out3.itemset((i,j), np.median(img[i-3:i+4,j-3:j+4]))
cv2.imshow('Medain 7x7', out3)


cv2.waitKey(0)
cv2.destroyAllWindows()




cv2.waitKey(0)
cv2.destroyAllWindows()