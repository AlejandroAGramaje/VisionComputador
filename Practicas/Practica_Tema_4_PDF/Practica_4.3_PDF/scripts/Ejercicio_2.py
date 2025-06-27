#Ejercicio 2: Umbralización del rojo y amarillo mediante LUT
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

img_gray = None

def cargar_imagen():
    global img_gray
    ruta = filedialog.askopenfilename(title="Seleccionar imagen")
    if ruta:
        img_color = cv2.imread(ruta)
        img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Original", img_color)
        aplicar_lut()

def aplicar_lut():
    if img_gray is not None:
        # Crear LUT: 0 para tonos oscuros (donde está rojo/amarillo), 255 para lo demás
        lut = np.ones(256, dtype=np.uint8) * 255
        # Aproximadamente entre 80 y 160 en gris aparecen rojo y amarillo
        lut[80:160] = 0

        # Aplicar LUT
        img_lut = cv2.LUT(img_gray, lut)
        cv2.imshow("Imagen con LUT", img_lut)

        # Suavizar con Gaussiano
        img_gauss = cv2.GaussianBlur(img_lut, (5, 5), 0)
        cv2.imshow("Gaussiano", img_gauss)

        # Umbralización final
        _, img_final = cv2.threshold(img_gauss, 128, 255, cv2.THRESH_BINARY)
        cv2.imshow("Resultado final (LUT + Gauss + Umbral)", img_final)

# GUI
ventana = tk.Tk()
ventana.title("Ejercicio 2 - LUT rojo/amarillo")

tk.Button(ventana, text="Seleccionar imagen", command=cargar_imagen).pack(pady=10)

ventana.mainloop()
