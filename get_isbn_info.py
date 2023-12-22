# get_isbn_info.py

import requests

def get_book_info(isbn):
    api_url = f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&maxResults=1"
    response = requests.get(api_url)
    book_info = response.json()

    # Verifica si hay resultados y toma el primer elemento
    if "items" in book_info and book_info["totalItems"] > 0:
        book_volume = book_info["items"][0]["volumeInfo"]

        # Verifica si los campos requeridos están presentes
        title = book_volume.get("title")
        authors = book_volume.get("authors", [])
        publisher = book_volume.get("publisher")

        # Retorna un diccionario con la información
        return {"title": title, "authors": authors, "publisher": publisher}
    else:
        # Retorna None si no se encontraron resultados
        return None