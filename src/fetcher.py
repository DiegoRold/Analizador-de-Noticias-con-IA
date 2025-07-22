import os
from newsapi import NewsApiClient
from dotenv import load_dotenv

load_dotenv()

def get_news(query, language='en', page_size=100):
    """
    Obtiene noticias utilizando la API de NewsAPI.

    Args:
        query (str): La palabra clave para buscar.
        language (str, optional): El idioma de las noticias. Defaults to 'en'.
        page_size (int, optional): El número de resultados a devolver por página. Defaults to 100.

    Returns:
        list: Una lista de artículos o None si ocurre un error.
    """
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        raise ValueError("No se encontró la clave de API. Asegúrate de que el archivo .env existe y contiene NEWS_API_KEY.")

    try:
        newsapi = NewsApiClient(api_key=api_key)
        all_articles = newsapi.get_everything(q=query,
                                              language=language,
                                              sort_by='relevancy',
                                              page_size=page_size)
        return all_articles['articles']
    except Exception as e:
        print(f"Error al obtener noticias: {e}")
        return None
