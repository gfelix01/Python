# 📊 **Análisis de Datos de Atención al Cliente con Python**

Este proyecto se centra en el análisis y visualización de datos de atención al cliente para identificar áreas de mejora en el servicio. A través del procesamiento de métricas clave, como la duración de las llamadas, la velocidad de respuesta y el índice de satisfacción, buscamos obtener insights valiosos para optimizar la experiencia del cliente.

## 🚀 **Objetivo del Proyecto**
El objetivo principal es descubrir patrones y áreas de mejora en la atención al cliente mediante el análisis de datos, para ayudar a las empresas a tomar decisiones informadas y mejorar su servicio.

---

## 🛠️ **Tecnologías y Herramientas Utilizadas**
- **Lenguaje:** Python 🐍
- **Bibliotecas:**
  - [Pandas](https://pandas.pydata.org/): Para el procesamiento y análisis de datos.
  - [Matplotlib](https://matplotlib.org/) y [Seaborn](https://seaborn.pydata.org/): Para la visualización de datos.
- **Entorno de Desarrollo:** Jupyter Notebook

---

## 📂 **Estructura del Proyecto**
- `datos.csv`: Dataset que contiene las métricas de las llamadas.
- `analisis_datos.py`: Script principal que ejecuta el análisis y genera las visualizaciones.
- `README.md`: Documento con la descripción del proyecto y las instrucciones.
- `grafico_1.png`, `grafico_2.png`, `grafico_3.png`: Imágenes de los gráficos generados.

---

## 📋 **Descripción del Dataset**
El archivo `datos.csv` contiene las siguientes columnas:
- **Id Llamada:** Identificador único para cada llamada.
- **Fecha:** Fecha de la llamada.
- **Asistente:** Nombre del asistente que atendió la llamada.
- **Área:** Departamento al que pertenece la llamada (Ej. Ventas, Reclamos, Cancelaciones).
- **Respondido - Resuelto (S/N):** Si la llamada fue resuelta o no.
- **Velocidad de respuesta (segundos):** Tiempo en segundos que tardó en responder la llamada.
- **Duración de la llamada:** Tiempo total de la llamada en formato `mm:ss`.
- **Duración con asistente (segundos):** Tiempo que el cliente estuvo en conversación con el asistente.
- **Índice de satisfacción:** Calificación del cliente de 1 a 5.

---

## 📊 **Visualizaciones Incluidas**
1. **Distribución del Índice de Satisfacción por Área**  
   Un gráfico de caja que muestra cómo varía el índice de satisfacción en diferentes áreas de la empresa.
   ![Distribución del Índice de Satisfacción](Velocidarespuesta.png)

2. **Duración Promedio con Asistente por Área**  
   Un gráfico de barras que presenta la duración promedio de las interacciones por cada área.
   ![Duración Promedio con Asistente](grafico_2.png)

3. **Relación entre Velocidad de Respuesta e Índice de Satisfacción**  
   Un gráfico de dispersión que muestra la relación entre la rapidez en la respuesta y la satisfacción del cliente.
   ![Relación Velocidad-Satisfacción](grafico_3.png)

---

## 🔎 **Insights Clave**
- **Áreas con mayor satisfacción:** El área de Ventas obtuvo un índice de satisfacción superior en promedio.
- **Relación entre velocidad y satisfacción:** Existe una correlación positiva entre la rapidez en la respuesta y un mayor índice de satisfacción.
- **Duración de interacción:** Las áreas como Cancelaciones mostraron tiempos de interacción significativamente más altos.

---

## 📥 **Cómo Ejecutar el Proyecto**
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/nombre-del-repositorio.git
pip install pandas matplotlib seaborn
python analisis_datos.py
🎨 Logo del Proyecto
<p align="center"> <img src="logo.png" alt="Logo del Proyecto" width="200"> </p>
📚 Licencia
Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo LICENSE.

















