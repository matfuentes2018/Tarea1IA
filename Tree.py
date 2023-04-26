import random
from Nodos import Node

class Tree:
    def __init__(self, node, parent_node, value):
        self.parent_node = parent_node
        self.node = node
        self.childNodes = []
        node.augment()
        self.heuristic = value
    # lo mismo que en nodos con append agregaremos nodos hijos al arbol
    def addChildNode(self, node):
        self.childNodes.append(node)

    def __lt__(self, other):
        if self.heuristic == other.heuristic:
            return random.choice([True, False])
        else:
            return self.heuristic < other.heuristic