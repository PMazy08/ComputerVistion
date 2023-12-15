import cv2
filename = "ImageFromOpenCV\home.jpg"
# Read file RGB in RGB mode
imRGB = cv2.imread(filename)
cv2.namedWindow('RGB', cv2.WINDOW_NORMAL)
cv2.imshow('RGB', imRGB)
print (imRGB [100, 100,0], imRGB [100, 100, 1], imRGB [100, 100,2]) 
imRGB [100, 100,0] = 0
imRGB [100, 100, 1] = 0
imRGB [100, 100,2] = 0
print (imRGB [100, 100,0], imRGB [100, 100, 1], imRGB [100, 100,2]) 

cv2.namedWindow('RGBnew', cv2.WINDOW_NORMAL)
cv2.imshow('RGBnew', imRGB)
print (imRGB [100, 100,0], imRGB [100, 100, 1], imRGB [100, 100,2]) 
cv2.namedWindow('RGBnew', cv2.WINDOW_NORMAL) 
cv2.imshow('RGBnew', imRGB)

# Read file RGB in grayscale mode 
imGray = cv2.imread(filename, 0) 
cv2.namedWindow('Gray', cv2.WINDOW_NORMAL) 
cv2.imshow('Gray', imGray)
print (imGray.item (100, 100))
imGray.itemset((100, 100),0) 
print (imGray. item (100, 100))
cv2.namedWindow('Graynew', cv2.WINDOW_NORMAL) 
cv2.imshow('Graynew', imGray)

cv2.waitKey(0)
cv2.destroyAllWindows()
