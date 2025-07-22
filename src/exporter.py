import pandas as pd
import os
from datetime import datetime

def export_to_csv(df, query):
    """
    Exporta un DataFrame a un archivo CSV.

    Args:
        df (pd.DataFrame): El DataFrame a exportar.
        query (str): La consulta de búsqueda original para nombrar el archivo.
    """
    if df.empty:
        print("El DataFrame está vacío. No se exportará ningún archivo.")
        return

    # Asegurarse de que el directorio de reportes exista
    if not os.path.exists('reports'):
        os.makedirs('reports')

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/analysis_results_{query}_{timestamp}.csv"
    
    try:
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"Resultados exportados correctamente a: {filename}")
    except Exception as e:
        print(f"Error al exportar a CSV: {e}")


if __name__ == '__main__':
    # Ejemplo de uso
    data = {
        'title': ['Noticia 1', 'Noticia 2'],
        'source': ['Fuente A', 'Fuente B'],
        'url': ['http://a.com', 'http://b.com'],
        'sentiment': ['positivo', 'negativo'],
        'summary': ['Resumen 1', 'Resumen 2']
    }
    sample_df = pd.DataFrame(data)
    export_to_csv(sample_df, "ejemplo_export")
