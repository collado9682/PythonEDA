#IMPORTAMOS LAS LIBRERIAS
import pandas as pd
import matplotlib.pyplot as plt
file_path="./Data/Pen Sales Data.xlsx" #archivo excel

#ALMACENAMOS EL ARCHIVO EN UN DATAFRAME
df_pen_sales= pd.read_excel(file_path,sheet_name="Pen Sales")

#df_pen_sales.head()
#print(df_pen_sales)

#INCISO 1
#Rendimiento de las ventas a lo largo del tiempo
#Tarea: Analizar cómo varían las ventas de los diferentes tipos de bolígrafos a lo largo del tiempo.
#Pasos:
#Convierta la fecha de compra a un formato de fecha y hora.
#Cuenta el número de ventas por mes.
#Traza un gráfico de líneas de series temporales para visualizar las tendencias de ventas.
#Visualización: 📈 Gráfico de líneas (ventas a lo largo del tiempo – por mes)


#Convierta la fecha de compra a un formato de fecha y hora.
df_pen_sales["Purchase Date"] = pd.to_datetime(df_pen_sales["Purchase Date"])

#Cuenta el número de ventas por mes.
df_pen_sales["Month"] = df_pen_sales["Purchase Date"].dt.to_period("M")
Ventas_mensuales= df_pen_sales.groupby("Month").size()

#Traza un gráfico de líneas de series temporales para visualizar las tendencias de ventas.
plt.figure(figsize=(10, 5))
Ventas_mensuales.plot(kind="line", marker="o", linestyle="-", color="b")
plt.title("Tendencia de Ventas Mensuales")
plt.xlabel("Mes")
plt.ylabel("Número de Ventas")
plt.grid(True)
plt.xticks(rotation=0)
plt.show()

#INCISO 2
#Análisis de costos de envío
#Tarea: Evalúe cómo varían los costos de envío entre pedidos.
#Pasos:
#Calcular la distribución del Costo de Envío.
#Agrupe por artículo y calcule el costo promedio de envío.
#Cree un gráfico de barras que compare los costos de envío por tipo de bolígrafo.
#Visualización: 📊 Gráfico de barras (costo promedio de envío por artículo)

#Calcular la distribución del Costo de Envío.
df_distribución_costo_envío= df_pen_sales["Shipping Cost"].describe()

#Agrupe por artículo y calcule el costo promedio de envío.
df_avg_pen_costs= df_pen_sales.groupby("Item")["Shipping Cost"].mean().sort_values()


print(df_distribución_costo_envío)
print(df_avg_pen_costs)

#Cree un gráfico de barras que compare los costos de envío por tipo de bolígrafo.
plt.figure(figsize=(10, 5))
df_avg_pen_costs.plot(kind="barh", color="purple")
plt.title("Costo de envio promedio por producto")
plt.xlabel("Costo medio de envio")
plt.ylabel("Tipo de Producto")
plt.show()

