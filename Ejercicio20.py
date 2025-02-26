import heapq

def a_estrella(grafo, inicio, fin, heuristica):
    abierta = []
    cerrada = set()
    heapq.heappush(abierta, (0 + heuristica(inicio), 0, inicio, [inicio]))
    
    while abierta:
        _, costo, nodo, camino = heapq.heappop(abierta)
        if nodo == fin:
            return camino
        if nodo in cerrada:
            continue
        cerrada.add(nodo)
        for vecino, peso in grafo.get(nodo, []):
            if vecino not in cerrada:
                heapq.heappush(abierta, (costo + peso + heuristica(vecino), costo + peso, vecino, camino + [vecino]))
    return None

# Ejemplo de uso
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

def heuristica_simple(nodo):
    heuristicas = {'A': 3, 'B': 2, 'C': 1, 'D': 0}
    return heuristicas[nodo]

camino = a_estrella(grafo, 'A', 'D', heuristica_simple)
print(f"Camino encontrado: {camino}")