import numpy as np
import cv2 

filename =r"NoiseImg\airplane.tiff"
img =cv2.imread(filename,cv2.IMREAD_GRAYSCALE)

kernel = np.array([[0,1,0],
                   [1,-4,1],
                   [0,1,0]])
dst =cv2.filter2D(img,-1,kernel)


kernel2 = np.array([[-1,-1,-1],
                    [-1,8,-1],
                    [-1,-1,-1]])
dst2 =cv2.filter2D(img,-1,kernel2)



cv2.imshow('Filtered image',dst)
cv2.imshow('Filtered image2',dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()