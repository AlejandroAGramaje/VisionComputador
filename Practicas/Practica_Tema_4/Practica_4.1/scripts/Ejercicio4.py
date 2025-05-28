import cv2
import numpy as np

color_fondo = np.array([0, 255, 0])  # valor por defecto
tolerancia = 40
color_reemplazo = np.array([255, 0, 0])  # azul

# Variable global para actualizar el color con el ratón
seleccionar_color = False

def aplicar_chroma(frame, color_objetivo, tolerancia):
    diff = np.abs(frame.astype(np.int16) - color_objetivo.astype(np.int16))
    mask = np.all(diff <= tolerancia, axis=2)
    frame_resultado = frame.copy()
    frame_resultado[mask] = color_reemplazo
    return frame_resultado

# Función de callback para capturar color del clic
def click_raton(event, x, y, flags, param):
    global color_fondo, seleccionar_color
    if event == cv2.EVENT_LBUTTONDOWN:
        frame = param
        color_fondo = frame[y, x]  # BGR en ese punto
        seleccionar_color = True
        print(f"Color seleccionado: {color_fondo}")

# Captura desde webcam
cap = cv2.VideoCapture(0)
cv2.namedWindow("Chroma Key")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Muestra el frame y espera clic
    cv2.setMouseCallback("Chroma Key", click_raton, param=frame)

    # Aplica el efecto
    resultado = aplicar_chroma(frame, color_fondo, tolerancia)

    # Muestra el resultado
    cv2.imshow("Chroma Key", resultado)

    # ESC para salir
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
