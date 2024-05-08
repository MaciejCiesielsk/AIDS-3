import numpy as np
import random
import numpy as np
import random


class Graph:
    
    def generate(self, saturation, nodes, graph):
        if graph == "Matrix":
            if saturation > 1 or saturation < 0:
                print("Saturation must be a value between [0, 1].")
                return None
        
            adjacency_matrix = np.zeros((nodes, nodes))

            for i in range(nodes):
                for j in range(i + 1, nodes):
                    if random.random() < saturation:
                        adjacency_matrix[i][j] = 1

            return adjacency_matrix
        elif graph == "List":
            if saturation > 1 or saturation < 0:
                print("Saturation must be a value between [0, 1].")
                return None

            graph = [[] for _ in range(nodes)]

            for i in range(1, nodes + 1):  
                for j in range(i + 1, nodes + 1):  
                    if random.random() < saturation:
                        graph[i - 1].append(j) 

            return graph
        else:
            print("Invalid graph type")
            return None
    
    
    
    def user_provided_graph(self, graph):
        if graph == "Matrix":
            nodes = int(input("Enter number of vertices: "))
            adjacency_matrix = np.zeros((nodes, nodes))

            for i in range(nodes):
                successors = input(f"Enter successors of vertex {i+1}, separated by spaces: ").split()
                for successor in successors:
                    j = int(successor) - 1 
                    if 0 <= j < nodes:
                        adjacency_matrix[i][j] = 1
                    else:
                        print(f"Invalid successor {successor} for vertex {i+1}")

            return adjacency_matrix
        elif graph == "List":
            nodes = int(input("Enter number of vertices: "))
            graph = [[] for _ in range(nodes)]

            for i in range(nodes):
                successors = input(f"Enter successors of vertex {i+1}, separated by spaces: ").split()
                for successor in successors:
                    j = int(successor) - 1
                    if 0 <= j < nodes:
                        graph[i].append(j)
                    else:
                        print(f"Invalid successor {successor} for vertex {i+1}")

            return graph
        else:
            print("Invalid graph type")
            return None
    
    def print_graph(self, graph):
        if graph == "Matrix":
            for i in range(len(graph)):
                print(f"{i}: {graph[i]}")
        elif graph == "List":
            for i, neighbors in enumerate(graph):
                print(f"{i + 1}: {neighbors}")
        else:
            print("Invalid graph type")

        def print_matrix_with_indices(matrix):
            print(" ", end=" ")
            for i in range(len(matrix[0])):
                print(i+1, end=" ")
            print()

            for i, row in enumerate(matrix, start=1):
                print(i, end=" ")
                for value in row:
                    print(int(value), end=" ")
                print()

