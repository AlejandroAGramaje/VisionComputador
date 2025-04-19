import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

def cargar_y_thinning():
    ruta = filedialog.askopenfilename(title="Seleccionar imagen fp2")
    if not ruta:
        return

    # Cargar imagen en escala de grises
    imagen = cv2.imread(ruta, 0)

    # Invertimos la imagen (fondo negro, huella blanca)
    imagen = cv2.bitwise_not(imagen)

    # Duplicamos para el proceso
    imagen1 = imagen.copy()
    iskel = np.zeros(imagen.shape, dtype='uint8')

    # Kernel cruzado (habitual para morfología)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

    # Bucle hasta que la imagen esté vacía
    while cv2.countNonZero(imagen1) != 0:
        img_erosionada = cv2.erode(imagen1, kernel)
        img_abierta = cv2.morphologyEx(img_erosionada, cv2.MORPH_OPEN, kernel)
        img_resta = cv2.subtract(img_erosionada, img_abierta)
        iskel = cv2.bitwise_or(iskel, img_resta)
        imagen1 = img_erosionada.copy()

    # Mostramos resultado (reducido para que no ocupe toda la pantalla)
    reducida_original = cv2.resize(imagen, None, fx=0.5, fy=0.5)
    reducida_thinning = cv2.resize(iskel, None, fx=0.5, fy=0.5)
    cv2.imshow("Original invertida", reducida_original)
    cv2.imshow("Resultado thinning", reducida_thinning)

# GUI
ventana = tk.Tk()
ventana.title("Ejercicio 4 - Thinning (fácil)")

tk.Button(ventana, text="Cargar imagen fp2", command=cargar_y_thinning).pack(pady=10)

ventana.mainloop()
