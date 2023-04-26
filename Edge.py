import random
from Nodos import Node

class Edge:
    def __init__(self, name, heuristic, node):
        self.heuristic = heuristic
        self.name = name
        self.node = node