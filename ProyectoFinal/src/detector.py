import cv2
import os
import numpy as np

# Ruta base
BASE_PATH = "ProyectoFinal/images"

# Categorías de conos
CATEGORIES = ["Buenas", "Rotas Fijas", "Rotas Rodando"]

# Tamaño de visualización
RESIZE_WIDTH = 400

def mostrar_imagenes():
    for categoria in CATEGORIES:
        carpeta = os.path.join(BASE_PATH, categoria)
        print(f"Mostrando imágenes de: {categoria}")

        for archivo in os.listdir(carpeta):
            ruta = os.path.join(carpeta, archivo)
            if ruta.lower().endswith((".bmp")):
                print(f"Leyendo: {ruta}")
                img = cv2.imread(ruta)
                if img is not None:
                    alto, ancho = img.shape[:2]
                    print(f"[INFO] Tamaño de imagen: {ancho} x {alto}")
                else:
                    print(f"Error al cargar {ruta}")
                    continue

                procesada = detectar_cono(img)
                cv2.imshow(f"{categoria}: {archivo}", procesada)
                key = cv2.waitKey(0)
                if key == 27:
                    break
                cv2.destroyAllWindows()

def detectar_cono(img):
    original = img.copy()
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    desenfoque = cv2.GaussianBlur(gris, (5, 5), 0)

    _, umbral = cv2.threshold(desenfoque,90, 255, cv2.THRESH_BINARY)
    cv2.imshow("Umbral", umbral)
    cv2.waitKey(0)

    contornos, jerarquia = cv2.findContours(umbral, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    if not contornos:
        print("No se encontraron contornos")
        return original

    for i, contorno in enumerate(contornos):
        print(f"[DEBUG] Contorno con {len(contorno)} puntos - Área: {cv2.contourArea(contorno):.1f}")
        if jerarquia[0][i][3] == -1 and cv2.contourArea(contorno) > 1000:
            x, y, w, h = cv2.boundingRect(contorno)
            cv2.rectangle(original, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # Detectar orientación con elipse
            if len(contorno) >= 5:
                try:
                    elipse = cv2.fitEllipse(contorno)
                    (xc, yc), (mayor, menor), angulo = elipse

                    if xc > 1500 or yc > 1500 or mayor > 2500 or menor > 2500:
                        print("[WARN] Elipse absurda. Reintentando con contorno suavizado...")
                        contorno = cv2.approxPolyDP(contorno, epsilon=2.0, closed=True)
                        if len(contorno) >= 5:
                            elipse = cv2.fitEllipse(contorno)
                            (xc, yc), (mayor, menor), angulo = elipse
                    else:
                        print("[ERROR] Contorno suavizado tiene <5 puntos. Usamos el original.")

                    print(f"[DEBUG] Elipse - Centro: ({xc:.1f}, {yc:.1f}), Ejes: ({mayor:.1f}, {menor:.1f}), Ángulo: {angulo:.2f}°")

                    alineado = (((angulo > 80 ) and (angulo < 100 )) or ((angulo < 285) and (angulo > 265)))
                    color = (0, 255, 0) if alineado else (0, 0, 255)

                    cv2.ellipse(original, elipse, color, 2)
                    cv2.circle(original, (int(xc), int(yc)), 4, (0, 0, 255), -1)

                except:
                    print("[ERROR] Fallo inesperado al ajustar la elipse.")
            else:
                print("Cono demasiado pequeño para analizar orientación.")

            # Detectar rotura por convexidad
            contorno_convexo = cv2.convexHull(contorno)
            area_original = cv2.contourArea(contorno)
            area_convexa = cv2.contourArea(contorno_convexo)
            ratio = area_original / area_convexa if area_convexa > 0 else 0

            roto_por_convexidad = ratio < 0.90
            print(f"[DEBUG] Roto por convexcdad: {roto_por_convexidad:.4f}")

            # Detectar rotura por comparación con múltiples plantillas
            similitudes = [
                cv2.matchShapes(contorno, plantilla, cv2.CONTOURS_MATCH_I1, 0.0)
                for plantilla in plantillas_buenas
            ]
            mejor_similitud = min(similitudes)
            roto_por_forma = mejor_similitud > 0.0595
            print(f"[DEBUG] Mejor similitud con plantillas: {mejor_similitud:.4f}")

            if roto_por_forma and roto_por_convexidad:
                print("❌ Cono posiblemente roto")
                cv2.putText(original, "ROTO", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
                cv2.drawContours(original, [contorno], -1, (0, 0, 255), 2)

            # Validación por tamaño
            valido = 300 <= w <= 345 and 125 <= h <= 150
            color = (0, 255, 0) if valido else (0, 0, 255)
            cv2.rectangle(original, (x, y), (x + w, y + h), color, 2)
            print(f"Cono {'válido' if valido else 'inválido'} - Ancho: {w}px, Alto: {h}px")

    return original

def guardar_varias_plantillas(directorio_buenos, salida="plantillas_buenas.npy"):
    plantillas = []
    for archivo in os.listdir(directorio_buenos):
        if archivo.lower().endswith((".bmp", ".jpg", ".jpeg")):
            ruta = os.path.join(directorio_buenos, archivo)
            img = cv2.imread(ruta)
            if img is None:
                continue

            gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            desenfoque = cv2.GaussianBlur(gris, (5, 5), 0)
            _, umbral = cv2.threshold(desenfoque, 95, 255, cv2.THRESH_BINARY)

            contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contornos = [c for c in contornos if cv2.contourArea(c) > 1000]

            if contornos:
                contorno_mayor = max(contornos, key=cv2.contourArea)
                plantillas.append(contorno_mayor)

    np.save(salida, np.array(plantillas, dtype=object))

    print(f"✅ {len(plantillas)} plantillas guardadas en '{salida}'")

if __name__ == "__main__":
    # Generar plantillas si no existen
    if not os.path.exists("plantillas_buenas.npy"):
        guardar_varias_plantillas("ProyectoFinal/images/Buenas")

    plantillas_buenas = np.load("plantillas_buenas.npy", allow_pickle=True)
    mostrar_imagenes()
