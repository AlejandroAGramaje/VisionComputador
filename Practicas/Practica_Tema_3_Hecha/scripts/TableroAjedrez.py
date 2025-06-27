import cv2
import numpy as np

# Crea una imagen con patrón de ajedrez en blanco y negro
def crear_tablero(ancho, alto, divisiones):
    # Imagen inicial en negro (uint8 -> escala de grises)
    tablero = np.zeros((alto, ancho), dtype=np.uint8)
    # Tamaño de cada celda
    h_celda = alto // divisiones
    w_celda = ancho // divisiones

    for fila in range(divisiones):
        for col in range(divisiones):
            # Alternar blanco y negro
            if (fila + col) % 2 == 0:
                y1 = fila * h_celda
                x1 = col * w_celda
                tablero[y1:y1+h_celda, x1:x1+w_celda] = 255  # píxeles blancos

    return tablero

if __name__ == "__main__":
    # Pedimos al usuario dimensiones y número de casillas
    ancho = int(input("Ancho de la imagen: "))
    alto = int(input("Alto de la imagen: "))
    divisiones = int(input("Número de divisiones: "))

    img = crear_tablero(ancho, alto, divisiones)
    cv2.imshow("Tablero de ajedrez", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
