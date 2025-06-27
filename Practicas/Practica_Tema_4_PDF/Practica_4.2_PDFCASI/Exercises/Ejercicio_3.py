import cv2
from tkinter import filedialog
import tkinter as tk

img = None
img_gray = None
img_mask = None

def mostrar(título, imagen):
    # Escala la imagen al 60% de su tamaño original
    reducida = cv2.resize(imagen, None, fx=0.6, fy=0.6)
    cv2.imshow(título, reducida)

def seleccionar_imagen():
    global img, img_gray
    ruta = filedialog.askopenfilename(title="Seleccionar imagen")
    if ruta:
        img = cv2.imread(ruta)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        aplicar_umbral(127)
        mostrar("Original", img)

def aplicar_umbral(umbral):
    global img_mask
    if img_gray is not None:
        _, img_mask = cv2.threshold(img_gray, umbral, 255, cv2.THRESH_BINARY)
        mostrar("Máscara", img_mask)

def aplicar_operacion(tipo):
    if img is None or img_mask is None:
        return

    if tipo == "suma":
        valor = (50, 50, 50)
        resultado = cv2.add(img, valor, mask=img_mask)

    elif tipo == "multiplica":
        tmp = cv2.convertScaleAbs(img, alpha=1.5, beta=0)
        caras = cv2.bitwise_and(tmp, tmp, mask=img_mask)
        fondo = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(img_mask))
        resultado = cv2.add(caras, fondo)

    mostrar(f"Resultado {tipo}", resultado)

# GUI
ventana = tk.Tk()
ventana.title("Ejercicio 3")

tk.Button(ventana, text="Seleccionar imagen", command=seleccionar_imagen).pack(pady=5)
tk.Button(ventana, text="Suma con máscara", command=lambda: aplicar_operacion("suma")).pack(pady=5)
tk.Button(ventana, text="Multiplicación con máscara", command=lambda: aplicar_operacion("multiplica")).pack(pady=5)

ventana.mainloop()


