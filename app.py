import os
from dotenv import load_dotenv
from src.fetcher import get_news
from src.analyzer import get_sentiment
from src.summarizer import summarize_text
import pandas as pd

load_dotenv()

def main():
    """
    Función principal para orquestar la recolección, análisis y resumen de noticias.
    """
    QUERY = "ciberseguridad"
    
    if not os.getenv("NEWS_API_KEY"):
        print("Por favor, configura tu clave de API de NewsAPI.org en un archivo .env")
        return

    print(f"Buscando noticias sobre: '{QUERY}'...")
    articles = get_news(QUERY, language='es', page_size=10) # Reducido a 10 para una demo más rápida

    if not articles:
        print("No se encontraron artículos o hubo un error en la solicitud.")
        return

    news_data = []
    for article in articles:
        title = article.get('title', 'N/A')
        description = article.get('description', '')
        content = article.get('content', '')
        
        # Priorizar contenido, luego descripción, para el análisis y resumen
        text_to_analyze = content if content and len(content) > 100 else description
        
        sentiment = get_sentiment(text_to_analyze)
        summary = summarize_text(text_to_analyze, sentences_count=2)
        
        news_data.append({
            'title': title,
            'source': article.get('source', {}).get('name', 'N/A'),
            'url': article.get('url', ''),
            'sentiment': sentiment,
            'summary': summary
        })

    # Convertir a DataFrame de pandas para una mejor visualización
    df = pd.DataFrame(news_data)
    
    # Imprimir los resultados de una forma más legible
    print("\n--- Análisis de Noticias ---")
    for index, row in df.iterrows():
        print(f"Noticia #{index + 1}")
        print(f"  Título: {row['title']}")
        print(f"  Sentimiento: {row['sentiment']}")
        print(f"  Resumen: {row['summary']}")
        print("-" * 30)


if __name__ == '__main__':
    main()
