import cv2 as cv
import numpy as np

img = cv.imread("TutorialFreeCodeCamp/img/Camara2.png")
cv.imshow("Camara", img)

#1. Transladar
# -x ---> Transladar a la izquierda
# -y ---> Transladar hacia arriba
# x ---> Transladar a la derecha
# y ---> Transladar hacia abajo

def translate(img, x, y): #img = imagen, x e y a los pixeles en los cuales quieres trasladar (la posicion)
    transMatrix = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img,transMatrix,dimension)

# translate1 = translate(img, 100,100)
# cv.imshow("translate1",translate1) 
# translate2 = translate(img, -100,-100)
# cv.imshow("translate2",translate2)

#2. Rotar
def rotation(img, angle, rotPoint = None):
    (height,width) = img.shape[:2]
    #Rotar en base del centro
    if rotPoint == None:
        rotPoint = (width//2,height//2)
    #Rotar en base del punto que se nos proporciona
    rotMatrix = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine(img,rotMatrix,dimensions)

rotate1 = rotation(img,45)
# cv.imshow("rotate1",rotate1)

#3.Reescalar de nuevo

resized = cv.resize(img,(400,400), interpolation=cv.INTER_CUBIC)
# cv.imshow("resized",resized)
#4. Flipping

flip = cv.flip(img, -1) #0 = Flipear la imagen verticalmente / 1 = Horizontalmente /-1 = Verticalmente y horizontalmente
cv.imshow("flip",flip)

#Cropping img[altura, ancho]
cropped = img[100:400, 100:300]
cv.imshow("Cropped",cropped)

cv.waitKey(0)