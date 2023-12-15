import cv2
filename = "ImageFromOpenCV\home.jpg"
# Read file RGB in RGB mode 
imRGB = cv2.imread(filename)
cv2.namedWindow('RGB', cv2.WINDOW_NORMAL)
cv2.imshow('RGB', imRGB)
dim = imRGB. shape
height = imRGB.shape[0] 
width = imRGB. shape [1] 
channel = imRGB. shape [2]
##width, height, channel=imRGB. shape
print (dim)
print (height, width, channel) 
print (imRGB.size)
print (imRGB.ndim)
# Read file RGB in grayscale mode 
imGray = cv2.imread(filename, 0)
cv2.namedWindow('Gray', cv2.WINDOW_NORMAL)
cv2.imshow('Gray', imGray)
                
print (imGray.shape) 
print (imGray.size)
print (imGray.ndim)
print (imGray.itemsize)

cv2.waitKey (0)
cv2.destroyAllWindows ()
