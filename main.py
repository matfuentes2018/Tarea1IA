import heapq
heur = {}
sizLines = 0

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

def gbfs(grafo, init, goal):
    lista = [(0, init, [init])]
    visited = set()
    yes = False
    while lista:
        h, node, way = heapq.heappop(lista)
        if node == goal:
            size = len(way)
            cost = sum(grafo[way[i]][way[i+1]] for i in range(size-1))
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
    heapq.heappush(queue, (0, init, way, cost))
    
    while queue:
        _, node, way, cost = heapq.heappop(queue)
        visited.add(node)
        
        if goal == node:
            return way + [node], cost, expanded, True
    
        for Ady, weight in graph[node].items():
            if Ady not in visited:
                h = get_heuristic(Ady,heur)
                heapq.heappush(queue, (cost + weight + h, Ady, way + [node], cost + weight))
                expanded += 1
    return None, None, None, False

non = None
grafo, init, goal = read_file('grafo.txt')
#Aca es donde debe cambiar la busqueda por dfs, ucs, gbfs, a_star_search
way, cost, expanded, opt = dfs(grafo, init, goal)
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