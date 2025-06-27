#Ejercicio 2: Slider para umbralización en tiempo real
import cv2
import tkinter as tk
from tkinter import filedialog

img_gray = None
img_umbralizada = None

def seleccionar_imagen():
    global img_gray
    ruta = filedialog.askopenfilename(title="Seleccionar imagen")
    if ruta:
        mg_color = cv2.imread(ruta)
        imagen_resize = cv2.resize(mg_color, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
        img_gray = cv2.cvtColor(imagen_resize, cv2.COLOR_BGR2GRAY)
        aplicar_umbral(slider_umbral.get())
        cv2.imshow("Original", imagen_resize)
        cv2.imshow("Escala de Grises", img_gray)
        

def aplicar_umbral(umbral):
    global img_umbralizada
    if img_gray is not None:
        _, img_umbralizada = cv2.threshold(img_gray, int(umbral), 255, cv2.THRESH_BINARY)
        cv2.imshow("Umbralizada", img_umbralizada)

# GUI
ventana = tk.Tk()
ventana.title("Ejercicio 2")

btn_cargar = tk.Button(ventana, text="Seleccionar imagen", command=seleccionar_imagen)
btn_cargar.pack(pady=5)

slider_umbral = tk.Scale(ventana, from_=0, to=255, orient=tk.HORIZONTAL, command=aplicar_umbral)
slider_umbral.set(127)
slider_umbral.pack(pady=5)

ventana.mainloop()
