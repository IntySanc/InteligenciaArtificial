import heapq

def a_estrella(grafico, inicio, objetivo, heuristica):
    cola_prioridad = [(0, inicio, [])]
    visitados = set()

    while cola_prioridad:
        costo_actual, nodo_actual, camino_actual = heapq.heappop(cola_prioridad)

        if nodo_actual == objetivo:
            return camino_actual + [nodo_actual]
        
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)

            for vecino, costo in grafico[nodo_actual].items():
                nuevo_costo =costo_actual + costo
                heuristico = heuristica(vecino, objetivo)
                heapq.headppush(cola_prioridad, (nuevo_costo + heuristico, vecino, camino_actual + [nodo_actual]))

            return None