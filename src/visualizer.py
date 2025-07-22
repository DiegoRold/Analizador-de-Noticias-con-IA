import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from datetime import datetime

def plot_sentiment_distribution(df, query):
    """
    Crea y guarda un gráfico de barras mostrando la distribución de sentimientos.

    Args:
        df (pd.DataFrame): El DataFrame con los datos de las noticias, debe incluir una columna 'sentiment'.
        query (str): La consulta de búsqueda original para titular el gráfico y el archivo.
    """
    if 'sentiment' not in df.columns:
        print("El DataFrame no contiene la columna 'sentiment'. No se puede generar el gráfico.")
        return

    # Asegurarse de que el directorio de reportes exista
    if not os.path.exists('reports'):
        os.makedirs('reports')

    plt.style.use('seaborn-v0_8-darkgrid')
    fig, ax = plt.subplots(figsize=(10, 6))

    sns.countplot(
        x='sentiment', 
        data=df, 
        ax=ax, 
        palette=['#4CAF50', '#FFC107', '#F44336'], 
        order=['positivo', 'neutro', 'negativo'],
        hue='sentiment', # Añadido para la nueva versión de seaborn
        legend=False     # Oculta la leyenda redundante
    )

    ax.set_title(f'Distribución de Sentimiento para Noticias sobre "{query.title()}"', fontsize=16)
    ax.set_xlabel('Sentimiento', fontsize=12)
    ax.set_ylabel('Número de Noticias', fontsize=12)
    ax.tick_params(axis='x', rotation=0)

    # Añadir el número exacto encima de cada barra
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', 
                    xytext=(0, 9), 
                    textcoords='offset points')

    # Guardar el gráfico
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/sentiment_distribution_{query}_{timestamp}.png"
    plt.savefig(filename, bbox_inches='tight')
    plt.close() # Cerrar la figura para liberar memoria

    print(f"\nGráfico de distribución de sentimiento guardado en: {filename}")


if __name__ == '__main__':
    # Ejemplo de uso
    data = {
        'title': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        'sentiment': ['positivo', 'neutro', 'negativo', 'neutro', 'positivo', 'positivo', 'neutro']
    }
    sample_df = pd.DataFrame(data)
    plot_sentiment_distribution(sample_df, "ejemplo")
