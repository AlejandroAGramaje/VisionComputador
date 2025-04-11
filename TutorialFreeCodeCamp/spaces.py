import cv2 as cv
import matplotlib.pyplot as plt

img =cv.imread("TutorialFreeCodeCamp/img/Camara2.png")
cv.imshow("Camara", img)


#Espacions de Color

#BGR --> A escalas de grises

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray',gray)

#BGR to HSV (Huge saturation Value)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow("HSV",hsv)

#BGR to L*a*b

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow("lab",lab)

#Enseña las imagenes en RGB no en GBR
# plt.imshow(img)
# plt.show()
#Convertimos imagen BGR to RGB

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)
plt.imshow(rgb)
plt.show()
#En resumidads cuentas tienen los colores invertidos la librearia de MATPLOTLIB y CV



cv.waitKey(0)