import cv2
import numpy as np
from tkinter import filedialog
import tkinter as tk

def cargar_imagen():
    ruta = filedialog.askopenfilename(title="Seleccionar imagen")
    if not ruta:
        return

    imagen = cv2.imread(ruta)
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # --- Detectar líneas con Hough ---
    bordes = cv2.Canny(gris, 100, 200)
    lineas = cv2.HoughLines(bordes, 1, np.pi / 180, 150)
    img_lineas = imagen.copy()
    if lineas is not None:
        for linea in lineas:
            rho, theta = linea[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv2.line(img_lineas, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # --- Detectar círculos con Hough ---
    imagen_blur = cv2.medianBlur(gris, 5)
    circulos = cv2.HoughCircles(imagen_blur, cv2.HOUGH_GRADIENT, dp=1.2,
                                 minDist=30, param1=100, param2=30,
                                 minRadius=10, maxRadius=100)

    img_circulos = imagen.copy()
    if circulos is not None:
        circulos = np.uint16(np.around(circulos))
        for c in circulos[0, :]:
            cv2.circle(img_circulos, (c[0], c[1]), c[2], (0, 0, 255), 2)
            cv2.circle(img_circulos, (c[0], c[1]), 2, (255, 0, 0), 3)

    # Mostrar imágenes reducidas
    mostrar("Original", imagen)
    mostrar("Líneas detectadas", img_lineas)
    mostrar("Círculos detectados", img_circulos)

def mostrar(nombre, imagen):
    reducida = cv2.resize(imagen, None, fx=0.5, fy=0.5)
    cv2.imshow(nombre, reducida)

# Interfaz
ventana = tk.Tk()
ventana.title("Ejercicio 1 - Hough")

tk.Button(ventana, text="Seleccionar imagen", command=cargar_imagen).pack(pady=10)

ventana.mainloop()
