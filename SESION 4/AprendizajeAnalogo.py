# Universidad del Valle - Inteligencia Artificial
# Tema: Aprendizaje Analogo

from sklearn.neighbors import NearestNeighbors
import numpy as np

#Datos conocidos (Entrenamiento)
X_train = np.array ([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6],[6,7],[7,8]])

#Datos desconocidos (Nuevas Observaciones)
X_unknown = np.array ([[1.5, 2.5],[3.5, 4.5],[5.5, 7.5]])

#Crear y ajustar el modelo de vecinos mas cercanos (Nearest Neighbors)
model = NearestNeighbors(n_neighbors=2)
model.fit(X_train)

#Encontrar los vecinos mas cercanos para las nuevas observaciones
distances, indices = model.kneighbors(X_unknown)

#Imprimir los vecinos mas cercanos encontrados
for i in range(len(X_unknown)):
    print("Para la observacion", X_unknown[i], "los  vecinos mas cercanos son:", X_train[indices[i]])