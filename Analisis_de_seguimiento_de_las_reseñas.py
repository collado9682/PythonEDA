import pandas as pd
import matplotlib.pyplot as plt

file_path="./Data/Pen Sales Data.xlsx" #archivo excel

#ALMACENAMOS EL ARCHIVO EN UN DATAFRAME
df_pen_sales= pd.read_excel(file_path,sheet_name="Pen Sales")


#5. Análisis de sentimiento de las reseñas
#Tarea: Extraer el sentimiento de las opiniones de los clientes.
#Pasos:
# Dividir la columna Review para separar el nombre del revisor y el comentario.
# Realizar un análisis básico de sentimientos (contar las apariciones de palabras positivas como amor, genial, bueno frente a palabras negativas como malo, disgusto).
# Genere una nube de palabras o un gráfico circular de sentimientos.
#Visualización: 🥧 Gráfico de pastel o circular (críticas positivas vs. negativas)


# Realizar un análisis básico de sentimientos (contar las apariciones de palabras positivas como amor, genial, bueno frente a palabras negativas como malo, disgusto).
reviews= df_pen_sales["Review"]

print(reviews)

reseñas_positivas= ["love","great","good","excellent","best","amazing"]
reseñas_negativas=["bad","poor","dislike","terrible","worst"]

contar_reseñas_positivas= reviews.str.contains("|".join(reseñas_positivas), case=False, na=False).sum()

print("cantidad de reseñas positivas:" + str(contar_reseñas_positivas))