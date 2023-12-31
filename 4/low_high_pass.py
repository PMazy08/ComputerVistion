import numpy as np 
import cv2 
import matplotlib.pyplot as plt

def normalize(sig,scale=255):
    spectrum = np.log(1+np.abs(sig))
    spectrum = cv2.normalize(spectrum, 0, 1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F) * scale

    return spectrum

img = cv2.imread(r"D:\junior_3\Term2_2566\ComputerVision\1\misc\misc\4.1.05.tiff", 0)


dft = np.fft.fft2(img)
spec_dft = normalize(dft)
dft_shift = np.fft.fftshift(dft)
spec_shift = normalize(dft_shift)

rows,cols = img.shape
crow,ccol = int (rows/2), int(cols/2)

#lowpass
mask = np.zeros(img.shape, np.uint8)
mask[crow-50:crow+50, ccol-50:ccol+50] = 1

#Highpass
# mask = np.ones(img.shape, np.uint8)
# mask[crow-50:crow+50, ccol-50:ccol+50] = 1



fshift = dft_shift * mask
f_ishift = np.fft.ifftshift(fshift)
img_back = normalize(np.fft.ifft2(f_ishift))


plt.subplot(221), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(spec_dft, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(spec_shift, cmap='gray')
plt.title('Centered Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(img_back, cmap='gray')
plt.title('Filtered Image'), plt.xticks([]), plt.yticks([])
plt.show()