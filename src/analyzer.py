import re
from textblob import TextBlob

def clean_text(text):
    """
    Limpia el texto de caracteres especiales, URLs y convierte a minúsculas.
    """
    if not isinstance(text, str):
        return ""
    text = re.sub(r'http\S+', '', text)  # Eliminar URLs
    text = re.sub(r'[^A-Za-z\s]', '', text)  # Eliminar caracteres no alfabéticos
    text = text.lower().strip()
    return text

def get_sentiment(text):
    """
    Analiza el sentimiento de un texto y lo clasifica como positivo, negativo o neutro.
    """
    cleaned_text = clean_text(text)
    analysis = TextBlob(cleaned_text)
    
    # La polaridad es un valor entre -1 (negativo) y 1 (positivo)
    if analysis.sentiment.polarity > 0.1:
        return 'positivo'
    elif analysis.sentiment.polarity < -0.1:
        return 'negativo'
    else:
        return 'neutro'

if __name__ == '__main__':
    # Ejemplo de uso
    sample_text = "Artificial Intelligence is transforming the world in amazing ways! #AI"
    sentiment = get_sentiment(sample_text)
    print(f"Texto: '{sample_text}'")
    print(f"Sentimiento: {sentiment}")

    sample_text_2 = "The new policy has been met with widespread criticism and anger."
    sentiment_2 = get_sentiment(sample_text_2)
    print(f"Texto: '{sample_text_2}'")
    print(f"Sentimiento: {sentiment_2}")
