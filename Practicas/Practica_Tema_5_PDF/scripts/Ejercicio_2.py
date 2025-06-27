import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

img_binaria = None

def cargar_imagen():
    global img_binaria
    ruta = filedialog.askopenfilename(title="Seleccionar imagen binaria")
    if ruta:
        img = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
        _, img_binaria = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY_INV)
        mostrar("Imagen binaria", img_binaria)

def mostrar(nombre, imagen):
    # Redimensionar la imagen al 50% para que no sea enorme
    reducida = cv2.resize(imagen, None, fx=0.5, fy=0.5)
    cv2.imshow(nombre, reducida)

def aplicar_operacion(tipo):
    if img_binaria is None:
        return

    kernel = np.ones((5, 5), np.uint8)

    if tipo == "gradiente":
        resultado = cv2.morphologyEx(img_binaria, cv2.MORPH_GRADIENT, kernel)
    elif tipo == "tophat":
        resultado = cv2.morphologyEx(img_binaria, cv2.MORPH_TOPHAT, kernel)
    elif tipo == "blackhat":
        resultado = cv2.morphologyEx(img_binaria, cv2.MORPH_BLACKHAT, kernel)

    mostrar(f"Resultado - {tipo}", resultado)

# GUI
ventana = tk.Tk()
ventana.title("Ejercicio 2 - Morfología derivada")

tk.Button(ventana, text="Cargar imagen", command=cargar_imagen).pack(pady=5)
tk.Button(ventana, text="Gradiente", command=lambda: aplicar_operacion("gradiente")).pack(pady=5)
tk.Button(ventana, text="TopHat", command=lambda: aplicar_operacion("tophat")).pack(pady=5)
tk.Button(ventana, text="BlackHat", command=lambda: aplicar_operacion("blackhat")).pack(pady=5)

ventana.mainloop()
