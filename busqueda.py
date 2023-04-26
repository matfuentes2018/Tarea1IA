import random
from queue import PriorityQueue

class Nodo:
    def __init__(self, nombre, costo=0, sucesores=None):
        self.nombre = nombre
        self.costo = costo
        self.visitado = False
        self.sucesores = sucesores or []

    def add_sucesor(self, sucesor, costo):
        self.sucesores.append((sucesor, costo))

    def get_sucesores(self):
        return self.sucesores

    def __lt__(self, other):
        return self.costo < other.costo
    
    def __eq__(self, other):
        return self.nombre == other.nombre

def busqueda_costo_uniforme(nodo_inicial, nodo_objetivo):
    frontera = PriorityQueue()
    frontera.put(nodo_inicial)
    
    while not frontera.empty():
        nodo_actual = frontera.get()
        
        if nodo_actual == nodo_objetivo:
            return nodo_actual
        
        nodo_actual.visitado = True
        
        for sucesor, costo in nodo_actual.get_sucesores():
            if not sucesor.visitado:
                sucesor.costo = nodo_actual.costo + costo
                frontera.put(sucesor)
    
    return None
    
class Arbol:
    def __init__(self, raiz):
        self.raiz = raiz
        self.nodos_expandidos = 0
    
    def dfs_aleatoria(self, nodo_actual, nodo_objetivo, camino, costo):
        nodo_actual.visitado = True
        camino.append(nodo_actual)
        
        if nodo_actual.nombre == nodo_objetivo:
            return camino, costo, self.nodos_expandidos, True
        
        sucesores = nodo_actual.get_sucesores()
        self.nodos_expandidos += 1
        
        random.shuffle(sucesores)
        for sucesor in sucesores:
            if not sucesor.visitado:
                costo += sucesor.costo
                resultado = self.dfs_aleatoria(sucesor, nodo_objetivo, camino, costo)
                if resultado[3]:
                    return resultado
                else:
                    costo -= sucesor.costo
        
        camino.pop()
        return camino, costo, self.nodos_expandidos, False

if __name__ == '__main__':
    with open('grafo.txt', 'r') as file:
        grafo = file.readlines()
        
    # Nodo inicial
    nodo_inicial = grafo[0].split(' ')[1].strip()
    
    # Nodo objetivo
    nodo_objetivo = grafo[1].split(' ')[1].strip()
    
    # Heurísticas
    heur = {}
    for linea in grafo[2:]:
        if ',' not in linea:
            nodo, heuristica = linea.strip().split(' ')
            heur[nodo] = int(heuristica)
            
    # Aristas
    nodos = {}
    for linea in grafo[2:]:
        if ',' in linea:
            nodo1, nodo2, costo = linea.strip().split(' ')
            costo = int(costo)
            
            if nodo1 not in nodos:
                nodos[nodo1] = Nodo(nodo1)
            if nodo2 not in nodos:
                nodos[nodo2] = Nodo(nodo2)
            
            nodos[nodo1].add_sucesor(nodos[nodo2])
            nodos[nodo2].add_sucesor(nodos[nodo1])
            
            nodos[nodo1].costo = costo
            nodos[nodo2].costo = costo
            
    raiz = nodos[nodo_inicial]
    arbol = Arbol(raiz)
    camino, costo, nodos_expandidos, solucion_optima = arbol.dfs_aleatoria(raiz, nodo_objetivo, [], 0)
    
    if solucion_optima:
        print("Solución encontrada:")
        for nodo in camino:
            print(nodo.nombre, end=" ")
        print(f"\nCosto: {costo}")
    else:
        print("No se encontró solución.")
    print(f"Nodos expandidos: {nodos_expandidos}")