# Este archivo es para probar tu código
from mean_var_std import calculate

# Prueba con el ejemplo que da freeCodeCamp
result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print("Resultado:")
print(result)

print("\n---")
# Prueba con ValueError
try:
    calculate([1, 2, 3])
except ValueError as e:
    print(f"Error correcto: {e}")
