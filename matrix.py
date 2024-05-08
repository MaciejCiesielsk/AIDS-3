import numpy as np
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

class Matrix:
    
    def generate_graph(self, saturation, nodes):
        if saturation > 1 or saturation < 0:
            print("Saturation must be a value between [0, 1].")
            return None
        
        adjacency_matrix = np.zeros((nodes, nodes))

        for i in range(nodes):
            for j in range(i + 1, nodes):
                if random.random() < saturation:
                    adjacency_matrix[i][j] = 1

        return adjacency_matrix