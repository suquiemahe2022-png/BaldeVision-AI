# BaldeVision AI

## Descripción
Sistema de detección de baldes de construcción mediante visión artificial.

## Objetivo
Desarrollar un detector de baldes en tiempo real utilizando Python, OpenCV y Haar Cascade.

## Herramientas utilizadas
- Python 3.12
- OpenCV
- NumPy
- Cascade Trainer GUI
- DroidCam

## Dataset
- 100 imágenes positivas.
- 100 imágenes negativas.

## Modelo
Se entrenó un clasificador Haar Cascade y se generó el archivo cascade.xml.

## Ejecución
1. Instalar OpenCV:
   `pip install opencv-contrib-python==4.10.0.84`
2. Conectar DroidCam.
3. Ejecutar:
   `python detectar_balde.py`

## Resultados
Se logró cargar el modelo y conectar la cámara. Durante las pruebas se identificaron falsos positivos que pueden mejorarse mediante un nuevo entrenamiento.
