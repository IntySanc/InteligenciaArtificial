
from sklearn.linear_model import LinearRegression

#Datos de entrenamiento: Kilobytes (Kb)
x_train = [[1024],[2048],[3072],[4096],[5120],[6144],[7168],[8192]]

#Etiquetas: Megabytes (MB)
y_train = [1, 2, 3, 4, 5, 6, 7, 8]

#Crear y entrenar el modelo de regresion lineal
model = LinearRegression()
model.fit(x_train, y_train)

#pedir el valo de KB0
kb = int(input("Ingrese el valor en Kb: "))

#Realizar Predicciones
kb_to_convert = [[kb]]
predicted_mb = model.predict(kb_to_convert)

#imprimir resultado

print(f"{kb} kb equivalen aproximadente a {predicted_mb[0]} MB")