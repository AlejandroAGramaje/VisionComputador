import cv2 as cv
import numpy as np
#Contornos y los edges no son lo mismo matematicamente

img =cv.imread("TutorialFreeCodeCamp/img/Camara2.png")
cv.imshow("Camara",img)




#Imagen en gris
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("gray",gray)

blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow("blur",blur)

#Edges de la imagen
canny = cv.Canny(blur,125,175)
cv.imshow("canny",canny)

#Contornos de la iamgen
#contornos es una lista.
contours, hgierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE) #cv.RETR_LIST = A todos los contornos de la imagen / cv.CHAIN_APPROX_NONE algoritmo de aproximacion
print(f'{len(contours)} contornos encontrados')

#Otra forma de encontrar los contornos, Threshold
#Si la intensidad del pixel es menor a 125 se pone en negro, si la intesidad es mayor a 255 se pone a blanco.
ret, thresh = cv.threshold(canny,125,255,cv.THRESH_BINARY)

contours, hgierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE) #cv.RETR_LIST = A todos los contornos de la imagen / cv.CHAIN_APPROX_NONE algoritmo de aproximacion
print(f'{len(contours)} contornos encontrados')
cv.imshow('thresh',thresh)

#Vamos a dibujar los contornos en una imagen en blanco

blank = np.zeros(img.shape, dtype='uint8')
cv.drawContours(blank,contours,-1,(0,0,255),thickness=1)
cv.imshow("ContornosDibujados", blank)



cv.waitKey(0)

