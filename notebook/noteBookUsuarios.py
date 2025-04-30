import pandas as pd

usuariosDataFrame=pd.read_excel("./data/usuarios_sistema_completo.xlsx")
#print(usuariosDataFrame)

print(usuariosDataFrame.isnull().sum()) #Verifica cuántos datos están vacíos

#1. Necesito solo un listado de aprendices o estudiantes.

#2. Necesito un listado de solo instructores o profesores.

#3. Necesito un listado de especialistas en dsrrllo web o sistemas.

#4. Necesito un listado de solo usuarios con direcciones en Medellín.

#5. Necesito un listado de solo usuarios cuyas direcciones terminen en SUR.

#6. Necesito un listado de especialistas o profesores que contengan la palabra Datos.(Que aparzca "Datos" en la descripcion de la especialidad).

#7. Necesito docentes de itagui.

#8. Necesito una lista de nacidos en el 90 o antes.

#9. Necesito un listado de instructores/profesor mayores.

#10. Necesito un listado de profesores y estudiantes nacidos en el nuevo milenio.