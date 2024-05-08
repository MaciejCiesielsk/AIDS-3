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


    def generate_graph(self, saturation, nodes):
        if saturation > 1 or saturation < 0:
            print("Saturation must be a value between [0, 1].")
            return None

        graph = [[] for _ in range(nodes)]

        for i in range(1, nodes + 1):  
            for j in range(i + 1, nodes + 1):  
                if random.random() < saturation:
                    graph[i - 1].append(j) 

        return graph
    
    def user_provided_graph(self):
        nodes = int(input("Enter number of vertices: "))
        graph = [[] for _ in range(nodes)]

        for i in range(nodes):
            successors = input(f"Enter successors of vertex {i+1}, separated by spaces: ").split()
            for successor in successors:
                j = int(successor) - 1
    
    
        