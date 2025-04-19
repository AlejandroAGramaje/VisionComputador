import cv2
from tkinter import filedialog
import tkinter as tk

img_color = None
img_hsv = None

def seleccionar_imagen():
    global img_color, img_hsv
    ruta = filedialog.askopenfilename(title="Seleccionar imagen")
    if ruta:
        img_color = cv2.imread(ruta)
        img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(img_hsv)
        cv2.imshow("Canal H (Hue)", h)
        cv2.imshow("Canal S (Saturation)", s)
        cv2.imshow("Canal V (Value)", v)

# GUI
ventana = tk.Tk()
ventana.title("Ejercicio 7")

btn_cargar = tk.Button(ventana, text="Seleccionar imagen", command=seleccionar_imagen)
btn_cargar.pack(pady=10)

ventana.mainloop()
