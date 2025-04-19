import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

img_original = None

def cargar_imagen():
    global img_original
    ruta = filedialog.askopenfilename(title="Seleccionar imagen (sample19.jpg)")
    if ruta:
        img_original = cv2.imread(ruta)
        mostrar("Imagen original", img_original)

def flood_fill():
    if img_original is None:
        return

    # Hacemos una copia y convertimos a formato con 1 canal
    im_flood = img_original.copy()
    h, w = im_flood.shape[:2]

    # Creamos una máscara 2 pixeles más grande que la imagen
    mascara = np.zeros((h + 2, w + 2), np.uint8)

    # Rellenamos desde un punto interior (x=10, y=10) con color blanco
    cv2.floodFill(im_flood, mascara, seedPoint=(10, 10), newVal=(255, 255, 255))
    mostrar("Flood Fill", im_flood)

def transformada_distancia():
    if img_original is None:
        return

    # Convertimos a gris y binarizamos
    img_gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
    _, img_binaria = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Calculamos la transformada de distancia
    dist_transform = cv2.distanceTransform(img_binaria, distanceType=cv2.DIST_L2, maskSize=3)

    # Normalizamos para visualizar
    dist_norm = cv2.normalize(dist_transform, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    mostrar("Transformada de la distancia", dist_norm)

def mostrar(nombre, imagen):
    cv2.imshow(nombre, imagen)

# GUI
ventana = tk.Tk()
ventana.title("Ejercicio 3 - Flood Fill y Transformada de Distancia")

tk.Button(ventana, text="Cargar imagen", command=cargar_imagen).pack(pady=5)
tk.Button(ventana, text="Aplicar Flood Fill", command=flood_fill).pack(pady=5)
tk.Button(ventana, text="Transformada de distancia", command=transformada_distancia).pack(pady=5)

ventana.mainloop()
