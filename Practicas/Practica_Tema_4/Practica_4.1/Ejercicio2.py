import cv2
import numpy as np

# Color verde para el nuevo fondo
color_fondo = [0, 255, 0]  # BGR

# Tolerancia para detectar el blanco
tolerancia = 40

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Crear máscara para detectar "blanco"
    blanco = np.array([220, 220, 220])
    diff = cv2.absdiff(frame, blanco)
    mascara = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    _, mascara = cv2.threshold(mascara, tolerancia, 255, cv2.THRESH_BINARY_INV)

    # Aplicar el fondo verde donde hay blanco
    frame_chroma = frame.copy()
    frame_chroma[mascara == 255] = color_fondo

    cv2.imshow("Chroma Key Básico", frame_chroma)

    if cv2.waitKey(1) == 27:  # ESC para salir
        break

cap.release()
cv2.destroyAllWindows()