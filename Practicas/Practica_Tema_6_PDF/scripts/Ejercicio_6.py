#Ejercicio 6 – Contar monedas en una imagen

import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

img_original = None

def cargar_imagen():
    global img_original
    ruta = filedialog.askopenfilename(title="Seleccionar imagen (monedas.jpg)")
    if ruta:
        img_original = cv2.imread(ruta)
        mostrar("Imagen original", img_original)

def contar_monedas():
    if img_original is None:
        return

    # Paso 1: Convertimos a escala de grises y desenfocamos
    gris = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
    gris = cv2.GaussianBlur(gris, (7, 7), 1)

    # Paso 2: Umbralizamos
    _, binaria = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Paso 3: Quitamos ruido con apertura
    kernel = np.ones((3, 3), np.uint8)
    binaria = cv2.morphologyEx(binaria, cv2.MORPH_OPEN, kernel, iterations=2)

    # Paso 4: Encontramos contornos
    contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujamos los contornos y mostramos el número de monedas
    resultado = img_original.copy()
    for c in contornos:
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(resultado, (x, y), (x + w, y + h), (0, 255, 0), 2)

    total = len(contornos)
    print(f"Total de monedas detectadas: {total}")
    cv2.putText(resultado, f"Monedas: {total}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    mostrar("Conteo de monedas", resultado)

def mostrar(nombre, imagen):
    reducida = cv2.resize(imagen, None, fx=0.6, fy=0.6)
    cv2.imshow(nombre, reducida)

# GUI
ventana = tk.Tk()
ventana.title("Ejercicio 6 - Contar monedas")

tk.Button(ventana, text="Cargar imagen", command=cargar_imagen).pack(pady=5)
tk.Button(ventana, text="Contar monedas", command=contar_monedas).pack(pady=10)

ventana.mainloop()
