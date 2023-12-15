import cv2 

filename = "ImageFromOpenCV\home.jpg"

imgRGB  = cv2.imread(filename)
cv2.namedWindow('RGB', cv2.WINDOW_NORMAL)
cv2.imshow('RGB', imgRGB)

# RGb 2 Grayscale
imgGray = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2GRAY)
cv2.namedWindow('Gray', cv2.WINDOW_NORMAL)
cv2.imshow('Gray', imgGray)

# Grayscale 2 Binary
_, imgBin = cv2.threshold(imgGray, 127, 255, cv2.THRESH_BINARY)
cv2.namedWindow('Binary', cv2.WINDOW_NORMAL)
cv2.imshow('Binary', imgBin)

# RGB 2 HSV
imgHSV = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2HSV)
cv2.namedWindow('HSV', cv2.WINDOW_NORMAL)
cv2.imshow('HSV', imgHSV)

cv2.waitKey(0)
cv2.destroyAllWindows()