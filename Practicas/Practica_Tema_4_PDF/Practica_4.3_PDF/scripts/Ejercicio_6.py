#Ejercicio Gordo: Difuminar solo las caras usando una máscara
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

img_original = None
mascara = None

def cargar_imagen():
    global img_original
    ruta = filedialog.askopenfilename(title="Seleccionar imagen principal")
    if ruta:
        img_original = cv2.imread(ruta)
        cv2.imshow("Imagen original", img_original)

def cargar_mascara():
    global mascara
    ruta = filedialog.askopenfilename(title="Seleccionar máscara")
    if ruta:
        mascara = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
        cv2.imshow("Máscara de caras", mascara)

def difuminar_caras():
    if img_original is None or mascara is None:
        messagebox.showerror("Error", "Carga una imagen y una máscara primero.")
        return

    # 1. Blur de toda la imagen
    imagen_blur = cv2.GaussianBlur(img_original, (25, 25), 0)
    cv2.imshow("Imagen con blur completo", imagen_blur)

    # 2. Máscara booleana y su inversa
    mascara_bin = mascara > 0
    mascara_inv = cv2.bitwise_not(mascara)
    cv2.imshow("Máscara invertida", mascara_inv)

    # 3. Fondo sin caras
    fondo = cv2.bitwise_and(img_original, img_original, mask=mascara_inv)
    cv2.imshow("Fondo sin caras", fondo)

    # 4. Caras difuminadas
    caras_blur = cv2.bitwise_and(imagen_blur, imagen_blur, mask=mascara)
    cv2.imshow("Sólo caras difuminadas", caras_blur)

    # 5. Imagen final combinada
    resultado = cv2.add(fondo, caras_blur)
    cv2.imshow("Resultado final", resultado)

# GUI
ventana = tk.Tk()
ventana.title("Ejercicio Gordo - Paso a paso")

tk.Button(ventana, text="Cargar imagen principal", command=cargar_imagen).pack(pady=5)
tk.Button(ventana, text="Cargar máscara de caras", command=cargar_mascara).pack(pady=5)
tk.Button(ventana, text="Aplicar difuminado", command=difuminar_caras).pack(pady=10)

ventana.mainloop()
