import cv2
import numpy as np

# Funciones para el brillo y contraste
def aplicar_brillo_contraste(frame, brillo, contraste):
    # Normaliza brillo (-100 a 100) y contraste (0.1 a 3.0)
    brillo = brillo - 100
    contraste = contraste / 50.0
    frame_modificado = cv2.convertScaleAbs(frame, alpha=contraste, beta=brillo)
    return frame_modificado

# Función vacía para trackbars
def nada(x):
    pass

# Captura de cámara
cap = cv2.VideoCapture(0)

# Ventana y sliders
cv2.namedWindow("Brillo y Contraste")
cv2.createTrackbar("Brillo", "Brillo y Contraste", 100, 200, nada)     # Rango de 0 a 200, base 100
cv2.createTrackbar("Contraste", "Brillo y Contraste", 50, 150, nada)  # Rango de 10 a 150, base 50

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Leer valores de sliders
    brillo = cv2.getTrackbarPos("Brillo", "Brillo y Contraste")
    contraste = cv2.getTrackbarPos("Contraste", "Brillo y Contraste")

    # Aplicar ajustes
    frame_ajustado = aplicar_brillo_contraste(frame, brillo, contraste)

    # Mostrar imagen resultante
    cv2.imshow("Brillo y Contraste", frame_ajustado)

    if cv2.waitKey(1) == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
