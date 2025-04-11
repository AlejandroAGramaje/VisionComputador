import cv2  as cv

img = cv.imread('PracticaTema4/img/Fotografia.jpg')

#Funciona en imagenes, Videos o Video en directo
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width,height)

    return cv.resize(frame,dimension, interpolation= cv.INTER_AREA)
#Solo para videos en Directo
def changeRes(width,height):
    #capture.set(3,with)
    #capture.set(4,heigh)
    pass

while True:
    frame_resize = rescaleFrame(img,0.2)
    
    cv.imshow("Imagen Redimensionada", frame_resize)

    if cv.waitKey(0) & 0xFF == ord('q'):
        break