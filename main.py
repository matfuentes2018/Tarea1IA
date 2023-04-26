import heapq
heur = {}
sizLines = 0
import math

def read_file(graph_name):
    grafo = {} 
    sizLines = 0
    with open(graph_name, 'r') as graph:
        for line in graph:
            sizLines = sizLines + 1
            if line.startswith('Init:'):
                init = line.split()[1]
            elif line.startswith('Goal:'):
                goal = line.split()[1]
            elif line.startswith('Change:'):
                break
            else:
                node, heuristic = line.split()
                heur[node] = int(heuristic)
                
                grafo[node] = {}
                grafo[node]['heuristic'] = int(heuristic)
        for line in graph:
            nodeA, nodeB, cost = line.split(',')
            if nodeA not in grafo:
                grafo[nodeA] = {}
            if nodeB not in grafo:
                grafo[nodeB] = {}
            grafo[nodeA][nodeB] = int(cost)
            grafo[nodeB][nodeA] = int(cost)
    return grafo, init, goal

def ucs(grafo, init, goal):
    lista = [(0, init, [init])]
    visited = set()
    yes = False
    while lista:
        cost, node, way = heapq.heappop(lista)
        if goal == node:
            siz = len(way)
            yes = True
            return way, cost, siz, yes
        if node not in visited:
            visited.add(node)
            for Ady in grafo[node]:
                if Ady not in visited:
                    Cost2 = cost + grafo[node][Ady]
                    way2 = way.copy()
                    way2.append(Ady)
                    heapq.heappush(lista, (Cost2, Ady, way))
    non = None
    return non, non, non, yes
    
def dfs(grafo, init, goal):
    lista = [(init, [init], 0)]
    yes = False
    visited = set()
    while lista:
        node, way, cost = lista.pop()
        if goal == node:
            siz = len(way)
            yes = True
            return way, cost, siz, yes
        if node not in visited:
            visited.add(node)
            for Ady in grafo[node]:
                if Ady not in visited:
                    Cost2 = cost + grafo[node][Ady]
                    way2 = way.copy()
                    way2.append(Ady)
                    
                    lista.append((Ady, way2, Cost2))
    non = None
    return non, non, non, yes

def greedy(grafo, init, goal):
    # Inicializamos la lista de nodos visitados y la cola de prioridad
    visited = set()
    queue = [(heur[init], init)]
    yes = False
    
    while queue:
        # Extraemos el nodo con la heurística más baja
        h, node = heapq.heappop(queue)
        
        if node == goal:
            # Si el nodo es el objetivo, devolvemos la solución
            size = len(visited)
            cost = 0
            for i in range(size-1):
                cost += grafo[visited[i]][visited[i+1]]
            cost += grafo[visited[size-1]][goal]
            yes = True
            return visited, cost, size, yes
        
        if node not in visited:
            # Si el nodo no ha sido visitado, lo marcamos como visitado
            visited.add(node)
            
            for ady in grafo[node]:
                # Agregamos los nodos adyacentes a la cola de prioridad
                if ady not in visited:
                    print(ady)
                    heapq.heappush(queue, (heur[ady], ady))
    
    non = None
    return non, non, non, yes

non = None
grafo, init, goal = read_file('grafo.txt')
#utilizar el siguiente en caso de usar busqueda greedy
way, cost, expanded, opt = greedy(grafo, init, goal)
if way != non:
    if opt == True:
        print('Solucion optima encontrada: Si')
    else:
        print('Solucion optima encontrada: No')
    print('Camino:', way)
    print('Costo del camino:', cost)
    print('Nodos expandidos:', expanded)
   
else:
    print('error')