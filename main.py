# main.py

from pic_to_text import extract_isbn
from get_isbn_info import get_book_info
from ml_price_scrapper import get_ml_prices

def main():
    # Paso 1: Extraer ISBN de la cam
    isbn = extract_isbn()

    # Paso 2: Obtener información del libro
    book_info = get_book_info(isbn)

    print("\n\n -- INFORMACIÓN DEL LIBRO --\n")
    if book_info:
        title = book_info.get("title")
        authors = ", ".join(book_info.get("authors", []))
        publisher = book_info.get("publisher")

        # Paso 3: Obtener precios en Mercado Libre
        prices = get_ml_prices(title, authors, publisher)

        # Paso 4: Calcular precio promedio
        average_price = sum(prices) / len(prices)

        # Paso 5: Imprimir resultados
        print("Título:", title)
        print("Autor(es):", authors)
        print("Editorial:", publisher)
        print("Precio promedio en Mercado Libre:", average_price)
    else:
        print("No se encontró información para el ISBN proporcionado.")

    input()
    
if __name__ == "__main__":
    main()
