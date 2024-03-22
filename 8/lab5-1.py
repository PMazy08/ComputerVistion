import numpy as np 
import cv2
import matplotlib.pyplot as plt

# Open the image 
img= cv2.imread(r'D:\junior_3\Term2_2566\ComputerVision\1\misc\misc\4.1.05.tiff', 0)
h, w = img.shape
thr=127 #np.mean (img)
# # Prewitt Operator
# hx = np.array([[-1, 0, 1],
#                [-1, 0, 1],
#                [-1, 0, 1]])
# hy = hx.T


# Sobel’s Operator
hx = np.array([[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]])

hy = np.array([[-1, -2, -1],
               [0, 0, 0],
               [1, 0, 1]])

Gx = np.zeros((h, w))
Gy = np. zeros ((h, w))
Gxy = np.zeros((h, w)) 
G = np.zeros((h, w)) 
theta = np.zeros((h, w)) 
for i in range (1, h - 1): 
    for j in range (1, w - 1):
        Gx.itemset((i,j),np.sum(hx*img[i-1:i+2,j-1:j+2]))
        Gy.itemset((i,j),np.sum(hy*img[i-1:i+2,j-1:j+2]))
        # Edge Magnitude
        Gxy.itemset((i,j), np.sqrt(Gx[i, j]**2 + Gy[i, j]**2.0))
        
        # check grandient with threshold
        if Gxy.item (i,j)>thr: G.itemset((i,j), 255) 
        else: G.itemset((i,j),0)
        
# direction
theta = np.arctan2 (Gy, Gx) * (180/np.pi)%180

plt.figure (2, figsize=(12,7))
plt.subplot (231)
plt.title("house"), plt.axis ('off')
plt.imshow(img,cmap='gray')
plt.subplot (232)
plt.title('Prewitt Gx'), plt.axis ('off')
plt.imshow (Gx, cmap='gray')
plt.subplot(233), plt.axis('off')
plt.title('Prewitt Gy')
plt.imshow (Gy, cmap='gray')
plt.subplot (234), plt.axis ('off') 
plt.title('Prewitt Gradient')
plt.imshow (Gxy, cmap='gray') 
plt.subplot (235), plt.axis ('off')
plt.title('Edge')
plt.imshow (G, cmap='gray')

plt.imsave('house-prewitt-1.png', Gxy, cmap='gray')
plt.show()


# ////////////////////////////////////////////

# define images with Os
Gxy = np.zeros((h, w), dtype=np. float64) 
G = np.zeros((h, w), dtype=np. uint8) 
theta = np. zeros ((h, w))

# Gradient
hx = np.array([[1,1,1], [0,0,0], [-1,-1,-1]]) 
hy = np.array([[-1,0,1], [-1,0,1], [-1,0,1]]) 
Gx = cv2.filter2D (img, cv2.CV_64F, hx)
Gy = cv2.filter2D (img, cv2.CV_64F, hy)
#Edge Magnitude
Gxy = np.sqrt(Gx**2 + Gy**2)
# direction
theta=np.arctan2 (Gy, Gx) * (180/np.pi)%180
# check grandient with threshold
G = np.array([[255 if g>thr else 0 for g in Gxy[j]] 
              for j in range (h)], dtype=np. uint8)

plt.figure (2, figsize=(12,7))
plt.subplot (231)
plt.title("house"), plt.axis ('off')
plt.imshow(img,cmap='gray')
plt.subplot (232)
plt.title('Prewitt Gx'), plt.axis ('off')
plt.imshow (Gx, cmap='gray')
plt.subplot(233), plt.axis('off')
plt.title('Prewitt Gy')
plt.imshow (Gy, cmap='gray')
plt.subplot (234), plt.axis ('off') 
plt.title('Prewitt Gradient')
plt.imshow (Gxy, cmap='gray') 
plt.subplot (235), plt.axis ('off')
plt.title('Edge')
plt.imshow (G, cmap='gray')

plt.imsave('house-prewitt-1.png', Gxy, cmap='gray')
plt.show()