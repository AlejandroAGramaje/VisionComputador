import os
import cv2
import numpy as np

def analizar_imagen(ruta):
    img = cv2.imread(ruta)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, binary = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    binary = cv2.bitwise_not(binary)
    contornos, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    estado_final = "BUENO"

    for cnt in contornos:
        area = cv2.contourArea(cnt)
        perimetro = cv2.arcLength(cnt, True)
        rot_rect = cv2.minAreaRect(cnt)
        (cx, cy), (w, h), _ = rot_rect
        aspect_ratio = w / h if w > h else h / w
        cuadrado = aspect_ratio < 1.2
        approx = cv2.approxPolyDP(cnt, 0.01 * perimetro, True)
        irregular = len(approx) > 10

        estado = "BUENO" if cuadrado and not irregular else "DEFECTUOSO"
        if estado == "DEFECTUOSO":
            estado_final = estado

        box = cv2.boxPoints(rot_rect)
        box = np.intp(box)
        color = (0,255,0) if estado == "BUENO" else (0,0,255)
        cv2.drawContours(img, [box], 0, color, 2)
        cv2.putText(img, estado, (int(cx), int(cy)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    return img, estado_final

# Carpeta con imágenes
carpeta = "Practicas/Practica_Tema_7/images/Imagenes_EjerAmpliacion"
for nombre in os.listdir(carpeta):
    if nombre.endswith(".jpg") or nombre.endswith(".png"):
        ruta = os.path.join(carpeta, nombre)
        resultado, estado = analizar_imagen(ruta)
        salida = f"resultado_{nombre.split('.')[0]}_{estado}.png"
        cv2.imwrite(salida, resultado)
        print(f"{nombre}: {estado}")
