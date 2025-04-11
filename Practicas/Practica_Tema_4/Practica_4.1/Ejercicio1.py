import cv2 as cv
import numpy as np

def transparencia(img,tolerancia):
# Leer la imagen (sin canal alfa aún)
    if img is None:
        print("Imagen no cargada correctamente")
        exit()

    bgra = cv.cvtColor(img, cv.COLOR_BGR2BGRA)  #Se crea una imagen con canal alpha
    fondo = np.array([255,255,255])  # BGR
    
    # Calcular máscara: píxeles que están "cerca" del blanco
    mask = np.all(np.abs(img - fondo) <= tolerancia, axis=2)


    # Asignar canal alfa:
    # 0 (transparente) para fondo
    # 255 (opaco) para el resto
    bgra[:, :, 3] = np.where(mask, 0, 255)
    return bgra

if __name__ =="__main__":
    img = cv.imread("PracticaTema4/img/parque.jpg")
    tolerancia = int(input("Introduce la cantidad de tolerancias"))
    

    result = transparencia(img,tolerancia,)
    cv.imwrite('PracticaTema4/img/salida_transparente.png', result)
    cv.imshow('Resultado', result)
    cv.waitKey(0)
    cv.destroyAllWindows()



