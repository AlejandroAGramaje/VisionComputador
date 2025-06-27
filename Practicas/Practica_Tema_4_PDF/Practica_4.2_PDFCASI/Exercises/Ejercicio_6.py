#Ejercicio 6: 2 sliders para suma/resta y multiplicación/división, y su efecto en el histograma
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

img_original = None

def seleccionar_imagen():
    global img_original
    ruta = filedialog.askopenfilename(title="Seleccionar imagen")
    if ruta:
        img = cv2.imread(ruta)
        img_original = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        aplicar_ajustes()

def aplicar_ajustes():
    if img_original is not None:
        suma = slider_suma.get()
        mult = slider_mult.get() / 10.0  # Para permitir decimales como 0.5, 1.2, etc.

        # Aplicar transformaciones
        modificada = cv2.convertScaleAbs(img_original, alpha=mult, beta=suma)
        cv2.imshow("Imagen Modificada", modificada)

        # Mostrar histograma
        hist = cv2.calcHist([modificada], [0], None, [256], [0, 256])
        plt.figure("Histograma modificado")
        plt.clf()
        plt.title(f"Histograma (Suma: {suma}, Multiplica: {mult})")
        plt.xlabel("Intensidad")
        plt.ylabel("Frecuencia")
        plt.plot(hist, color='black')
        plt.grid()
        plt.tight_layout()
        plt.pause(0.001)

# GUI
ventana = tk.Tk()
ventana.title("Ejercicio 6")

btn_cargar = tk.Button(ventana, text="Seleccionar imagen", command=seleccionar_imagen)
btn_cargar.pack(pady=5)

slider_suma = tk.Scale(ventana, from_=-100, to=100, label="Suma/Resta", orient=tk.HORIZONTAL, command=lambda x: aplicar_ajustes())
slider_suma.set(0)
slider_suma.pack(pady=5)

slider_mult = tk.Scale(ventana, from_=5, to=30, label="Multiplica (x/10)", orient=tk.HORIZONTAL, command=lambda x: aplicar_ajustes())
slider_mult.set(10)  # 10 = 1.0
slider_mult.pack(pady=5)

ventana.mainloop()
