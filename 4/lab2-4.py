import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(50, 10), constrained_layout=False)
img_c1 = cv2.imread(r"Image4Otsu\s047.tif", 0)
img_c2 = np.fft.fft2(img_c1) #2d fft
img_c3 = np.fft.fftshift(img_c2) #fft shift
img_c4 = np.fft.ifftshift(img_c3) #inverse fft shift
img_c5 = np.fft.ifft2(img_c4) #inverse 2d fft
img_c6 = np.angle(img_c2) #phase spectrum

plt.subplot(231), plt.imshow(img_c1, "gray")
plt.title("Original Image"), plt.axis("off")

plt.subplot(232), plt.imshow(np.log(1+np.abs(img_c2)), "gray")
plt.title("Frequency Spectrum"), plt.axis("off")

plt.subplot(233), plt.imshow(img_c6, "gray")
plt.title("Phase Spectrum"), plt.axis("off")

plt.subplot(234), plt.imshow(np.log(1+np.abs(img_c3)), "gray")
plt.title("Centered Spectrum"), plt.axis("off")

plt.subplot(235), plt.imshow(np.log(1+np.abs(img_c4)), "gray")
plt.title("Decentralized Spectrum"), plt.axis("off")

plt.subplot(236), plt.imshow(np.abs(img_c5), "gray")
plt.title("Processed Image"), plt.axis("off")

plt.show()