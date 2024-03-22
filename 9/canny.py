import cv2
def funcCan (thresh1=0):
    thresh1 = cv2.getTrackbarPos ('Low threshold', 'Canny') 
    thresh2 = cv2.getTrackbarPos ('High threshold', 'Canny') 
    edge = cv2.Canny (img, thresh1, thresh2) 
    cv2.imshow('canny', edge)
    
if __name__ == '__main__':
    original=cv2.imread(r"D:\junior_3\Term2_2566\ComputerVision\1\misc\misc\5.1.09.tiff",1)
    img=original.copy()
    img=cv2. GaussianBlur (img, (5,5), 1.4) 
    cv2.namedWindow('Canny')
    thresh1=100 
    thresh2=1
    cv2.createTrackbar ('Low threshold', 'Canny', thresh1,255, funcCan) 
    cv2.createTrackbar ('High threshold', 'Canny', thresh2, 255, funcCan) 
    funcCan (0)
    cv2.imshow('Frame', original)
    cv2.waitKey (0)
    
cv2.destroyAllWindows()
