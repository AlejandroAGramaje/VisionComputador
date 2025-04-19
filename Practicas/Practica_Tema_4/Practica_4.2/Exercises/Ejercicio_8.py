#Ejercicio 8: Mostrar imagen original, HSV y canales modificados
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

img_color = None
img_hsv = None

def seleccionar_imagen():
    global img_color, img_hsv
    ruta = filedialog.askopenfilename(title="Seleccionar imagen")
    if ruta:
        img_color = cv2.imread(ruta)
        img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)

        cv2.imshow("Original (BGR)", img_color)
        cv2.imshow("Convertida a HSV", cv2.cvtColor(img_hsv, cv2.COLOR_BGR2HSV))

        aplicar_modificacion()

def aplicar_modificacion():
    if img_hsv is not None:
        h, s, v = cv2.split(img_hsv)

        # Modificaciones
        h_mod = (h + 30) % 180
        s_mod = cv2.add(s, 30)
        v_mod = cv2.subtract(v, 40)

        nueva_hsv = cv2.merge((h_mod, s_mod, v_mod))
        resultado_bgr = cv2.cvtColor(nueva_hsv, cv2.COLOR_HSV2BGR)

        cv2.imshow("Imagen modificada (BGR)", resultado_bgr)

# GUI
ventana = tk.Tk()
ventana.title("Ejercicio 8 mejorado")

btn_cargar = tk.Button(ventana, text="Seleccionar imagen", command=seleccionar_imagen)
btn_cargar.pack(pady=10)

ventana.mainloop()
