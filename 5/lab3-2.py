import numpy as np
X = np.array([[10, 4, 22],
              [2, 18, 7],
              [9, 14, 25]])
x,y= X.shape[:2]
scale = 2
height, width = X.shape[:2]
nheight = int(height * scale)
nwidth = int(width * scale)
new_array = np.zeros((nheight, nwidth), dtype=X.dtype)
for i in range(nheight):
    for j in range(nwidth):
        i2 = int(i / scale)
        j2 = int(j / scale)
        new_array[i, j] = X[i2,j2]
print(X)
print("================================")
print(new_array)
