import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Importar datos
df = pd.read_csv("medical_examination.csv")

# 2. Agregar columna overweight (sobrepeso)
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2).apply(lambda x: 1 if x > 25 else 0)

# 3. Normalizar cholesterol y gluc: 0 = bueno, 1 = malo
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# 4. Función para dibujar el gráfico categórico
def draw_cat_plot():
    # 5. Crear DataFrame con melt para las variables categóricas
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )
    
    # 6. Agrupar y reformatear
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()
    
    # 7. Crear el catplot
    fig = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    ).fig
    
    # 9. No modificar
    fig.savefig('catplot.png')
    return fig


# 10. Función para dibujar el mapa de calor
def draw_heat_map():
    # 11. Limpiar datos
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &  # presión diastólica <= sistólica
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    
    # 12. Calcular matriz de correlación
    corr = df_heat.corr()
    
    # 13. Crear máscara para el triángulo superior
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # 14. Configurar la figura de matplotlib
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # 15. Dibujar el mapa de calor
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        center=0,
        square=True,
        linewidths=1,
        cbar_kws={'shrink': 0.5},
        ax=ax
    )
    
    # 16. No modificar
    fig.savefig('heatmap.png')
    return fig
