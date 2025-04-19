#Ejercicio 4: Umbralización doble (rango de valores)
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

img_gray = None
img_rango = None

def seleccionar_imagen():
    global img_gray
    ruta = filedialog.askopenfilename(title="Seleccionar imagen")
    if ruta:
        img_color = cv2.imread(ruta)
        img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
        aplicar_umbral()

def aplicar_umbral():
    global img_rango
    if img_gray is not None:
        minimo = int(entry_min.get())
        maximo = int(entry_max.get())
        # Creamos la máscara con inRange
        img_rango = cv2.inRange(img_gray, minimo, maximo)
        cv2.imshow("Umbralización doble", img_rango)

# GUI
ventana = tk.Tk()
ventana.title("Ejercicio 4")

btn_cargar = tk.Button(ventana, text="Seleccionar imagen", command=seleccionar_imagen)
btn_cargar.pack(pady=5)

tk.Label(ventana, text="Umbral mínimo").pack()
entry_min = tk.Entry(ventana)
entry_min.insert(0, "100")
entry_min.pack()

tk.Label(ventana, text="Umbral máximo").pack()
entry_max = tk.Entry(ventana)
entry_max.insert(0, "200")
entry_max.pack()

btn_aplicar = tk.Button(ventana, text="Aplicar umbralización doble", command=aplicar_umbral)
btn_aplicar.pack(pady=10)

ventana.mainloop()
