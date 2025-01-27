import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo CSV con separador correcto
archivo_csv = "datos.csv"
df = pd.read_csv(archivo_csv, sep=";")  # El separador es ';'

# Convertir columna de duración de la llamada a segundos
def convertir_a_segundos(duracion):
    partes = duracion.split(":")
    return int(partes[0]) * 60 + int(partes[1])

df["Duración de la llamada (s)"] = df["Duración de la llamada"].apply(convertir_a_segundos)

# Configuración global para mejorar estilo de gráficos
sns.set_theme(style="whitegrid", palette="pastel")

# Graficar índice de satisfacción por área
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="Área", y="Índice de satisfacción", palette="coolwarm", showmeans=True, 
            meanprops={"marker": "o", "markerfacecolor": "white", "markeredgecolor": "black"})
plt.title("Distribución del Índice de Satisfacción por Área", fontsize=14, fontweight='bold')
plt.ylabel("Índice de Satisfacción", fontsize=12)
plt.xlabel("Área", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Graficar duración promedio con asistente por área
duracion_por_area = df.groupby("Área")["Duración con asistente en segundos"].mean().sort_values()
plt.figure(figsize=(8, 6))
bars = plt.bar(duracion_por_area.index, duracion_por_area.values, color="skyblue", edgecolor="black")
plt.title("Duración Promedio con Asistente por Área", fontsize=14, fontweight='bold')
plt.ylabel("Duración promedio (segundos)", fontsize=12)
plt.xlabel("Área", fontsize=12)
plt.xticks(rotation=45)
for bar in bars:  # Añadir etiquetas en las barras
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 5, round(yval, 1), ha="center", fontsize=10)
plt.tight_layout()
plt.show()

# Graficar la relación entre velocidad de respuesta e índice de satisfacción
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Velocidad de respuesta", y="Índice de satisfacción", hue="Área", 
                palette="viridis", size="Duración con asistente en segundos", sizes=(20, 200), alpha=0.7)
plt.title("Relación entre Velocidad de Respuesta e Índice de Satisfacción", fontsize=14, fontweight='bold')
plt.xlabel("Velocidad de Respuesta", fontsize=12)
plt.ylabel("Índice de Satisfacción", fontsize=12)
plt.legend(title="Área", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
