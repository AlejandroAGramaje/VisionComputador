import cv2
import numpy as np

# Crea una imagen tipo tablero, pero con colores aleatorios en cada celda
def crear_tablero_color(ancho, alto, divisiones):
    tablero = np.zeros((alto, ancho, 3), dtype=np.uint8)  # 3 canales: BGR
    h_celda = alto // divisiones
    w_celda = ancho // divisiones

    for fila in range(divisiones):
        for col in range(divisiones):
            # Generamos un color aleatorio con 3 valores
            color = np.random.randint(0, 256, 3).tolist()
            y1 = fila * h_celda
            x1 = col * w_celda
            tablero[y1:y1+h_celda, x1:x1+w_celda] = color

    return tablero

if __name__ == "__main__":
    ancho = int(input("Ancho: "))
    alto = int(input("Alto: "))
    divisiones = int(input("Divisiones: "))

    img = crear_tablero_color(ancho, alto, divisiones)
    cv2.imshow("Tablero a color", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
