import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as grid 

img = cv2.imread(r'D:\junior_3\Term2_2566\ComputerVision\1\ImageFromOpenCV\orchid.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

near_img = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_NEAREST)

bilinear_img = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_LINEAR)

bicubic_img = cv2.resize(img,(img.shape[0]*2,img.shape[1]*2),interpolation= cv2.INTER_CUBIC)

plt.figure(1)
grid.GridSpec(3,6)
plt.subplot2grid((3,6),(0,2)),plt.imshow(img)
plt.title("Original Image"),plt.axis('off')

plt.subplot2grid((3,6),(1,0),colspan=2,rowspan=2)
plt.imshow(near_img),plt.title("Near Image"),plt.axis('off')

plt.subplot2grid((3,6),(1,2),colspan=2,rowspan=2)
plt.imshow(bilinear_img),plt.title("bilinear Image"),plt.axis('off')

plt.subplot2grid((3,6),(1,4),colspan=2,rowspan=2)
plt.imshow(bicubic_img),plt.title("bicubic Image"),plt.axis('off')
plt.show()