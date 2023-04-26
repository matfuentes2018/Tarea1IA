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
    with open(nombre_archivo, 'r') as f:
        lineas = f.readlines()
    
    linea_init = lineas[0].strip()
    linea_goal = lineas[1].strip()
    info_nodos = lineas[2:-1]
    info_aristas = lineas[-1].strip().split(', ')
    
    init = Nodo(linea_init.split()[1])
    goal = Nodo(linea_goal.split()[1])
    
    arbol = Arbol(init, goal)
    nodos = {init.nombre: init}
    
    for info in info_nodos:
        nombre, valor_h = info.strip().split()
        nodos[nombre] = Nodo(nombre, valor_h)
    
    for info in info_aristas:
        nombre1, nombre2, costo = info.strip().split()
        nodos[nombre1].add_sucesor(nodos[nombre2], int(costo))
    
    for nodo in nodos.values():
        arbol.agregar_nodo(nodo)
    
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