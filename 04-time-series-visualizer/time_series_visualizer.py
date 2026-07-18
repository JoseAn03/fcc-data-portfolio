import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# 1. Importar datos
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

# 2. Limpiar datos (filtrar percentiles 2.5 y 97.5)
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

# 3. Gráfico de líneas
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(16, 6))
    
    ax.plot(df.index, df['value'], color='red', linewidth=0.8)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    fig.savefig('line_plot.png')
    return fig

# 4. Gráfico de barras
def draw_bar_plot():
    # Preparar datos: promedio por mes y año
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean()
    df_bar = df_bar.unstack()
    
    # Crear figura
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Colores para cada mes
    month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    df_bar.plot(kind='bar', ax=ax, legend=True)
    
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', labels=month_names)
    
    fig.savefig('bar_plot.png')
    return fig

# 5. Diagramas de caja
def draw_box_plot():
    # Preparar datos
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    # Orden de meses
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    
    # Crear figura con dos subplots
    fig, axes = plt.subplots(1, 2, figsize=(20, 8))
    
    # Year-wise box plot
    sns.boxplot(data=df_box, x='year', y='value', ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    # Month-wise box plot
    sns.boxplot(data=df_box, x='month', y='value', order=month_order, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    
    fig.savefig('box_plot.png')
    return fig
