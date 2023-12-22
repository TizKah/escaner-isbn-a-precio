# Book Scanner and Price Analyzer

Este proyecto es una herramienta que utiliza la cámara de tu computadora para escanear el código de barras de un libro, extrae el ISBN, y luego utiliza este ISBN para obtener información del libro desde la API de Google Books. Además, obtiene los precios del libro en Mercado Libre y calcula el precio promedio.

## Requisitos

- Python 3.x
- Instalar las dependencias ejecutando `pip install -r requirements.txt`

## Configuración

Asegúrate de tener Tesseract OCR instalado. Puedes descargarlo desde [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).

## Uso

1. Ejecuta el archivo `main.py`.
2. La cámara se activará, escanea el código de barras del libro.
3. Espera a que el programa extraiga la información del libro y muestre los resultados.

## Estructura del Proyecto

- **pic_to_text.py:** Contiene funciones para extraer el ISBN de la cámara.
- **get_isbn_info.py:** Obtiene información del libro usando el ISBN.
- **ml_price_scrapper.py:** Obtiene precios del libro en Mercado Libre.
- **main.py:** El punto de entrada principal que utiliza las funciones anteriores para mostrar la información del libro y los precios en Mercado Libre.

## Atribuciones

- **pytesseract:** Herramienta para interactuar con Tesseract OCR.
- **pyzbar:** Librería para decodificar códigos de barras en imágenes.
- **requests:** Para realizar solicitudes HTTP a la API de Google Books y Mercado Libre.

## Contribuciones

Siéntete libre de contribuir al proyecto. Puedes hacer mejoras en el código, agregar nuevas características o corregir problemas.

## Licencia

Este proyecto está bajo la Licencia [MIT](LICENSE).
