import pandas as pd

#Leyendo los datos de asistencias
asistenciaDataFrame=pd.read_csv("./data/asistencia_estudiantes_completo.csv")
#print(asistenciaDataFrame)

#Obteniendo información básica del dataframe
#print(asistenciaDataFrame.info()) #Información de todos los datos.

#print(asistenciaDataFrame.tail(20))#muestra los últimos N registros de la tabla.

#print(asistenciaDataFrame.head(20)) #muestra los primeros N registros de la tabla.

#print(asistenciaDataFrame.describe()) #Analisis descriptivo de los datos numéricos.

#print(asistenciaDataFrame.isnull().sum())  #Verifica cuántos datos están vacíos

#print(asistenciaDataFrame['estado']) #Selecciona columnas por separado.

#print(asistenciaDataFrame['estado'].value_counts()) #Para contar los valores.

print(asistenciaDataFrame['estrato'].value_counts().head()) 

