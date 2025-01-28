# Análisis de Ventas

Este proyecto realiza un análisis de ventas a partir de un archivo CSV y genera gráficos para visualizar los resultados.

## Estructura del Proyecto

- `analisis_ventas.py`: Script de Python que realiza el análisis de ventas.
- `ventas.csv`: Archivo CSV que contiene los datos de ventas.
- `LICENSE`: Archivo que contiene la licencia del proyecto.

## Requisitos

- Python 3.x
- Pandas
- Matplotlib

Puedes instalar las dependencias necesarias ejecutando:

```sh
pip install pandas matplotlib
```

## Resultados del Análisis

Columnas en el archivo CSV: Index(['Producto', 'Cantidad', 'Precio'], dtype='object')
Primeras filas de los datos:
   Producto  Cantidad  Precio
0  Camiseta        20     200
1  Pantalon        10     500
2   Zapatos         5     300
3  Camiseta        15     100
4  Pantalon         7     250

=== Reporte de Ventas ===
Total de ventas por producto:
Producto
Camiseta    5500
Pantalon    6750
Zapatos     5250
Name: Total, dtype: int64

Producto más vendido: Pantalon con un total de $6750
Promedio de ventas: $3500.00
Gráficos
El script generará dos gráficos:

Gráfico de barras para el total de ventas por producto.
Gráfico de pie para mostrar el porcentaje de cada producto en las ventas.

## Licencia

Este proyecto está bajo la Licencia MIT. Puedes ver el archivo de licencia en `LICENSE`.



## Otros Archivos

- `README.md`: Archivo que contiene la documentación del proyecto.
- `requirements.txt`: Archivo que lista las dependencias del proyecto.
- `data/`: Directorio que contiene archivos de datos adicionales.

## Análisis Adicional

Además del análisis de ventas, el proyecto puede realizar los siguientes análisis adicionales:

### Análisis de Tendencias

Este análisis identifica las tendencias de ventas a lo largo del tiempo. Se puede generar un gráfico de líneas para visualizar cómo cambian las ventas de cada producto mes a mes.

### Análisis de Clientes

Este análisis se enfoca en identificar los patrones de compra de los clientes. Se puede generar un gráfico de barras para mostrar la cantidad de productos comprados por cada cliente.

### Análisis de Descuentos

Este análisis evalúa el impacto de los descuentos en las ventas. Se puede generar un gráfico de barras para comparar las ventas con y sin descuentos.

Para ejecutar estos análisis adicionales, puedes modificar el script `analisis_ventas.py` o crear nuevos scripts específicos para cada análisis.