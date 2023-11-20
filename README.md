# Descargador MP3 de YouTube

Esta aplicación en Python te permite descargar listas de reproducción de YouTube en formato MP3 utilizando la biblioteca Pytube.

## Requisitos Previos:
- Python 3.x instalado en tu sistema. Puedes descargarlo [aquí](https://www.python.org/downloads/).
- Asegúrate de tener una conexión a Internet estable durante el proceso de descarga.

## Estructura del Proyecto:

- `main.py`: Script principal que ejecuta la aplicación con una interfaz gráfica.
- `requirements.txt`: Archivo que lista las dependencias del proyecto.
- `.gitignore`: Configuración para ignorar archivos y directorios específicos al usar Git.

## Uso

1. Clona el repositorio:

    ```bash
    git clone <enlace del repositorio>
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd <nombre del proyecto>
    ```

3. Crea un entorno virtual (opcional pero recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # Para sistemas basados en Unix
    # o
    venv\Scripts\activate  # Para Windows
    ```

4. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

5. Ejecuta la aplicación:

    ```bash
    python main.py
    ```

Se abrirá una ventana con la interfaz gráfica de la aplicación. Ingresa la URL de la lista de reproducción de YouTube en el campo correspondiente, selecciona la carpeta de destino y haz clic en "Descargar MP3" para iniciar el proceso de descarga.

## Contribuciones

¡Contribuciones son bienvenidas! Si encuentras algún problema o tienes alguna mejora, por favor, crea un problema o envía una solicitud de extracción.

