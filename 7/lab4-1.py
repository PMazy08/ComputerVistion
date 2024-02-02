import cv2
import numpy as np
from matplotlib import pyplot as plt
file=r'D:\junior_3\Term2_2566\ComputerVision\1\Image4Otsu\sudoku.png'

img=cv2.imread(file, 0)
ret, otsu = cv2.threshold (img, 0, 255, cv2.THRESH_OTSU)

blur=cv2.blur(img, (3,3))
mean=cv2.adaptiveThreshold(blur, 10, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 7, 7)
niblack = cv2.ximgproc.niBlackThreshold (img, 255, cv2.THRESH_BINARY, 65,-0.2, cv2.ximgproc. BINARIZATION_NIBLACK) 

# //////////////////////////////////

gaussC=cv2.GaussianBlur(img, (3,3), 7)
gauss=cv2.adaptiveThreshold(gaussC, 10, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 7)
sauvola = cv2.ximgproc.niBlackThreshold (img, 255, cv2.THRESH_BINARY,65,-0.5,cv2.ximgproc. BINARIZATION_SAUVOLA)


fig, axs = plt.subplots(2, 5, figsize=(15, 7))

axs[0, 0].imshow(img, 'gray')
axs[0, 0].set_title("Original")
axs[0, 0].axis("off")

axs[0, 1].imshow(blur, 'gray')
axs[0, 1].set_title("Blur")
axs[0, 1].axis("off")

axs[0, 2].imshow(otsu, 'gray')
axs[0, 2].set_title("Otsu")
axs[0, 2].axis("off")

axs[0, 3].imshow(mean, 'gray')
axs[0, 3].set_title("Mean")
axs[0, 3].axis("off")

axs[0, 4].imshow(niblack, 'gray')
axs[0, 4].set_title("Niblack")
axs[0, 4].axis("off")

# /////////////////////////////////////

axs[1, 0].imshow(img, 'gray')
axs[1, 0].set_title("Original")
axs[1, 0].axis("off")

axs[1, 1].imshow(gaussC, 'gray')
axs[1, 1].set_title("Gaussian Blur")
axs[1, 1].axis("off")

axs[1, 2].imshow(otsu, 'gray')
axs[1, 2].set_title("Otsu")
axs[1, 2].axis("off")

axs[1, 3].imshow(gauss, 'gray')
axs[1, 3].set_title("Gaussian")
axs[1, 3].axis("off")

axs[1, 4].imshow(sauvola, 'gray')
axs[1, 4].set_title("Sauvola")
axs[1, 4].axis("off")

plt.show()