from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
import nltk

# Descargar los recursos necesarios de NLTK la primera vez
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# Para el español, sumy requiere un recurso adicional de NLTK.
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

def summarize_text(text, sentences_count=3, language="spanish"):
    """
    Genera un resumen extractivo de un texto.

    Args:
        text (str): El texto a resumir.
        sentences_count (int, optional): El número de oraciones en el resumen. Defaults to 3.
        language (str, optional): El idioma del texto para el tokenizador. Defaults to "spanish".

    Returns:
        str: El texto resumido.
    """
    if not isinstance(text, str) or not text.strip():
        return ""

    parser = PlaintextParser.from_string(text, Tokenizer(language))
    summarizer = Summarizer()
    summary = summarizer(parser.document, sentences_count)
    
    # Concatenar las oraciones del resumen
    summarized_text = " ".join([str(sentence) for sentence in summary])
    return summarized_text

if __name__ == '__main__':
    # Ejemplo de uso
    sample_text = (
        "La inteligencia artificial (IA) es un campo de la informática que se centra en la creación de sistemas "
        "que pueden realizar tareas que normalmente requieren inteligencia humana. Estas tareas incluyen el aprendizaje, "
        "el razonamiento, la resolución de problemas, la percepción, el reconocimiento del habla y la traducción de idiomas. "
        "La IA tiene aplicaciones en una amplia variedad de industrias, desde la atención médica y las finanzas hasta "
        "el transporte y el entretenimiento. A medida que la tecnología continúa avanzando, se espera que el impacto "
        "de la IA en la sociedad crezca exponencialmente, presentando tanto oportunidades como desafíos significativos."
    )
    
    summary = summarize_text(sample_text, sentences_count=2)
    
    print("--- Texto Original ---")
    print(sample_text)
    print("\n--- Resumen ---")
    print(summary)
