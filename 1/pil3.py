from PIL import Image

filename= 'ImageFromOpenCV\WindowsLogo.jpg' 
img = Image.open (filename) 
width, height = img.size 
binImage = img.convert('1')
binImage.show()

# อ่านจุกภาพ x = 10, y = 10
print(binImage.getpixel((10,10)))

binImage.putpixel((10,10), 1)
print(binImage.getpixel((10,10)))