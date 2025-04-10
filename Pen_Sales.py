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
plt.tight_layout()
plt.show()

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

#INCISO 4
#Análisis de Tiempo de Entrega
#Tarea: Calcular el tiempo medio de entrega para cada tipo de bolígrafo.
#Pasos:
#Calcular tiempo de entrega = Fecha de entrega - Fecha de compra.
#Agrupe por artículo y encuentre el tiempo medio de entrega.
#Traza un gráfico de barras para comparar los tiempos de entrega.
#Visualización: ⏳ Gráfico de barras (tiempo medio de entrega por tipo de bolígrafo)


#Calcular tiempo de entrega = Fecha de entrega - Fecha de compra.
Tiempo_de_entrega= (df_pen_sales["Delivery Date"] - df_pen_sales["Purchase Date"])
print(Tiempo_de_entrega)

#Columna nueva
df_pen_sales["Tiempo de entrega"] = Tiempo_de_entrega

#print (df_pen_sales.dtypes)

#Agrupe por artículo y encuentre el tiempo medio de entrega.
Tiempo_medio_entrega= df_pen_sales.groupby("Item") ["Tiempo de entrega"].mean().sort_values()

print(Tiempo_medio_entrega)

#Traza un gráfico de barras para comparar los tiempos de entrega.
plt.figure(figsize=(10, 5))
Tiempo_medio_entrega.plot(kind="bar", color="orange")
plt.title("Tiempo medio entrega de productos")
plt.xlabel("Tipo de Producto")
plt.ylabel("Tiempo medio de entrega (días)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
