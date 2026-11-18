import cv2

# Cargar modelo Haar Cascade
ruta_modelo = r"C:\Users\Maria\Downloads\DATASET_BALDE\classifier\cascade.xml"
detector = cv2.CascadeClassifier(ruta_modelo)

if detector.empty():
    print("ERROR: No se pudo cargar el modelo")
    raise SystemExit

print("MODELO HAAR CASCADE CARGADO CORRECTAMENTE")

# Conectar DroidCam
camara = cv2.VideoCapture(1, cv2.CAP_DSHOW)

if not camara.isOpened():
    print("ERROR: No se pudo abrir DroidCam")
    raise SystemExit

print("CAMARA CONECTADA CORRECTAMENTE")
print("DETECTOR INICIADO - PRESIONA Q PARA SALIR")

while True:
    correcto, imagen = camara.read()

    if not correcto:
        print("ERROR: No se recibe imagen")
        break

    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    gris = cv2.equalizeHist(gris)

    baldes = detector.detectMultiScale(
        gris,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(40, 40)
    )

    if len(baldes) > 0:
        for (x, y, w, h) in baldes:
            cv2.rectangle(imagen, (x, y), (x+w, y+h), (0, 255, 0), 3)
            cv2.putText(
                imagen,
                "BALDE DE CONSTRUCCION",
                (x, max(y-10, 30)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )
    else:
        cv2.putText(
            imagen,
            "NO SE DETECTA EL BALDE",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 0, 255),
            2
        )

    cv2.imshow("DETECTOR HAAR CASCADE - BALDE", imagen)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camara.release()
cv2.destroyAllWindows()
print("DETECTOR FINALIZADO")
