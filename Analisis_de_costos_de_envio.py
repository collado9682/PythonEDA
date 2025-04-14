import pandas as pd
import matplotlib.pyplot as plt

file_path="./Data/Pen Sales Data.xlsx" #archivo excel

#ALMACENAMOS EL ARCHIVO EN UN DATAFRAME
df_pen_sales= pd.read_excel(file_path,sheet_name="Pen Sales")

#INCISO 2
#Análisis de costos de envío
#Tarea: Evalúe cómo varían los costos de envío entre pedidos.
#Pasos:
#Calcular la distribución del Costo de Envío.
#Agrupe por artículo y calcule el costo promedio de envío.
#Cree un gráfico de barras que compare los costos de envío por tipo de bolígrafo.
#Visualización: 📊 Gráfico de barras (costo promedio de envío por artículo)

#Calcular la distribución del Costo de Envío.
df_distribucion_costo_envío= df_pen_sales["Shipping Cost"].describe()

#Agrupe por artículo y calcule el costo promedio de envío.
df_avg_pen_costs= df_pen_sales.groupby("Item")["Shipping Cost"].mean().sort_values()

#print(df_distribución_costo_envío)
print(df_avg_pen_costs)


#Cree un gráfico de barras que compare los costos de envío por tipo de bolígrafo.
plt.figure(figsize=(10, 5))
df_avg_pen_costs.plot(kind="barh", color="purple")
plt.title("Costo de envío promedio por producto")
plt.xlabel("Costo medio de envío")
plt.ylabel("Tipo de Producto")
plt.tight_layout()
plt.show()