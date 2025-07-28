import re
from transformers import pipeline

# Cargar el pipeline de análisis de sentimiento solo una vez.
# La primera vez que se ejecute, descargará el modelo (aprox. 400-500 MB).
print("Cargando modelo de análisis de sentimiento... (Esto puede tardar un momento la primera vez)")
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model="pysentimiento/robertuito-sentiment-analysis"
)
print("¡Modelo cargado con éxito!")


def clean_text(text):
    """
    Limpia el texto de caracteres especiales, URLs y convierte a minúsculas.
    """
    if not isinstance(text, str):
        return ""
    # Esta limpieza es menos agresiva para no perder contexto para el modelo transformer
    text = re.sub(r'http\S+', '', text)  # Eliminar URLs
    text = text.strip()
    return text

def get_sentiment(text):
    """
    Analiza el sentimiento de un texto usando un modelo Transformer (robertuito).
    """
    if not text:
        return 'neutro'

    cleaned_text = clean_text(text)
    
    # El modelo puede manejar hasta 512 tokens. Truncamos para evitar errores.
    truncated_text = cleaned_text[:512]

    try:
        result = sentiment_analyzer(truncated_text)
        # Mapear la etiqueta del modelo a nuestras etiquetas
        label_map = {
            'POS': 'positivo',
            'NEU': 'neutro',
            'NEG': 'negativo'
        }
        return label_map.get(result[0]['label'], 'neutro')
    except Exception as e:
        print(f"Error durante el análisis de sentimiento: {e}")
        return 'neutro'

if __name__ == '__main__':
    # Ejemplo de uso
    sample_text_1 = "Este servicio es una maravilla, ¡estoy encantado con los resultados!"
    sentiment_1 = get_sentiment(sample_text_1)
    print(f"Texto: '{sample_text_1}'")
    print(f"Sentimiento (Robertuito): {sentiment_1}")

    sample_text_2 = "La película fue aburrida y predecible, no la recomendaría en absoluto."
    sentiment_2 = get_sentiment(sample_text_2)
    print(f"Texto: '{sample_text_2}'")
    print(f"Sentimiento (Robertuito): {sentiment_2}")

    sample_text_3 = "El presidente anunció nuevas medidas económicas durante la conferencia de prensa."
    sentiment_3 = get_sentiment(sample_text_3)
    print(f"Texto: '{sample_text_3}'")
    print(f"Sentimiento (Robertuito): {sentiment_3}")
