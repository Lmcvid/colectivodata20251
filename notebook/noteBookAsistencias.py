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

#print(asistenciaDataFrame['estrato'].value_counts().head(2)) 

#FILTROS O CONSULTAS DETALLADAS

#1. Necesito encontrar los estudiantes que sí asistieron.
estudiantesQueAsistieron=asistenciaDataFrame.query('estado=="asistio"')
print(estudiantesQueAsistieron)

#2. Necesito encontrar los estudiantes que faltaron.
estudiantesQueNoAsistieron=asistenciaDataFrame.query('estado=="inasistencia"')
print(estudiantesQueNoAsistieron)

#3. Necesito encontrar los estudiantes que llegaron tarde.(Justificaron)
estudiantesQueJustificaron=asistenciaDataFrame.query('estado=="justificado"')
print(estudiantesQueJustificaron)


#4. Necesito encontrar los estudiantes de estrato 1.
estudiantesEstratoUno=asistenciaDataFrame.query('estrato==1')
print(estudiantesEstratoUno)

#5. Necesito encontrar los estudiantes de estratos altos.
estudiantesEstratoAlto=asistenciaDataFrame.query('estrato==5')
print(estudiantesEstratoAlto)

#6. Necesito encontrar estudiantes que llegan en metro.
estudiantesQueLleganEnMetro=asistenciaDataFrame.query('medio_transporte=="metro"')
print(estudiantesQueLleganEnMetro)

#7. Necesito encontrar estudiantes que llegaron en bicicleta.

#8. Necesito encontrar todos los estudiantes menos los que llegaron a pie.
estudiantesNoAPie=asistenciaDataFrame.query('medio_transporte!="a pie"')
print(estudiantesNoAPie)
#print(asistenciaDataFrame["medio_transporte"].unique())

#9. Necesito todos los registros de asistencia de junio.

#10. Necesito todos los estudiantes que usan transportes ecológicos.

#11. Necesito los estudianes que usan bus y son de estrato alto.

#12. Necesito los estudianes que usan bus y son de estrato bajo.

#13.Necesito estudiantes que caminan para llegar a clases.(se usa el filtro de a pie)

#CONTEOS POR AGRUPACIONES 

#1. Necesito el conteo de registros por estado de asistencia(cuantos asistieron, cuantos faltaron, cuántos justificaron)
conteo=asistenciaDataFrame.groupby('estado').size()
print(conteo)

#2. Necesito obtener el número de registros por estrato.(revisar si ya está)

#3. Necesito la cantidad de estudiantes por medio de transporte.(Cuántos usan bus, cupantos metro...)
conteoMediotransporte=asistenciaDataFrame.groupby('medio_transporte').size()
print(conteoMediotransporte)

#4. Necesito el promedio de estrato por estado de asistencia. (en priomedio los que asisten qué estrato son, los que faltan... los que justifican...)
promedioAsistenciaPorEstrato=asistenciaDataFrame.groupby('estado')['estrato'].mean()
print(promedioAsistenciaPorEstrato)

#5. Máximo estrato por estado.

#6. Mínimo estrato por estado.

#7. Necesito un conteo de asistencias por grupo y estado. (Grupo x cantidad de estudiantes, X son estado tal).





