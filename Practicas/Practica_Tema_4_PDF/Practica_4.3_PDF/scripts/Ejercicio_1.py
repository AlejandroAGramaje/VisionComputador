import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

img = None
mascara = None

# Función para seleccionar imagen y convertirla a escala de grises
def cargar_imagen():
    global img
    ruta = filedialog.askopenfilename(title="Seleccionar imagen")
    if ruta:
        img_color = cv2.imread(ruta)
        img = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Imagen original", img)

# Función para seleccionar una máscara opcional
def cargar_mascara():
    global mascara
    ruta = filedialog.askopenfilename(title="Seleccionar máscara")
    if ruta:
        mascara = cv2.imread(ruta, cv2.IMREAD_GRAYSCALE)
        cv2.imshow("Máscara", mascara)

# Cálculo de media y desviación, con o sin máscara
def calcular_valores():
    if img is None:
        messagebox.showerror("Error", "Primero carga una imagen.")
        return

    # Si hay máscara, sólo se toman los píxeles donde máscara > 0
    if mascara is not None:
        valores = img[mascara > 0]
    else:
        valores = img.flatten()

    media = np.mean(valores)
    desviacion = np.std(valores)

    # Mostrar valores sobre una copia en color
    img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.putText(img_color, f"Media: {media:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.putText(img_color, f"Desv: {desviacion:.2f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow("Resultado", img_color)

# Interfaz básica con botones
ventana = tk.Tk()
ventana.title("Ejercicio 1 - Brillo y Desviación")

tk.Button(ventana, text="Seleccionar imagen", command=cargar_imagen).pack(pady=5)
tk.Button(ventana, text="Seleccionar máscara (opcional)", command=cargar_mascara).pack(pady=5)
tk.Button(ventana, text="Calcular media y desviación", command=calcular_valores).pack(pady=10)

ventana.mainloop()

