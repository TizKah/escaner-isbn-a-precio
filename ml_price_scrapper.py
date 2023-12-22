# ml_price_scrapper.py

import requests

def get_ml_prices(title, author, publisher):
    mercado_libre_api_url = "https://api.mercadolibre.com/sites/MLA/search"
    
    params = {
        "q": f"{title} {author} {publisher}",
        "category": "MLA119871",  # Categoría de libros usados en Mercado Libre
    }

    ml_response = requests.get(mercado_libre_api_url, params=params)
    ml_results = ml_response.json()

    prices = [result["price"] for result in ml_results["results"][:3]]
    return prices
