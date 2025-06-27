#EditBox y umbralización
import cv2
import tkinter as tk
from tkinter import filedialog
import os

img_gray = None
img_umbralizada = None

def seleccionar_imagen():
    global img_gray
    ruta = filedialog.askopenfilename(title="Seleccionar imagen")
    if ruta:
        img_color = cv2.imread(ruta)
        imagen_resize = cv2.resize(img_color, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
        img_gray = cv2.cvtColor(imagen_resize, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Original", imagen_resize)
        cv2.imshow("EscalaGrises", img_gray)

def aplicar_umbral():
    global img_umbralizada
    if img_gray is not None:
        umbral = int(entry_umbral.get())
        _, img_umbralizada = cv2.threshold(img_gray, umbral, 255, cv2.THRESH_BINARY)
        cv2.imshow("Umbralizada", img_umbralizada)

# GUI
ventana = tk.Tk()
ventana.title("Ejercicio 1")

btn_cargar = tk.Button(ventana, text="Seleccionar imagen", command=seleccionar_imagen)
btn_cargar.pack(pady=5)

entry_umbral = tk.Entry(ventana)
entry_umbral.insert(0, "127")
entry_umbral.pack(pady=5)

btn_aplicar = tk.Button(ventana, text="Aplicar Umbral", command=aplicar_umbral)
btn_aplicar.pack(pady=5)

ventana.mainloop()


