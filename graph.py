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

    def find_edge(self, graph_type, graph_data):
        if graph_type == "Matrix":
            i = int(input("Enter starting vertex: ")) - 1
            j = int(input("Enter ending vertex: ")) - 1
            if 0 <= i < len(graph_data) and 0 <= j < len(graph_data):
                if graph_data[i][j] == 1:
                    print(f"Edge from {i + 1} to {j + 1} exists")
                else:
                    print(f"Edge from {i + 1} to {j + 1} does not exist")
            else:
                print("Invalid vertices")
        elif graph_type == "List":
            i = int(input("Enter starting vertex: ")) - 1
            j = int(input("Enter ending vertex: ")) - 1
            if 0 <= i < len(graph_data) and 0 <= j < len(graph_data):
                if j in graph_data[i]:
                    print(f"Edge from {i + 1} to {j + 1} exists")
                else:
                    print(f"Edge from {i + 1} to {j + 1} does not exist")
            else:
                print("Invalid vertices")
        else:
            print("Invalid graph type")


    def bfs(self, graph_type, graph_data, start):
        if graph_type == "Matrix":
            visited = [False] * len(graph_data)
            queue = [start]
            visited[start] = True

            while queue:
                vertex = queue.pop(0)
                print(vertex + 1, end=" ")
                for i in range(len(graph_data)):
                    if graph_data[vertex][i] == 1 and not visited[i]:
                        queue.append(i)
                        visited[i] = True
        elif graph_type == "List":
            start -= 1 
            if start < 0 or start >= len(graph_data):
                print("Invalid starting vertex")
                return

            visited = [False] * len(graph_data)
            queue = [start]
            visited[start] = True
            while queue:
                vertex = queue.pop(0)
                print(vertex + 1, end=" ")  

                for neighbor in graph_data[vertex]:
                    if not visited[neighbor - 1]:  
                        queue.append(neighbor - 1)
                        visited[neighbor - 1] = True
                
        else:
            print("Invalid graph type")


    def dfs_util(self, graph_data, vertex, visited):
        visited[vertex] = True
        print(vertex + 1, end=" ")

        for i in range(len(graph_data)):
            if graph_data[vertex][i] == 1 and not visited[i]:
                self.dfs_util(graph_data, i, visited)
    
    def dfs(self, graph_type, graph_data):
        if graph_type == "Matrix":
            start = int(input("Enter starting vertex: "))
            visited = [False] * len(graph_data)
            self.dfs_util(graph_data, start, visited)
            print()
        elif graph_type == "List":
            start = int(input("Enter starting vertex: ")) 
            if 0 <= start < len(graph_data):
                visited = [False] * len(graph_data)
                self.dfs_util_list(graph_data, start, visited)
                print()
            else:
                print("Invalid starting vertex")
        else:
            print("Invalid graph type")


        

    def dfs_util_list(self, graph_data, vertex, visited):
        visited[vertex] = True
        print(vertex + 1, end=" ")  

        for neighbor in graph_data[vertex]:
            if not visited[neighbor - 1]: 
                self.dfs_util_list(graph_data, neighbor - 1, visited)
