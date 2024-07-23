# Herramienta de Censura de Imágenes

## Descripción

Este proyecto proporciona una herramienta gráfica para censurar partes de imágenes. Utiliza `Tkinter` para la interfaz gráfica de usuario y `OpenCV` para el procesamiento de imágenes. La herramienta permite abrir una imagen, seleccionar áreas para censurar, aplicar zoom, deshacer cambios y guardar la imagen censurada con un texto personalizado.

## Funcionalidades

- **Abrir imagen**: Permite abrir archivos de imagen en varios formatos (JPG, PNG, BMP, TIFF).
- **Censurar áreas**: Permite seleccionar áreas rectangulares de la imagen para aplicar censura mediante desenfoque.
- **Deshacer censura**: Permite deshacer la última censura aplicada.
- **Zoom In/Out**: Permite hacer zoom in y zoom out en la imagen para una mejor visualización y selección de áreas.
- **Guardar imagen**: Guarda la imagen censurada en blanco y negro, con un texto personalizado en el centro.
- **Ayuda**: Muestra una imagen de ayuda a la derecha de la interfaz, con opción de ocultarla.
- 
## Ejecucción en Windows

Ejecute la aplicación ImageCensorApp.exe contenida en la carpeta dist, no requiere ninguna instalación previa.

## Requisitos

- Python 3.6 o superior
- Tkinter (generalmente incluido con Python)
- Pillow (PIL Fork)
- OpenCV

## Instalación de Librerías

Para instalar las librerías necesarias, puedes usar `pip`:

```sh
pip install pillow opencv-python

