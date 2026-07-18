# Prueba del Medical Data Visualizer
from medical_data_visualizer import draw_cat_plot, draw_heat_map

print("Generando gráfico categórico...")
fig_cat = draw_cat_plot()
print("✅ catplot.png generado")

print("Generando mapa de calor...")
fig_heat = draw_heat_map()
print("✅ heatmap.png generado")
