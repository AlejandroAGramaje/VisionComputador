#Ejercicio 3: Usar una imagen umbralizada como máscara en una operación de suma o multiplicación

import cv2
import numpy as np
from tkinter import filedialog
import tkinter as tk

img = None
img_gray = None
img_mask = None

def seleccionar_imagen():
    global img, img_gray
    ruta = filedialog.askopenfilename(title="Seleccionar imagen")
    if ruta:
        img = cv2.imread(ruta)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        aplicar_umbral(127)
        cv2.imshow("Original", img)

def aplicar_umbral(umbral):
    global img_mask
    if img_gray is not None:
        _, img_mask = cv2.threshold(img_gray, umbral, 255, cv2.THRESH_BINARY)
        cv2.imshow("Máscara", img_mask)

def aplicar_operacion(tipo):
    if img is not None and img_mask is not None:
        if tipo == "suma":
            resultado = cv2.add(img, (50, 50, 50), mask=img_mask)
        elif tipo == "multiplica":
            # Multiplicamos todo y usamos la máscara manualmente
            img_float = img.astype(np.float32)
            resultado_full = img_float * 1.5
            resultado_full = np.clip(resultado_full, 0, 255).astype(np.uint8)
            resultado = img.copy()
            resultado[img_mask == 255] = resultado_full[img_mask == 255]
        cv2.imshow(f"Resultado {tipo}", resultado)

# GUI
ventana = tk.Tk()
ventana.title("Ejercicio 3")

btn_cargar = tk.Button(ventana, text="Seleccionar imagen", command=seleccionar_imagen)
btn_cargar.pack(pady=5)

btn_suma = tk.Button(ventana, text="Suma con máscara", command=lambda: aplicar_operacion("suma"))
btn_suma.pack(pady=5)

btn_mult = tk.Button(ventana, text="Multiplicación con máscara", command=lambda: aplicar_operacion("multiplica"))
btn_mult.pack(pady=5)

ventana.mainloop()

