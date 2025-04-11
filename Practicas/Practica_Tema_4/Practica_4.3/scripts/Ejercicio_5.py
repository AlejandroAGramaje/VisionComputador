#Ejercicio 5: Filtro de Canny con sliders para umbral mínimo y máximo
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

img_gray = None

def cargar_imagen():
    global img_gray
    ruta = filedialog.askopenfilename(title="Seleccionar imagen")

    if ruta:
        img_color = cv2.imread(ruta)
        img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Original", img_gray)
        aplicar_canny()

def aplicar_canny():
    if img_gray is not None:
        umbral1 = slider_min.get()
        umbral2 = slider_max.get()
        bordes = cv2.Canny(img_gray, umbral1, umbral2)
        cv2.imshow("Canny", bordes)

# GUI
ventana = tk.Tk()
ventana.title("Ejercicio 6 - Canny")

tk.Button(ventana, text="Seleccionar imagen", command=cargar_imagen).pack(pady=10)

slider_min = tk.Scale(ventana, from_=0, to=255, label="Umbral mínimo", orient=tk.HORIZONTAL, command=lambda x: aplicar_canny())
slider_min.set(50)
slider_min.pack(pady=5)

slider_max = tk.Scale(ventana, from_=0, to=255, label="Umbral máximo", orient=tk.HORIZONTAL, command=lambda x: aplicar_canny())
slider_max.set(150)
slider_max.pack(pady=5)

ventana.mainloop()
