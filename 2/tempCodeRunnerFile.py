out1 = np.zeros(img.shape, dtype=np.uint8)
# for i in range(2,h-2):
#     for j in range(2, w-2):
#         out1.itemset((i,j), np.mean(img[i-2:i+3,j-2:j+3]))
# cv2.imshow('Average filter', out1)


# # Weight Average filter
# mask=np.array([[1,2,4,2,1],
#                [2,4,8,4,2],
#                [4,8,16,8,4],
#                [2,4,8,4,2],
#                [1,2,4,2,1]])/128

# out2 = np.zeros(img.shape, dtype=np.uint8)
# for i in range(2,h-2):
#     for j in range(2, w-2):
#         out2.itemset((i,j), (mask*(img[i-2:i+3,j-2:j+3])).sum())
# cv2.imshow('Weight Average', out2)