import cv2
import numpy as np
import random

img = cv2.imread('Practicas/Practica_Tema_7/images/tema7-img/img1.png', cv2.IMREAD_GRAYSCALE)

_, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary)

output = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

for i in range(1, num_labels):
    mask = (labels == i)
    color = [random.randint(0, 255) for _ in range(3)]
    output[mask] = color

    # Dibujar círculo en el centroide
    cx, cy = int(centroids[i][0]), int(centroids[i][1])
    cv2.circle(output, (cx, cy), 3, (255, 255, 255), -1)

    x, y, w, h, area = stats[i]
    print(f"Obj {i}: LEFT={x}, TOP={y}, WIDTH={w}, HEIGHT={h}, AREA={area}, Centroide=({cx},{cy})")

# Guardar resultado
cv2.imwrite("Practicas/Practica_Tema_7/images/resultados/resultado_img1.png", output)
