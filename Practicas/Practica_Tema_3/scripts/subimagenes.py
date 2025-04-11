import cv2
import os

# Divide una imagen en filas x columnas subimágenes y las guarda
def generar_subimagenes(ruta, filas, columnas):
    img = cv2.imread(ruta)
    if img is None:
        print("No se pudo cargar la imagen.")
        return

    h, w = img.shape[:2]
    h_corte = h // filas
    w_corte = w // columnas

    # Creamos carpeta si no existe
    os.makedirs("subimagenes", exist_ok=True)

    for i in range(filas):
        for j in range(columnas):
            # Cortamos la región correspondiente
            subimg = img[i*h_corte:(i+1)*h_corte, j*w_corte:(j+1)*w_corte]
            # Guardamos cada subimagen
            nombre = f"subimagenes/sub_{i}_{j}.png"
            cv2.imshow(f"Subimagen {i},{j}", subimg)
            cv2.imwrite(nombre, subimg)
            
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    ruta = "Practicas/Practica_Tema_3/img/Foto_Barranc.png"
    filas = int(input("Número de filas: "))
    columnas = int(input("Número de columnas: "))
    generar_subimagenes(ruta, filas, columnas)
