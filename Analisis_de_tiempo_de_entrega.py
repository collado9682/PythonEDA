import pandas as pd
import matplotlib.pyplot as plt

file_path="./Data/Pen Sales Data.xlsx" #archivo excel

#ALMACENAMOS EL ARCHIVO EN UN DATAFRAME
df_pen_sales= pd.read_excel(file_path,sheet_name="Pen Sales")

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
Tiempo_medio_entrega = df_pen_sales.groupby("Item") ["Tiempo de entrega"].mean().sort_values()

print(Tiempo_medio_entrega)
