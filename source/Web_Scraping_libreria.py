
# ************ Sección 1: Importación de librerías ************ #

# Se importan las librerías necesarias para el proyecto

# librerías "estándar" de python
import os  # usado para la gestión de archivos y rutas (exportar csv)
import time # controla tiempos de espera durante la ejecución

# librerías para análisis y procesamiento de datos
import pandas as pd  # Manipulación y exportación de datos en formato CSV

# librerías de scraping
from selenium import webdriver  # Control del navegador (Chrome)
from selenium.webdriver.chrome.options import Options # Configurar opciones del Chrome para Selenium
from bs4 import BeautifulSoup # # Analizar y extraer datos del HTML obtenido


# ************ Sección 2: Configuración de Selenium y navegación ************ #

# Configuración para ignorar errores de SSL
chrome_options = Options()  # Inicia las opciones de configuración de Chrome
chrome_options.add_argument('--ignore-certificate-errors') 
chrome_options.add_argument('--ignore-ssl-errors')

# Establecer el User-Agent  (fuente: https://www.whatismybrowser.com/w/XQ429LH)
chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36')

# Se incializa el WebDriver con las opciones configuradas
driver = webdriver.Chrome(options=chrome_options) # inicia el navegador con las anteriores configuraciones


# ************ Sección 3: Navegación en la página y captura de HTML ************ #

# Lectura del sitio web de la tienda de libros Buscalibre
url_principal = "https://www.buscalibre.com.co"
driver.get(url_principal) # Abre el sitio en el navegador (controlado por Selenium)
time.sleep(7)  # Pausa para cargar la página principal (es posible adapatar dependiendo de la veloocidad del internet)

# Captura el HTML de la página principal
html = driver.page_source  # obtiene el html de la págona
print("HTML capturado correctamente.") # mensaje de confirmación de lectura
soup = BeautifulSoup(html, "lxml") # BeautifulSoup crea un objeto para analizar el HTML (parser o analizador)


# ************ Sección 4: Extracción de categorías ************ #

# Búsqueda y extracción de las categorías dentro de la página
categoria_enlaces = soup.select('div#categoriasdeployed ul li a') # busca todos los enlaces y las etiquetas de categorías dentro de su respectivo contenedor
categorias = [] # inicializa una lista vacía donde se almacenarán las categorías y sus enlaces

# Se extrae los enlaces de cada categoría
for enlace in categoria_enlaces:
    link = enlace.get('href') # obtiene el enlace de la categoría
    nombre_categoria = enlace.get_text(strip=True) # obtiene el nombre y elimina espacios demás
    categorias.append((nombre_categoria, link))# se almacena la tupla de nombre y enlace en la lista "categorias"

# se crea una lista para almacenar todos los datos de los libros
data_total = []


# ************ Sección 5: Navegación por categorías y extracción de datos de los libros ************ #

# Se navega por cada categoría y extrae los datos de los libros
for nombre_categoria, link in categorias:
    print(f"Extrayendo datos de la categoría: {nombre_categoria}")
    driver.get(link) # Navega a la URL de la categoría
    time.sleep(5)  # Pausa para cargar la página de la categoría

    html_categoria = driver.page_source # Captura el HTML de la página de la categoría
    soup_categoria = BeautifulSoup(html_categoria, "lxml") # parser del html de la categoría respectiva


