import cv2
import numpy as np

# Cargar la imagen en escala de grises
img = cv2.imread('Practicas/Practica_Tema_7/images/tema7-img/img4.png', cv2.IMREAD_GRAYSCALE)

# Binarizar
_, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# Convertir a color para dibujar
output = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)

# Obtener todos los contornos (incluyendo internos)
contornos, jerarquia = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Procesar cada contorno
for i, cnt in enumerate(contornos):
    # Área y perímetro
    area = cv2.contourArea(cnt)
    perimetro = cv2.arcLength(cnt, True)

    # Ignorar contornos muy pequeños (ruido)
    if area < 50:
        continue

    # Rectángulo no rotado
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)  # verde

    # Rectángulo rotado mínimo
    rot_rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rot_rect)
    box = np.intp(box)
    cv2.drawContours(output, [box], 0, (0, 0, 255), 2)  # rojo

    # Posición del texto (ligeramente desplazado)
    cx, cy = int(rot_rect[0][0]), int(rot_rect[0][1])
    texto = f"A:{int(area)} P:{int(perimetro)}"
    cv2.putText(output, texto, (cx + 10, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)

    print(f"Obj {i}: Área = {area:.2f}, Perímetro = {perimetro:.2f}")

# Guardar el resultado
cv2.imwrite("Practicas/Practica_Tema_7/images/resultados/img4_rectangulos_todos.png", output)
