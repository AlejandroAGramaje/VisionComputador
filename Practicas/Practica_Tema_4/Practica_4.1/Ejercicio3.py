import cv2
import numpy as np

# Color verde para el fondo
color_fondo = [0, 255, 0]
tolerancia = 100

# Abrir webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("No se pudo abrir la cámara.")
    exit()

# Obtener tamaño del video
ancho = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
alto = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Crear el objeto para grabar el video (formato MJPG)
salida = cv2.VideoWriter("salida.avi", cv2.VideoWriter_fourcc(*'MJPG'), 20.0, (ancho, alto))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    blanco = np.array([220, 220, 220])
    diff = cv2.absdiff(frame, blanco)
    mascara = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    _, mascara = cv2.threshold(mascara, tolerancia, 255, cv2.THRESH_BINARY_INV)

    frame_chroma = frame.copy()
    frame_chroma[mascara == 255] = color_fondo

    # Mostrar y grabar
    cv2.imshow("Chroma + Grabación", frame_chroma)
    salida.write(frame_chroma)

    if cv2.waitKey(1) == 27:  # ESC
        break

cap.release()
salida.release()
cv2.destroyAllWindows()
