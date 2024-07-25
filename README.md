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
  
## Ejecucción en Windows

Descargue [aquí](https://www.mediafire.com/file/i9sfoy9tvbx53i5/ImageCensorApp.exe/file) la aplicación ImageCensorApp.exe, luego ejecute. No requiere ninguna instalación previa.

## Requisitos

- Python 3.6 o superior
- Tkinter (generalmente incluido con Python)
- Pillow (PIL Fork) versión 10.3.0
- OpenCV versión 4.10.0.82
- numpy versión 1.26.4

## Instalación de Librerías

Para instalar las librerías necesarias, puedes usar `pip`:

```sh
pip install pillow==10.3.0 opencv-python==4.10.0.82 numpy==1.26.4
```

## Instalación en Linux

Sigue estos pasos para configurar y ejecutar el proyecto en Linux:

1. Actualiza tu sistema y asegúrate de tener `pip` y `tkinter` instalados:
    ```sh
    sudo apt update
    sudo apt install python3-pip python3-tk -y
    ```

2. Crea un entorno virtual:
    ```sh
    python3 -m venv myenv
    ```

3. Verifica que el entorno virtual se creó correctamente:
    ```sh
    ls myenv
    ```

4. Activa el entorno virtual:
    ```sh
    source myenv/bin/activate
    ```

5. Instala los paquetes necesarios dentro del entorno virtual:
    ```sh
    pip install numpy==1.26.4 opencv-python==4.10.0.82 Pillow==10.3.0
    ```

Con estos pasos, tendrás todas las dependencias necesarias instaladas y podrás ejecutar el programa dentro del entorno virtual.
