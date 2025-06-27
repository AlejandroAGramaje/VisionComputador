import cv2
import numpy as np

# Genera un degradado horizontal o vertical, directo o invertido
def crear_degradado(ancho, alto, direccion="horizontal", inverso=False):
    if direccion == "horizontal":
        # Genera un vector de 0 a 255 a lo ancho
        grad = np.linspace(0, 255, ancho, dtype=np.uint8)
        if inverso:
            grad = grad[::-1]  # lo invertimos
        imagen = np.tile(grad, (alto, 1))  # copiamos la fila en todas las filas
    else:
        # Igual pero en vertical
        grad = np.linspace(0, 255, alto, dtype=np.uint8)
        if inverso:
            grad = grad[::-1]
        imagen = np.tile(grad[:, np.newaxis], (1, ancho))  # copiamos la columna en todas las columnas

    return imagen

if __name__ == "__main__":
    ancho = int(input("Ancho: "))
    alto = int(input("Alto: "))
    direccion = input("Dirección (horizontal/vertical): ")
    inverso = input("Invertir (s/n): ").lower() == "s"

    img = crear_degradado(ancho, alto, direccion, inverso)
    cv2.imshow("Degradado", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
