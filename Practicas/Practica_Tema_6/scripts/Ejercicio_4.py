#Ejercicio 4 – Segmentación con GrabCut
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

def aplicar_grabcut():
    if img_original is None:
        return

    img = img_original.copy()
    mask = np.zeros(img.shape[:2], np.uint8)

    # Modelos internos de GrabCut (obligatorios aunque no los uses directamente)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    # Rectángulo que encierra el objeto (ajustable)
    alto, ancho = img.shape[:2]
    rect = (int(ancho*0.1), int(alto*0.1), int(ancho*0.8), int(alto*0.8))

    # Ejecutar GrabCut
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)

    # Procesar la máscara para dejar solo el objeto
    output_mask = np.where((mask == 2) | (mask == 0), 0, 1).astype(np.uint8)
    resultado = img * output_mask[:, :, np.newaxis]

    mostrar("Segmentación con GrabCut", resultado)

def mostrar(nombre, imagen):
    reducida = cv2.resize(imagen, None, fx=0.5, fy=0.5)
    cv2.imshow(nombre, reducida)

# GUI
ventana = tk.Tk()
ventana.title("Ejercicio 4 - GrabCut")

tk.Button(ventana, text="Cargar imagen", command=cargar_imagen).pack(pady=5)
tk.Button(ventana, text="Aplicar GrabCut", command=aplicar_grabcut).pack(pady=10)

ventana.mainloop()
