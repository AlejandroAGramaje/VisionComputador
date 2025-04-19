import cv2
import numpy as np
from tkinter import filedialog
import tkinter as tk
import matplotlib.pyplot as plt

img_color = None

def seleccionar_imagen():
    global img_color
    ruta = filedialog.askopenfilename(title="Seleccionar imagen")
    if ruta:
        img_color = cv2.imread(ruta)
        cv2.imshow("Imagen cargada", img_color)
        mostrar_histograma()

def mostrar_histograma():
    if img_color is not None:
        canales = ('b', 'g', 'r')
        colores = ('blue', 'green', 'red')
        plt.figure("Histograma por canal")
        plt.clf()  # Borrar figura previa
        for i, canal in enumerate(canales):
            hist = cv2.calcHist([img_color], [i], None, [256], [0, 256])
            plt.plot(hist, color=colores[i], label=f'Canal {canal.upper()}')
        plt.title("Histogramas por canal (RGB)")
        plt.xlabel("Intensidad")
        plt.ylabel("Frecuencia")
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.show()

# GUI
ventana = tk.Tk()
ventana.title("Ejercicio 5")

btn_cargar = tk.Button(ventana, text="Seleccionar imagen", command=seleccionar_imagen)
btn_cargar.pack(pady=10)

ventana.mainloop()
