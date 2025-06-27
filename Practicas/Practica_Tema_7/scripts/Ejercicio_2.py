import cv2
import numpy as np

# Cargar la imagen en escala de grises
img = cv2.imread('Practicas/Practica_Tema_7/images/tema7-img/jcontornos-test.png', cv2.IMREAD_GRAYSCALE)

# Binarizar (si no está ya)
_, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# Copias a color para pintar los resultados
solo_externos = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
relleno_todo = solo_externos.copy()

# --- a) Contornos externos ---
contornos_ext, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(solo_externos, contornos_ext, -1, (0, 255, 0), 2)  # verde

# --- b) Todos los contornos con relleno ---
contornos_todos, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(relleno_todo, contornos_todos, -1, (0, 0, 255), cv2.FILLED)  # rojo y relleno

# Guardar resultados
cv2.imwrite("Practicas/Practica_Tema_7/images/resultados/contornos_externos.png", solo_externos)
cv2.imwrite("Practicas/Practica_Tema_7/images/resultados/contornos_rellenos.png", relleno_todo)
