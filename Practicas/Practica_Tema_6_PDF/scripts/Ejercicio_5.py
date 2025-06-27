#Ejercicio 5 – Segmentación basada en MeanShift
import cv2
import tkinter as tk
from tkinter import filedialog
import numpy as np

img_original = None

def cargar_imagen():
    global img_original
    ruta = filedialog.askopenfilename(title="Seleccionar imagen (Gaviota.png)")
    if ruta:
        img_original = cv2.imread(ruta)
        mostrar("Imagen original", img_original)

def aplicar_meanshift():
    if img_original is None:
        return

    # Aplicar MeanShift Filtering
    resultado = cv2.pyrMeanShiftFiltering(img_original, sp=20, sr=40)

    mostrar("Segmentación con MeanShift", resultado)

def mostrar(nombre, imagen):
    reducida = cv2.resize(imagen, None, fx=0.5, fy=0.5)
    cv2.imshow(nombre, reducida)

# GUI
ventana = tk.Tk()
ventana.title("Ejercicio 5 - MeanShift")

tk.Button(ventana, text="Cargar imagen", command=cargar_imagen).pack(pady=5)
tk.Button(ventana, text="Aplicar MeanShift", command=aplicar_meanshift).pack(pady=10)

ventana.mainloop()
