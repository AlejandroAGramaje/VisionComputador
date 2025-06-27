#Ejercicio 3 – Segmentación basada en FloodFill

import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

img_original = None

def cargar_imagen():
    global img_original
    ruta = filedialog.askopenfilename(title="Seleccionar imagen (Gaviota.png)")
    if ruta:
        img_original = cv2.imread(ruta)
        mostrar("Imagen original", img_original)

def aplicar_floodfill():
    if img_original is None:
        return

    # Copia de la imagen para trabajar
    imagen = img_original.copy()
    alto, ancho = imagen.shape[:2]

    # Crear máscara 2px más grande que la imagen original
    mascara = np.zeros((alto + 2, ancho + 2), np.uint8)

    # Semilla: esquina superior izquierda (0, 0)
    semilla = (0, 0)

    # Rellenamos con blanco
    tolerancia = int(entry_tol.get())
    cv2.floodFill(imagen, mascara, seedPoint=semilla,
                  newVal=(0, 0, 255),
                  loDiff=(tolerancia, tolerancia, tolerancia),
                  upDiff=(tolerancia, tolerancia, tolerancia))

    mostrar(f"FloodFill con tolerancia {tolerancia}", imagen)

def mostrar(nombre, imagen):
    reducida = cv2.resize(imagen, None, fx=0.5, fy=0.5)
    cv2.imshow(nombre, reducida)

# GUI
ventana = tk.Tk()
ventana.title("Ejercicio 3 - FloodFill")

tk.Button(ventana, text="Cargar imagen", command=cargar_imagen).pack(pady=5)

tk.Label(ventana, text="Tolerancia de color:").pack()
entry_tol = tk.Entry(ventana, justify="center")
entry_tol.insert(0, "5")  # valor por defecto recomendado
entry_tol.pack(pady=5)

tk.Button(ventana, text="Aplicar FloodFill", command=aplicar_floodfill).pack(pady=10)

ventana.mainloop()
