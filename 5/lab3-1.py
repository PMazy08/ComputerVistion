import cv2
import numpy as np

def translation(src, shift, shape_out):
    h, w=src.shape[:2]
    out_img=np.zeros(shape_out,dtype=np.uint8)
    
    for i in range(shift[1],h):
        for j in range(shift[0],w):
            out_img[i,j]=src[i-shift[1], j-shift[0]]
    return out_img

image = cv2.imread(r'D:\junior_3\Term2_2566\ComputerVision\1\misc\misc\4.1.05.tiff')

heigh, width = image.shape[:2]
shift=(100,100)
img_trans=translation(image,shift,image.shape)
cv2.namedWindow('Original',cv2.WINDOW_NORMAL)
cv2.imshow('Original', image)
cv2.namedWindow('Translation',cv2.WINDOW_NORMAL)
cv2.imshow('Translation', img_trans)



T = np.float32([[1, 0, shift[0]], [0, 1, shift[1]]])
img_trans2 = cv2.warpAffine(image, T , (width, heigh))
cv2.imshow('Translation2', img_trans2)

cv2.waitKey()
cv2.destroyAllWindows()