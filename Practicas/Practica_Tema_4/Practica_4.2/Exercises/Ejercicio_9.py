import cv2
import numpy as np
from tkinter import filedialog
import os

fondo = None
color_croma = None
tolerancia = 40  # Tolerancia para eliminar el color

# Paso 1: Cargar imagen de fondo
ruta_fondo = filedialog.askopenfilename(title="Selecciona imagen de fondo")
if not ruta_fondo:
    print("No se seleccionó fondo.")
    exit()

fondo = cv2.imread(ruta_fondo)

# Paso 2: Abrir cámara
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("No se pudo acceder a la cámara.")
    exit()

# Obtener tamaño para redimensionar fondo
ret, frame = cap.read()
alto, ancho = frame.shape[:2]
fondo = cv2.resize(fondo, (ancho, alto))

# Paso 3: Crear writer para guardar el video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (ancho, alto))

def seleccionar_color(event, x, y, flags, param):
    global color_croma
    if event == cv2.EVENT_LBUTTONDOWN:
        color_croma = frame[y, x]
        print(f"Color seleccionado: {color_croma}")

cv2.namedWindow("Chroma")
cv2.setMouseCallback("Chroma", seleccionar_color)

print("Haz clic sobre el color que quieras eliminar (fondo verde o azul).")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if color_croma is not None:
        # Crear máscara para el color seleccionado
        color_bgr = np.array(color_croma)
        color_hsv = cv2.cvtColor(np.uint8([[color_bgr]]), cv2.COLOR_BGR2HSV)[0][0]

        min_hsv = np.clip(color_hsv - tolerancia, 0, 255)
        max_hsv = np.clip(color_hsv + tolerancia, 0, 255)

        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(frame_hsv, min_hsv, max_hsv)
        mask_inv = cv2.bitwise_not(mask)

        # Crear imagen combinada
        foreground = cv2.bitwise_and(frame, frame, mask=mask_inv)
        background = cv2.bitwise_and(fondo, fondo, mask=mask)
        resultado = cv2.add(foreground, background)
    else:
        resultado = frame

    cv2.imshow("Chroma", resultado)
    out.write(resultado)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
