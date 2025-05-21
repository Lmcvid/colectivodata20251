import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#Gráfica de barras
colores=["#6fe5a4","#6fe5a4","#00a6a2","#0f8592","#286678","red"]

dataFrameAsistencia=pd.read_csv("./data/asistencia_estudiantes_completo.csv")

plt.figure(figsize=(8,5))
sns.countplot(x='estado',data=dataFrameAsistencia, palette=colores)
plt.title("Cantidad de registros por estado")
plt.xlabel("Estado")
plt.ylabel("Cantidad")
plt.tight_layout()
plt.show()

#Gráfica de torta
conteoTransporte=dataFrameAsistencia['medio_transporte'].value_counts()
plt.figure(figsize=(5,5))
plt.pie(
    conteoTransporte,
    labels=conteoTransporte.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette("Blues")
)
plt.title("Distribución por medio de transporte")
plt.tight_layout()
plt.show()

#Barras 
plt.figure(figsize=(10,6))
conteoEstadoMedioTransporte=dataFrameAsistencia.groupby(['estado','medio_transporte']).size().unstack(fill_value=0)
conteoEstadoMedioTransporte.plot(
    kind='bar',
    figsize=(10,6),
    color=colores
)
plt.title("Registros por estado y medio de transporte")
plt.xlabel("Estados de asistencia")
plt.ylabel("Medio de transporte")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

#Gráfica de línea
promedioTransporte=dataFrameAsistencia.groupby('medio_transporte')['estrato'].mean().sort_values()
plt.figure(figsize=(10,5))
plt.plot(promedioTransporte.index,promedioTransporte.values, marker='o', linestyle='-', color="#6fe5a4")
plt.title("Promedio de estrato por medio de transporte")    
plt.xlabel("Medio de transporte")
plt.ylabel("Estrato promedio")
plt.grid(True)
plt.tight_layout()
plt.show()
