import sys
from PIL import Image
print("Ingrese el nombre de la imagen, Ej Lena.jpg: ")
imageName=input()
print("Elija el Nombre y formato de salida, Ej Lena.jpg: ")
imageSave=input()
global height
global width
imagen=str(imageName)
try:
        img = Image.open(imagen)
except:
        print("La imagen no está en este directorio")
        sys.exit()
#img2= img.convert('LA')
width, height = img.size
print(width)
print(height)


img = img.resize((9,9)) #optimize operations reducing scale with same ratio
img.save(imageSave) #Turn rgb image 2 gray scale [0,255]
