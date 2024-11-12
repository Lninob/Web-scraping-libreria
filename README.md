# Práctica 1: Web scraping

## Descripción

Este proyecto se enmarca dentro de la asignatura "Tipología y Ciclo de Vida de los Datos", del Máster en Ciencia de Datos de la Universitat Oberta de Catalunya. El objetivo principal es aplicar técnicas de web scraping para extraer datos de los libros disponibles en las diversas categorías de la librería en línea Buscalibre. Los datos extraídos serán procesados y organizados en un conjunto de datos estructurado que servirá como base para futuros análisis. (El proyecto está desarrollado en python)

## Integrantes del grupo:
* Lady Carolina Niño Beltrán
* Daniel Leonardo Martinez Ruiz

## Descripción archivos del repositorio:

El repositorio contiene los siguientes archivos:

* **README.md:** Documento con la descripción del proyecto, los detalles del código, las instrucciones de uso, y otros apartados relevantes.
* **/source:** Carpeta que contiene el código Python implementado para la obtención de los datos mediante técnicas de web scraping desde el sitio web de Buscalibre.
* **/dataset:** Carpeta que contiene el conjunto de datos resultante, guardado en formato CSV. Este archivo es el producto final de la extracción de datos.

### Archivos y complementos

**/complementos:**

* **WebDriver (para Chrome):** Se adjunta el ChromeDriver para la versión de Chrome 130.0.6723... Si se desea obtener el WebDriver para una versión diferente de Chrome, puedes consultar los siguientes enlaces:
  * Para versiones anteriores a la 115, puedes obtenerlo en [ChromeDriver Downloads](https://sites.google.com/chromium.org/driver/downloads).
  * Para versiones 115 en adelante, consulta [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/).
* **requirements.txt:** Archivo con las librerías necesarias para ejecutar el código de este repositorio.
* **Informe pdf:** Contiene el informe en pdf del proyecto.

## Enlaces:
* **Doi Zenodo:** [https://doi.org/10.5281/zenodo.14079106](https://doi.org/10.5281/zenodo.14079106)
* **Enlace video:** video alojado en [https://drive.google.com/file/d/187GOLEZyD030NRyMAKHsmkC89-CIrBGi/view?usp=sharing](GoogleDrive) o en disponible en [https://youtu.be/VFXW1eVO864](Youtube)
* Página web: https://www.buscalibre.com.co/
* Repositorio en github: https://github.com/Lninob/Web-scraping-libreria/ 


## Instrucciones para ejecutar el código:

**Se recomienda tener Python 3.6 o superior**

### 1. Requisitos previos

Antes de ejecutar el código, es necesario descargar los siguientes archivos en la misma carpeta:

* **Web_Scaping_libreria.py:** El script de Python que realiza la recolección de datos mediante web scraping.
* **chromedriver.exe:** El WebDriver de Chrome, necesario para que Selenium interactúe con el navegador Chrome. (descargar la versión correspondiente al navegador según lo indicado anteriormente)
* **requirements.txt:** Archivo que contiene la lista de librerías necesarias para ejecutar el código del proyecto.

### 2. Instalación de dependencias

Para instalar las librerías necesarias, abrir la terminal o línea de comandos y navegar hasta la carpeta donde se encuentran los archivos y ejecutar el siguiente comando:
`pip install -r requirements.txt`

### 3. Ejecución del código

Una vez descargados y configurados todos los archivos en la misma carpeta, ejecutar el siguiente comando en la terminal para iniciar el script Python `Web_Scaping_libreria.py` o ejecutar el archivo en el IDE de preferencia como por ejemplo Visual Studio Code

Este comando ejecutará el proceso de web scraping.

El script hará lo siguiente:

* Cargar la página principal de Buscalibre.
* Extraer las categorías disponibles.
* Navegar por cada categoría y extraer información de los libros (como el título, autor, ISBN, precio, etc.).

**NOTA:** El script guarda los datos extraídos en un archivo CSV en la misma carpeta donde se encuentra el script.

## Ejemplo de salida

Al ejecutar el script, se generará un archivo `datos_libros_categorias.csv` dentro de la carpeta con todos los datos extraídos, incluyendo las siguientes columnas:

* Categoría
* ID Producto
* Costo estimado
* ISBN
* Título
* Autor
* Calificaciones
* Unidades restantes
* Descuento
* Precio anterior
* Precio actual

## Notas adicionales

* **Tiempo de ejecución:** El tiempo de ejecución puede variar según la velocidad de la conexión a internet y el número de categorías que el script deba procesar.
* **Interacción con el sitio web:** El script simula la navegación de un usuario real y puede estar sujeto a cambios en la estructura del sitio web de Buscalibre. Si el sitio cambia, puede ser necesario actualizar las funciones de extracción de datos.



