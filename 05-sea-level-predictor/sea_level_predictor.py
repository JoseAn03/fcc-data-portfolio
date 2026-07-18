import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Importar datos
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Diagrama de dispersión
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], 
               color='blue', alpha=0.6, s=30, label='Datos originales')

    # 3. Línea de mejor ajuste (todos los datos, hasta 2050)
    reg1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = range(1880, 2051)
    y1 = reg1.slope * x1 + reg1.intercept
    ax.plot(x1, y1, color='red', linewidth=2, label='Tendencia 1880-2050')

    # 4. Línea de mejor ajuste (solo desde 2000 hasta 2050)
    df_2000 = df[df['Year'] >= 2000]
    reg2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x2 = range(2000, 2051)
    y2 = reg2.slope * x2 + reg2.intercept
    ax.plot(x2, y2, color='green', linewidth=2, label='Tendencia 2000-2050')

    # 5. Etiquetas y título
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Guardar y retornar
    fig.savefig('sea_level_plot.png')
    return fig
