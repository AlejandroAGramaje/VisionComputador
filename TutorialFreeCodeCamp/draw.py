import cv2 as cv
import numpy as np

blank= np.zeros((500,500,3), dtype='uint8')

img = cv.imread('TutorialFreeCodeCamp/img/Fotografia.jpg')
# cv.imshow('Fotografia',img)

# 1. Pintar toda la imagen de verde (crear una copia antes de modificar)
blank_green = blank.copy()
blank_green[:] = 0, 255, 0  # Toda la imagen verde
# cv.imshow('Green', blank_green)

# 2. Pintar solo una sección de la imagen de verde (crear otra copia)
blank_section = blank.copy()
blank_section[200:300, 300:400] = 0, 255, 0  # Solo una parte verde
# cv.imshow('Rango Verde', blank_section)

#3. Dibujar un rectangulo

blank_rectangulo = blank.copy()
cv.rectangle(blank_rectangulo, (0,0), (250,250), (0,255,0), thickness= 2) #thickness= cv.FILLED /-1 rellena el rectangulo
# cv.imshow("Rectangulo", blank_rectangulo)
 
#4. Dibujar ciruclo
blank_circulo = blank.copy()
cv.circle (blank_circulo, (250,250),40, (0,255,0), thickness= -1)
# cv.imshow("Circulo", blank_circulo)

#5. Dibujar todo junto sobre un mismo canvas
cv.circle (blank_rectangulo, (250,250),40, (0,255,0), thickness= -1)
# cv.imshow("Rectangulo", blank_rectangulo)

#6. Dibujar una linea
blank_linea = blank.copy()
cv.line(blank_linea, (50,50) , (250,250), (255,0,0), thickness= 50)
cv.imshow("Linea", blank_linea)

cv.waitKey(0)