from PIL import Image
filename = "ImageFromOpenCV\home.jpg"

imageObj = Image.open(filename)
imageObj.show()

# image 2 grayscale
grayImage = imageObj.convert('L')
grayImage.show()

# grayscale 2 Binary
theshold = 127
biImage = grayImage.point(lambda p:p > theshold and 255)
biImage.show()