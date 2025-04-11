import cv2 as cv

img = cv.imread("TutorialFreeCodeCamp/img/Camara2.png")
cv.imshow("Fotografia", img)

#1. Convertir imagen a escala de grises
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

#2. Añadir el "ruido" de la iamgen"
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

#3. Edge Cascade
canny = cv.Canny(img,125,175)
# cv.imshow("Canny", canny)
    # Puedes eliminar el numero de esquinas, utilizando una imagen con ruido/Blur
cannyBlur = cv.Canny(blur,125,175)
# cv.imshow("cannyBlur", cannyBlur)

#4. Dilatar imagenes
dilate = cv.dilate(canny, (7,7), iterations= 3)
# cv.imshow("dilate", dilate)

#5. Eroding
eroded = cv.erode(dilate, (7,7), iterations=3)
# cv.imshow("eroded", eroded)

#6. Reescalar Imagenes
resized = cv.resize(img, (500,500), interpolation= cv.INTER_CUBIC) #cv.INTER_AREA para hacer la imagen mas pequeña / cv.INTER_LINEAR para hacer mas grande / cv.INTER_CUBIC la mas lenta pero con mas calidad
# cv.imshow("resized", resized)

#7. Cropping
cropped = img[0:200, 100:500]
cv.imshow("cropped", cropped)
cv.waitKey(0)