# Prueba del Time Series Visualizer
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

print("Generando gráfico de líneas...")
fig_line = draw_line_plot()
print("✅ line_plot.png generado")

print("Generando gráfico de barras...")
fig_bar = draw_bar_plot()
print("✅ bar_plot.png generado")

print("Generando diagramas de caja...")
fig_box = draw_box_plot()
print("✅ box_plot.png generado")
