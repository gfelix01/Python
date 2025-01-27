import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo CSV con el delimitador correcto
archivo_csv = 'D:/Python/ventas.csv'

# Especificar el delimitador como punto y coma ';'
datos = pd.read_csv(archivo_csv, delimiter=';')

# Eliminar los espacios en blanco de las columnas
datos.columns = datos.columns.str.strip()

# Verificar si las columnas están correctamente leídas
print("Columnas en el archivo CSV:", datos.columns)
print("Primeras filas de los datos:")
print(datos.head())

# Calcular el total de ventas por producto
def calculate_total(datos):
    datos['Total'] = datos['Cantidad'] * datos['Precio']

calculate_total(datos)
ventas_por_producto = datos.groupby('Producto')['Total'].sum()

# Producto más vendido
producto_mas_vendido = ventas_por_producto.idxmax()
ventas_maximas = ventas_por_producto.max()

# Promedio de ventas
promedio_ventas = datos['Total'].mean()

# Imprimir resultados
print("=== Reporte de Ventas ===")
print("Total de ventas por producto:")
print(ventas_por_producto)
print(f"\nProducto más vendido: {producto_mas_vendido} con un total de ${ventas_maximas}")
print(f"Promedio de ventas: ${promedio_ventas:.2f}")

# Graficar los resultados
plt.figure(figsize=(8, 6))

# Gráfico de barras para el total de ventas por producto
ventas_por_producto.plot(kind='bar', color='skyblue')

# Etiquetas y título
plt.title("Total de Ventas por Producto")
plt.xlabel("Producto")
plt.ylabel("Ventas Totales ($)")
plt.xticks(rotation=45)

# Mostrar el gráfico
plt.tight_layout()
plt.show()

# Gráfico de pie para mostrar el porcentaje de cada producto en las ventas
plt.figure(figsize=(6, 6))
ventas_por_producto.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightgreen', 'lightcoral', 'lightskyblue'])

# Título del gráfico
plt.title("Porcentaje de Ventas por Producto")

# Mostrar el gráfico de pie
plt.show()
