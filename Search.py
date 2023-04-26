import Nodos, Edge, Tree, queue, random

def dfs(init,goal):
    none = None
    tree = Tree(init, none, 0)
    endTree = tree # como el arbol recien esta inicializado el final es el mismo arbol 
    if (goal == init):
        return endTree
    while (goal != endTree.node):
        siz = len(endTree.node.edges) - 1
        num = random.randint(0,siz)
        nodeAux = endTree.node.edges[num].node
        heur = endTree.heuristic + endTree.node.edges[num].heuristic
        x = Tree(nodeAux, endTree, heur)
        endTree.addChildNodes(x)
        endTree = x
    return tree

def UniformCost(init, goal):
    none = None
    q = queue.PriorityQueue()
    tree2 = Tree(init, none, 0)
    endTree2 = tree2
    q.put(endTree2,endTree2.heuristic)
    asx = 1
    while(asx == 1):
        for x in endTree2.node.edges:
            heur = int(endTree2.heuristic) + int(x.heuristic)
            a = Tree(x.node,endTree2,heur)
            endTree2.addChildNode(a)
            q.put(a, a.heuristic)
            if(goal == a.node):
                asx = asx + 1
                endTree2 = a
                break
        if (goal == endTree2):
            break
        q.get()
        q = q.queue.PriorityQueue(reversed)
        endTree2 = q.get()
    return endTree2

def greedySearch(init, goal):
    none = None
    tree3 = Tree(init, none, init.heuristic)
    endTree3 = tree3
    if(goal == init):
        return tree3
    while(goal != endTree3.node):
        