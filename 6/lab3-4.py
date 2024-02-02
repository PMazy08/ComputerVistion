import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r'D:\junior_3\Term2_2566\ComputerVision\1\Image4Otsu\sudoku.png') 
rows, cols = img.shape[0], img.shape [1]

#image translation
M = np.float32 ([[1,0,100], [0,1,50]])
trans = cv2.warpAffine (img, M, (cols, rows))

#image rotation
M = cv2.getRotationMatrix2D (((cols-1)/2.0, (rows-1)/2.0), 60,1) 
rot = cv2.warpAffine (img, M, (cols, rows))

rot1 = cv2.rotate (img, cv2.ROTATE_90_CLOCKWISE)
rot2 = cv2.rotate (img, cv2.ROTATE_180)
rot3 = cv2.rotate (img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# affine tranformation
pts1 = np.float32 ([[50,50], [200, 50], [50,200]]) 
pts2 = np.float32 ([[10,100], [200, 50], [100,250]]) 
M = cv2.getAffineTransform (pts1,pts2)
aff= cv2.warpAffine (img, M, (cols, rows))

# Perspective Transformation
pts1 = np.float32 ([[73,85], [493,68], [35,515], [522,523]]) 
pts2 = np.float32 ([[0,0], [300,0], [0,300], [300, 300]])
M = cv2.getPerspectiveTransform (pts1,pts2)
perspec = cv2.warpPerspective (img, M, (300,300))

# flip
flip1 = cv2.flip(img, 0)
flip2 = cv2.flip(img, 1)


plt.subplot(431), plt.imshow(img) 
plt.title("Original"), plt.axis ("off") 

plt.subplot(432), plt.imshow(trans) 
plt.title("Translation"), plt.axis ("off") 

plt.subplot(433), plt.imshow(rot) 
plt.title("Rotation"), plt.axis ("off")

plt.subplot(435), plt.imshow(aff)
plt.title("Affine"), plt.axis("off") 

plt.subplot(436), plt.imshow (perspec) 
plt.title("Perspective"), plt.axis ("off")

plt.subplot(4,3,7), plt.imshow (rot1) 
plt.title("ROTATE_90_CLOCKWISE"), plt.axis ("off")
plt.subplot(4,3,8), plt.imshow (rot2) 

plt.title("ROTATE_180"), plt.axis ("off")

plt.subplot(4,3,9), plt.imshow (rot3) 
plt.title("ROTATE_90_COUNTERCLOCKWISE"), plt.axis ("off")

plt.subplot(4,3,10), plt.imshow (flip1) 
plt.title("Flip X"), plt.axis ("off")

plt.subplot(4,3,11), plt.imshow (flip2) 
plt.title("Flip Y"), plt.axis ("off")




plt.show()

