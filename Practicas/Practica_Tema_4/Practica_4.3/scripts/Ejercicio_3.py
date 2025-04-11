#Ejercicio 3: Ecualización del histograma

import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

def cargar_y_ecualizar():
    ruta = filedialog.askopenfilename(title="Seleccionar imagen")
    if not ruta:
        return

    img = cv2.imread(ruta)
    # Separar canales
    b, g, r = cv2.split(img)

    # Comprobamos si es en escala de grises o color
    if np.array_equal(b, g) and np.array_equal(g, r):
        # Imagen en escala de grises
        img_eq = cv2.equalizeHist(img[:,:,0])
        cv2.imshow("Original (Gris)", img)
        cv2.imshow("Ecualizada (Gris)", img_eq)
    else:
        # Imagen en color → pasar a HSV y ecualizar el canal H
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(img_hsv)

        # Ecualizar el canal H (tono)
        h_eq = cv2.equalizeHist(h)

        # Juntar canales y volver a BGR
        img_hsv_eq = cv2.merge((h_eq, s, v))
        img_color_eq = cv2.cvtColor(img_hsv_eq, cv2.COLOR_HSV2BGR)

        
        cv2.imshow("Original (Color)", img)
        cv2.imshow("Imagen ecualizada", img_hsv_eq)
        cv2.imshow("Ecualizada (Canal H)", img_color_eq)

# GUI básica
ventana = tk.Tk()
ventana.title("Ejercicio 3 - Ecualización")

tk.Button(ventana, text="Seleccionar imagen", command=cargar_y_ecualizar).pack(pady=10)

ventana.mainloop()
