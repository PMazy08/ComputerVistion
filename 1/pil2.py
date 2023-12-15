from PIL import Image

filename= 'ImageFromOpenCV\WindowsLogo.jpg' 
img = Image.open (filename) 
width, height = img.size 
img.show()
# อ่านจุดภาพตําาแหน่ง x,y=(100,100) 
pxy=img.getpixel ((100, 100))
print (pxy)
#เขียนค่าสีขาว ให้จุดภาพตําาแหน่ง x,y=(100,100) และ (101,100)
img.putpixel ((100, 100), (255,255,255))
img.putpixel ((101,100), (255,255,255))
img.putpixel ((100,101), (255,255,255)) 
img.putpixel ((101,101), (255,255,255))
img.putpixel ((102,101), (0,0,0)) 
img.putpixel ((103,101), (0,0,0)) 
print (img.getpixel ((100,100))) 
img.show()