# ************ Sección 6: Extracción de datos de los libros ************ #

    # Encuentra todos los contenedores de los libros en la categoría
    libros = soup_categoria.find_all('div', class_='box-producto')

    # Extrae la información de cada libro
    for libro in libros:
        id_producto = libro.get('data-id_producto', 'ID no disponible') # selecciona el id del libro
        costo = libro.get('data-precio', 'Costo no disponible') # se presume que es el costo del libro 
        isbn = libro.get('data-isbn', 'ISBN no disponible') # el isbn


        # Extrae el título ( Intenta encontrar el atributo title del enlace (<a>))
        enlace_titulo = libro.find('a') # Encuentra la etiqueta <a> que contiene el título del libro
        if enlace_titulo: 
            titulo = enlace_titulo.get('title').strip() # también se elimina espacios en blanco extras
        else:
            titulo = "Título no disponible" # Si no se encuentra el título, asigna un valor por defecto


        # Extrae el autor
        div_autor = libro.find('div', class_='autor') # busca el autor dentro de la etiqueta <div> con la clase autor.
        if div_autor:
            autor = div_autor.text.strip() # .text para extraer solo el contenido textual de la etiqueta HTML
        else:
            autor = "Autor no disponible"


        # Extrae el número de calificaciones
        span_calificaciones = libro.find('span', class_='color-dark-gray font-weight-light margin-left-5 font-size-small') # Busca el contenedor del autor dentro del libro
        if span_calificaciones:
            calificaciones = span_calificaciones.get_text(strip=True).replace('(', '').replace(')', '') # Extrae el texto y elimina paréntesis
        else:
            calificaciones = "Calificaciones no disponibles"

        
        # Extrae el número de unidades restantes
            # Busca el <div> que contiene el número de unidades restantes, identificado por la clase (stock hide...)
        div_stock = libro.find('div', class_='stock hide-on-hover color-green font-size-small margin-top-5')
        if div_stock:
            unidades = div_stock.get_text(strip=True).replace('Quedan', '').replace('unidades', '').strip() # se elimina las palabras quedan y unidades (para extraer el número)
        else:
            unidades = "Unidades no disponibles"


        # Extrae el porcentaje de descuento
           # Buscar un bloque <div> que contenga el porcentaje de descuento
        div_descuento = libro.find('div', class_='descuento-v2 color-white position-relative')
        if div_descuento:
            descuento = div_descuento.get_text(strip=True)
        else:
            descuento = "Descuento no disponible"


        # Extrae el precio antes del descuento
           # Busca el contenedor <p> con la clase precio-antes, (allí está el precio original)
        p_precio_antes = libro.find('p', class_='precio-antes')
        if p_precio_antes:
            del_tag = p_precio_antes.find('del') # busca dentro de la etiqueta del (para tachar en html, señala el precio original)
            if del_tag:
                precio_sin_dcto = del_tag.get_text(strip=True) # si encuentra la etieuta del extrae el precio
            else:
                precio_sin_dcto = "Precio sin descuento no disponible"
        else:
            precio_sin_dcto = "Precio sin descuento no disponible"


        # Extrae el precio con descuento
        p_precio_ahora = libro.find('p', class_='precio-ahora') # busca el contenedor libro un parrafo "p" con la clase del precio ahora 
        if p_precio_ahora:
            strong_tag = p_precio_ahora.find('strong')
            if strong_tag:
                precio_actual = strong_tag.get_text(strip=True) # extrae el texto que esta en la etiqueta strong (donde está el precio)
            else:
                precio_actual = "Precio actual no disponible"
        else:
            precio_actual = "Precio actual no disponible"


# ************ Sección 7: Almacenamiento de los datos ************ #

# Se añade un diccionario con los datos extraídos a la lista "data_total"
        data_total.append({
            'Categoría': nombre_categoria,
            'ID Producto': id_producto,
            'Costo estimado': costo,
            'ISBN': isbn,
            'Título': titulo,
            'Autor': autor,
            'Calificaciones': calificaciones,
            'Unidades Restantes': unidades,
            'Descuento': descuento,
            'Precio Anterior': precio_sin_dcto,
            'Precio Actual': precio_actual
        })

# Cierra el navegador
driver.quit()


# ************ Sección 8: Guardado en CSV ************ #

# DataFrame de pandas a partir de los datos recolectados
df = pd.DataFrame(data_total)

# Guardar el archivo CSV en la misma carpeta donde se encuentra el script
script_directory = os.path.dirname(os.path.abspath(__file__))  # Obtiene la ubicación del script 
filename = os.path.join(script_directory, "datos_libros_categorias.csv") # "construye" la ruta con la variable que contiene la ubicación del script y da nombre al archivo

# Guardar el DataFrame en el archivo CSV
df.to_csv(filename, index=False, encoding='utf-8-sig') # convierte el set de datos en csv (se pasa la ruta y la codificación)

# Confirmación de la ubicación donde se guardó el archivo
print(f"Archivo CSV generado exitosamente en: {filename}") 

