import pandas as pd
import matplotlib.pyplot as plt

file_path="./Data/Pen Sales Data.xlsx" #archivo excel

#ALMACENAMOS EL ARCHIVO EN UN DATAFRAME
df_pen_sales= pd.read_excel(file_path,sheet_name="Pen Sales")

#INCISO 3
#Ranking de popularidad de bolígrafos
#Tarea: Identificar el tipo de bolígrafo que se compra con más frecuencia.
#Pasos:
#Cuente el número de compras por artículo.
#Ordenar en orden descendente.
#Traza un gráfico de barras horizontales para mayor claridad.
#Visualización: 📊 Gráfico de barras horizontales (bolígrafos más vendidos)

#Cuente el número de compras por artículo.
Conteo_de_productos= df_pen_sales ["Item"].value_counts()

print(Conteo_de_productos)

#Traza un gráfico de barras horizontales para mayor claridad.
plt.figure(figsize=(10, 5))
Conteo_de_productos.plot(kind="barh", color="green")
plt.title("Ranking de popularidad de productos")
plt.xlabel("Cantidad de ventas")
plt.ylabel("Tipo de Producto")
plt.tight_layout()
plt.show()
