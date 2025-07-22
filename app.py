import os
from dotenv import load_dotenv
from src.fetcher import get_news
from src.analyzer import get_sentiment
from src.summarizer import summarize_text
from src.visualizer import plot_sentiment_distribution
import pandas as pd

load_dotenv()

def main():
    """
    Función principal para orquestar la recolección, análisis, resumen y visualización de noticias.
    """
    QUERY = "elecciones presidenciales"
    
    if not os.getenv("NEWS_API_KEY"):
        print("Por favor, configura tu clave de API de NewsAPI.org en un archivo .env")
        return

    print(f"Buscando noticias sobre: '{QUERY}'...")
    articles = get_news(QUERY, language='es', page_size=50) # Aumentamos para tener más datos para el gráfico

    if not articles:
        print("No se encontraron artículos o hubo un error en la solicitud.")
        return

    news_data = []
    for article in articles:
        title = article.get('title', 'N/A')
        description = article.get('description', '')
        content = article.get('content', '')
        
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

    # Convertir a DataFrame de pandas
    df = pd.DataFrame(news_data)
    
    # Imprimir los resultados en consola
    print("\n--- Análisis de Noticias ---")
    for index, row in df.iterrows():
        print(f"Noticia #{index + 1}: {row['title']} ({row['sentiment']})")

    # Generar y guardar la visualización
    if not df.empty:
        plot_sentiment_distribution(df, QUERY)

if __name__ == '__main__':
    main()
