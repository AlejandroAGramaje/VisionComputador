#Ejercicio 1 – Erosión, dilatación, apertura y cierr
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

img_binaria = None

# Cargar imagen y umbralizar
def cargar_imagen():
    global img_binaria
    ruta = filedialog.askopenfilename(title="Seleccionar imagen binaria")
    if ruta:
        img = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
        _, img_binaria = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
        cv2.imshow("Imagen binaria", img_binaria)

def aplicar_operacion(tipo):
    if img_binaria is None:
        return

    # Definimos un kernel 5x5
    kernel = np.ones((5, 5), np.uint8)

    if tipo == "erosion":
        resultado = cv2.erode(img_binaria, kernel, iterations=1)
    elif tipo == "dilatacion":
        resultado = cv2.dilate(img_binaria, kernel, iterations=1)
    elif tipo == "apertura":
        resultado = cv2.morphologyEx(img_binaria, cv2.MORPH_OPEN, kernel)
    elif tipo == "cierre":
        resultado = cv2.morphologyEx(img_binaria, cv2.MORPH_CLOSE, kernel)

    cv2.imshow(f"Resultado - {tipo}", resultado)

# GUI
ventana = tk.Tk()
ventana.title("Ejercicio 1 - Morfología básica")

tk.Button(ventana, text="Cargar imagen", command=cargar_imagen).pack(pady=5)
tk.Button(ventana, text="Erosión", command=lambda: aplicar_operacion("erosion")).pack(pady=5)
tk.Button(ventana, text="Dilatación", command=lambda: aplicar_operacion("dilatacion")).pack(pady=5)
tk.Button(ventana, text="Apertura", command=lambda: aplicar_operacion("apertura")).pack(pady=5)
tk.Button(ventana, text="Cierre", command=lambda: aplicar_operacion("cierre")).pack(pady=5)

ventana.mainloop()
