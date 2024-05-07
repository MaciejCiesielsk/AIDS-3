import random

class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = []
        self.visited = False

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

class List:
    vertices = {}

    

    def generate_graph(self, saturation, nodes):
        if saturation > 1 or saturation < 0:
            print("Saturation must be a value between [0, 1].")
            return None

        graph = [[] for _ in range(nodes)]

        for i in range(1, nodes + 1):  
            for j in range(1, nodes + 1):  
                if i != j and random.random() < saturation:
                    graph[i - 1].append(j) 

        return graph
    
    
        