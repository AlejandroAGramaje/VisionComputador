import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

img_gray = None

# Cargar imagen y convertirla a escala de grises
def cargar_imagen():
    global img_gray
    ruta = filedialog.askopenfilename(title="Seleccionar imagen")
    if ruta:
        img_color = cv2.imread(ruta)
        img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Original (Gris)", img_gray)
        aplicar_sobel()

# Aplicar Sobel con los parámetros actuales
def aplicar_sobel():
    if img_gray is not None:
        dx = int(slider_dx.get())
        dy = int(slider_dy.get())
        ksize = int(slider_ksize.get())

        # Aplicamos filtro Sobel
        sobel = cv2.Sobel(img_gray, cv2.CV_64F, dx, dy, ksize=ksize)
        sobel_abs = cv2.convertScaleAbs(sobel)  # Convertimos para mostrar bien
        cv2.imshow("Sobel", sobel_abs)

# GUI
ventana = tk.Tk()
ventana.title("Ejercicio 4 - Filtro Sobel")

tk.Button(ventana, text="Seleccionar imagen", command=cargar_imagen).pack(pady=10)

# Sliders para elegir dx, dy y ksize
slider_dx = tk.Scale(ventana, from_=0, to=2, label="dx", orient=tk.HORIZONTAL, command=lambda x: aplicar_sobel())
slider_dx.set(1)
slider_dx.pack(pady=5)

slider_dy = tk.Scale(ventana, from_=0, to=2, label="dy", orient=tk.HORIZONTAL, command=lambda x: aplicar_sobel())
slider_dy.set(0)
slider_dy.pack(pady=5)

slider_ksize = tk.Scale(ventana, from_=1, to=7, resolution=2, label="Kernel size (ímpar)", orient=tk.HORIZONTAL, command=lambda x: aplicar_sobel())
slider_ksize.set(3)
slider_ksize.pack(pady=5)

ventana.mainloop()
