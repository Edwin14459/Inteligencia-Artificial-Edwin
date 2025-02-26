# Grafo cono nodos y costos 
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Heristica de distancia simple
def heuristica(nodo):
    distancias = {'A': 3, 'B': 2, 'C': 1, 'D': 0}
    return distancias.get(nodo, 0)

# Implementación del algoritmo A*
def a_estrella(grafo, inicio, objetivo, heuristica):
    import heapq
    cola = [(0, inicio)]
    costos = {inicio: 0}
    padres = {inicio: None}

    while cola:
        (costo, nodo_actual) = heapq.heappop(cola)

        if nodo_actual == objetivo:
            camino = []
            while nodo_actual:
                camino.append(nodo_actual)
                nodo_actual = padres[nodo_actual]
            return camino[::-1]

        for vecino, peso in grafo[nodo_actual]:
            nuevo_costo = costos[nodo_actual] + peso
            if vecino not in costos or nuevo_costo < costos[vecino]:
                costos[vecino] = nuevo_costo
                prioridad = nuevo_costo + heuristica(vecino)
                heapq.heappush(cola, (prioridad, vecino))
                padres[vecino] = nodo_actual

    return None

#Ejemplo de uso
camino = a_estrella(grafo, 'A', 'D', heuristica)
print(f"Camino encontrado: {camino}")