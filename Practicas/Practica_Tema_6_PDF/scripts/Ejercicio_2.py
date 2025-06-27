#Ejercicio 2 – Segmentación mediante Histograma

import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

img_gray = None

def cargar_imagen():
    global img_gray
    ruta = filedialog.askopenfilename(title="Seleccionar imagen (monedasG-ROI)")
    if ruta:
        img = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
        img_gray = img
        mostrar("Original (gris)", img_gray)
        mostrar_histograma(img_gray)

def mostrar(nombre, imagen):
    reducida = cv2.resize(imagen, None, fx=0.5, fy=0.5)
    cv2.imshow(nombre, reducida)

def mostrar_histograma(img):
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    plt.figure("Histograma de la imagen")
    plt.title("Histograma de Intensidad")
    plt.plot(hist, color='gray')
    plt.xlabel("Intensidad")
    plt.ylabel("Frecuencia")
    plt.grid()
    plt.show()

def aplicar_umbral():
    if img_gray is None:
        return

    umbral = int(entry_umbral.get())
    _, binaria = cv2.threshold(img_gray, umbral, 255, cv2.THRESH_BINARY_INV)
    mostrar(f"Umbralizado ({umbral})", binaria)

# Interfaz
ventana = tk.Tk()
ventana.title("Ejercicio 2 - Histograma + Umbral")

tk.Button(ventana, text="Cargar imagen", command=cargar_imagen).pack(pady=5)

tk.Label(ventana, text="Valor umbral:").pack()
entry_umbral = tk.Entry(ventana, justify="center")
entry_umbral.insert(0, "120")  # valor típico para monedasG-ROI
entry_umbral.pack(pady=5)

tk.Button(ventana, text="Aplicar umbralización", command=aplicar_umbral).pack(pady=10)

ventana.mainloop()
