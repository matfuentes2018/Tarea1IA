import heapq
heur = {}
sizLines = 0
#EL CAMINO OPTIMO ES DE COSTE 18
def get_heuristic(node, heur):
    return heur.get(node, float('inf'))

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

def ucs(graph, start, goal):
    visited = set()
    queue = [(0, [start])]
    expanded = 0
    yes = False
    while queue:
        (cost, way) = heapq.heappop(queue)
        node = way[-1]
        if node not in visited:
            expanded += 1
            visited.add(node)
            if node == goal:
                if(cost == 18):
                    yes = True
                return way, cost, expanded, True
            del graph[node]['heuristic']
            for Ady, weight in graph[node].items():
                if Ady not in visited:
                    Cost2 = cost + weight
                    way2 = list(way)
                    way2.append(Ady)
                    heapq.heappush(queue, (Cost2, way2))
    return None, None, None, yes
    
def dfs(grafo, init, goal):
    lista = [(init, [init], 0)]
    yes = False
    visited = set()
    while lista:
        node, way, cost = lista.pop()
        if goal == node:
            siz = len(way)
            if(cost == 18):
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

def gbfs(grafo, init, goal):
    lista = [(0, init, [init])]
    visited = set()
    yes = False
    while lista:
        h, node, way = heapq.heappop(lista)
        if node == goal:
            size = len(way)
            cost = sum(grafo[way[i]][way[i+1]] for i in range(size-1))
            if(cost == 18):
                yes = True
            return way, cost, size, yes
        if node not in visited:
            visited.add(node)
            for ady in grafo[node]:
                if ady not in visited:
                    h = get_heuristic(ady, heur)
                    way2 = way.copy()
                    way2.append(ady)
                    heapq.heappush(lista, (h, ady, way2))
    non = None
    return non, non, non, yes

def a_star_search(graph, init, goal):
    queue = []
    visited = set()
    way = []
    cost = 0
    expanded = 0
    yes = False
    heapq.heappush(queue, (0, init, way, cost))
    
    while queue:
        _, node, way, cost = heapq.heappop(queue)
        visited.add(node)
        
        if goal == node:
            if(cost == 18):
                yes = True
            return way + [node], cost, expanded, yes
    
        for Ady, weight in graph[node].items():
            if Ady not in visited:
                h = get_heuristic(Ady,heur)
                heapq.heappush(queue, (cost + weight + h, Ady, way + [node], cost + weight))
                expanded += 1
    return None, None, None, yes

non = None
grafo, init, goal = read_file('grafo.txt')
#Aca es donde debe cambiar la busqueda por dfs, ucs, gbfs, a_star_search
way, cost, expanded, opt = ucs(grafo, init, goal)
if way != non:
    #La solucion optima es de coste 18, si obtienen una distinta arrojara No, en cambio si obtienen 18 arrojara Si
    if opt == True:
        print('Solucion optima encontrada: Si')
    else:
        print('Solucion optima encontrada: No')
    print('Camino:', way)
    print('Costo del camino:', cost)
    print('Nodos expandidos:', expanded)
   
else:
    print('error')