import random

class Node:
    edges = []
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.augmented = False

    
    # con append agregaremos las aristas
    def add_edge(self, edge):
        self.edges.append(edge)
    
    def remove_edge(self, edge):
        self.edges.remove(edge)

    def traverse(self):
        print(self.name)
        print(" ")
        print(self.heuristic)
        for edge in self.edges:
            print(" ->")
            print(edge.name)
            print(edge.heuristic)
            edge.node.traverse()
    #confirmaremos si se expandio el nodo o no
    def augment(self):
        self.augmented = True


