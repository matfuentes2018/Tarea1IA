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

def leer_archivo(nombre_archivo):
    with open(nombre_archivo) as archivo:
        contenido = archivo.readlines()
    
    init = contenido[0].split()[1]
    goal = contenido[1].split()[1]

    nodos_heuristicas = {}
    for i in range(2, len(contenido)-1):
        nodo, heuristica = contenido[i].split()
        nodos_heuristicas[nodo] = int(heuristica)

    aristas = []
    for i in range(len(contenido)-1, len(contenido)*2-2):
        datos_arista = contenido[i].split()
        arista = (datos_arista[0], datos_arista[1], int(datos_arista[2]))
        aristas.append(arista)

    arbol = Arbol(init, goal)
    for arista in aristas:
        nodo1, nodo2, costo = arista
        nodo1 = Nodo(nodo1, nodos_heuristicas[nodo1])
        nodo2 = Nodo(nodo2, nodos_heuristicas[nodo2])
        arbol.agregar_arista(nodo1, nodo2, costo)

    return arbol

def busqueda_greedy(arbol, f_meta):
    pila_nodos = [(arbol.nodo_init, f_meta(arbol.nodo_init))]
    
    while pila_nodos:
        nodo_actual, _ = pila_nodos.pop()
        nodo_actual.visitado = True
        
        if nodo_actual == arbol.nodo_goal:
            return True
        
        sucesores = nodo_actual.get_sucesores()
        sucesores.sort(key=lambda s: f_meta(s[0]))
        
        for sucesor, costo in sucesores:
            if not sucesor.visitado:
                pila_nodos.append((sucesor, f_meta(sucesor)))
    
    return False

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


if __name__ == '__main__':
    arbol = leer_archivo('grafo.txt')
    heuristica = lambda n: int(n.valor_h)
    
    print('Búsqueda DFS aleatoria')
    dfs_aleatoria = arbol.busqueda_dfs_aleatoria()
    print('Camino:', dfs_aleatoria)
    print('Costo:', arbol.calcular_costo_camino(dfs_aleatoria))
    
    print('\nBúsqueda por costo uniforme')
    costo_uniforme = arbol.busqueda_costo_uniforme()
    print('Camino:', costo_uniforme)
    print('Costo:', arbol.calcular_costo_camino(costo_uniforme))
    
    print('\nBúsqueda Greedy')
    greedy = busqueda_greedy(arbol, heuristica)
    print('Encontrado:', greedy)