import numpy as np
import random
import math


class Graph:
    def __init__(self):
        self.adjacency_matrix = None
        self.graph = None

    def generate(self, saturation, nodes, graph):
        if graph == "Matrix":
            if saturation > 1 or saturation < 0:
                print("Saturation must be a value between [0, 1].")
                return None

            self.adjacency_matrix = [[0] * nodes for _ in range(nodes)]

            for i in range(nodes):
                for j in range(i + 1, nodes):
                    if random.random() < saturation:
                        self.adjacency_matrix[i][j] = 1

            return self.adjacency_matrix
        elif graph == "List":
            if saturation > 1 or saturation < 0:
                print("Saturation must be a value between [0, 1].")
                return None

            self.graph = [[] for _ in range(nodes)]

            for i in range(1, nodes + 1):
                for j in range(i + 1, nodes + 1):
                    if random.random() < saturation:
                        self.graph[i - 1].append(j)

            return self.graph
        elif graph == "Table":
            if saturation > 1 or saturation < 0:
                print("Saturation must be a value between [0, 1].")
                return None

            self.connections = []

            for i in range(nodes):
                for j in range(i + 1, nodes):
                    if random.random() < saturation:
                        self.connections.append((i+1, j+1))

            return self.connections
        else:
            print("Invalid graph type")
            return None
    
    
    def user_provided_graph(self, graph):
        if graph == "Matrix":
            nodes = int(input("Enter number of vertices: "))
            self.adjacency_matrix = np.zeros((nodes, nodes))

            for i in range(nodes):
                successors = input(f" {i+1}>").split()
                for successor in successors:
                    j = int(successor) - 1 
                    if 0 <= j < nodes:
                        self.adjacency_matrix[i][j] = 1
                    else:
                        print(f"Invalid successor {successor} for vertex {i+1}")

            return self.adjacency_matrix
        elif graph == "List":
            nodes = int(input("Enter number of vertices: "))
            self.graph = [[] for _ in range(nodes)]

            for i in range(nodes):
                successors = input(f" {i+1}>").split()
                for successor in successors:
                    j = int(successor) - 1 
                    if 0 <= j < nodes:
                        self.graph[i].append(j)
                    else:
                        print(f"Invalid successor {successor} for vertex {i+1}")

            return self.graph
        else:
            print("Invalid graph type")
            return None
    
    def print_list(self, graph_data, graph_type):
        if graph_type == "List":    
            for i, neighbors in enumerate(graph_data, start=1):
                successors = ", ".join(str(neighbor + 1) for neighbor in neighbors)
                print(f"{i}: {successors}")
        else:
            print("Invalid graph type")


    def print_matrix(self):
        if self.adjacency_matrix is None:
            print("Adjacency matrix is not generated.")
            return
        print("    " + "  ".join(str(i) for i in range(1, len(self.adjacency_matrix)+1)))  
        print("--+" + "---"*len(self.adjacency_matrix)) 
        for i, row in enumerate(self.adjacency_matrix, start=1):
            print(f"{i} | {'  '.join(str(int(cell)) for cell in row)}")
        
    def print_table(self, graph_data):
        for connection in graph_data:
            print(f"{connection[0]} -> {connection[1]}")


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
        elif graph_type == "Table":
            i = int(input("Enter starting vertex: "))
            j = int(input("Enter ending vertex: "))
            if (i, j) in graph_data:
                print(f"Edge from {i} to {j} exists")
            else:
                print(f"Edge from {i} to {j} does not exist")
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
                    if not visited[neighbor ]:  
                        queue.append(neighbor )
                        visited[neighbor ] = True
        elif graph_type == "Table":
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

                for connection in graph_data:
                    if connection[0] == vertex + 1 and not visited[connection[1] - 1]:  
                        queue.append(connection[1] - 1)
                        visited[connection[1] - 1] = True
                
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
            start = int(input("Enter starting vertex: ")) - 1 
            visited = [False] * len(graph_data)
            self.dfs_util(graph_data, start, visited)
            print()
        elif graph_type == "List":
            start = int(input("Enter starting vertex: ")) - 1 
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
            if not visited[neighbor]: 
                self.dfs_util_list(graph_data, neighbor, visited)



    def khan(self, graph_type, graph_data):
        if graph_type == "Matrix":
            in_degree = [0] * len(graph_data)
            for i in range(len(graph_data)):
                for j in range(len(graph_data)):
                    if graph_data[i][j] == 1:
                        in_degree[j] += 1

            queue = []
            for i in range(len(in_degree)):
                if in_degree[i] == 0:
                    queue.append(i)

            top = []
            while queue:
                vertex = queue.pop(0)
                top.append(vertex + 1)

                for i in range(len(graph_data)):
                    if graph_data[vertex][i] == 1:
                        in_degree[i] -= 1
                        if in_degree[i] == 0:
                            queue.append(i)

            if len(top) == len(graph_data):
                print("Topological order:", top)
            else:
                print("Graph has a cycle")

        elif graph_type == "List":
            in_degree = [0] * len(graph_data)
            for neighbors in graph_data:
                for neighbor in neighbors:
                    in_degree[neighbor] += 1

            queue = []
            for i in range(len(in_degree)):
                if in_degree[i] == 0:
                    queue.append(i)

            top = []
            while queue:
                vertex = queue.pop(0)
                top.append(vertex + 1)

                for neighbor in graph_data[vertex]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)

            if len(top) == len(graph_data):
                print("Topological order:", top)
            else:
                print("Graph contains a cycle")

        else:
            print("Invalid graph type")

    def tarjan(self, graph_type, graph_data):
        if graph_type == "Matrix":
            visited = [False] * len(graph_data)
            stack = []
            for i in range(len(graph_data)):
                if not visited[i]:
                    self.tarjan_dfs_util(graph_data, i, visited, stack)
            topological_order = []
            while stack:
                topological_order.append(stack.pop())
            print("Topological order:", topological_order[::-1])
        elif graph_type == "List":
            visited = [False] * len(graph_data)
            stack = []
            for i in range(len(graph_data)):
                if not visited[i]:
                    self.tarjan_dfs_util_list(graph_data, i, visited, stack)
            topological_order = []
            while stack:
                topological_order.append(stack.pop())
            print("Topological order:", topological_order)
        else:
            print("Invalid graph type")

    def tarjan_dfs_util(self, graph_data, vertex, visited, stack):
        visited[vertex] = True
        for i in range(len(graph_data)):
            if graph_data[vertex][i] == 1 and not visited[i]:
                self.tarjan_dfs_util(graph_data, i, visited, stack)
        stack.append(vertex + 1)

    def tarjan_dfs_util_list(self, graph_data, vertex, visited, stack):
        visited[vertex] = True
        for neighbor in graph_data[vertex]:
            if not visited[neighbor-1]:
                self.tarjan_dfs_util_list(graph_data, neighbor, visited, stack)
        stack.append(vertex + 1)
    

    def export_to_tikz(self, graph_type, graph_data, file_path):
        if graph_type == "Matrix":
            with open(file_path, "w") as file:
                file.write("\\documentclass{standalone}\n")
                file.write("\\usepackage{tikz}\n")
                file.write("\\begin{document}\n")
                file.write("\\begin{tikzpicture}\n")
                for i in range(len(graph_data)):
                    angle = i * (360 / len(graph_data))
                    x = 2 * math.cos(math.radians(angle))
                    y = 2 * math.sin(math.radians(angle))
                    file.write(f"\\node ({i+1}) at ({x},{y}) {{{i+1}}};\n")
                for i in range(len(graph_data)):
                    for j in range(len(graph_data)):
                        if graph_data[i][j] == 1:
                            file.write(f"\\draw[->] ({i+1}) -- ({j+1});\n")
                file.write("\\end{tikzpicture}\n")
                file.write("\\end{document}\n")
            print(f"Graph exported to {file_path}")
        elif graph_type == "List":
            with open(file_path, "w") as file:
                file.write("\\documentclass{standalone}\n")
                file.write("\\usepackage{tikz}\n")
                file.write("\\begin{document}\n")
                file.write("\\begin{tikzpicture}\n")
                for i, neighbors in enumerate(graph_data, start=1):
                    angle = i * (360 / len(graph_data))
                    x = 2 * math.cos(math.radians(angle))
                    y = 2 * math.sin(math.radians(angle))
                    file.write(f"\\node ({i}) at ({x},{y}) {{{i}}};\n")
                for i, neighbors in enumerate(graph_data, start=1):
                    for neighbor in neighbors:
                        file.write(f"\\draw[->] ({i}) -- ({neighbor+1});\n")
                file.write("\\end{tikzpicture}\n")
                file.write("\\end{document}\n")
            print(f"Graph exported to {file_path}")
        elif graph_type == "Table":
            with open(file_path, "w") as file:
                file.write("\\documentclass{standalone}\n")
                file.write("\\usepackage{tikz}\n")
                file.write("\\begin{document}\n")
                file.write("\\begin{tikzpicture}\n")
                for i, neighbors in enumerate(graph_data, start=1):
                    angle = i * (360 / len(graph_data))
                    x = 2 * math.cos(math.radians(angle))
                    y = 2 * math.sin(math.radians(angle))
                    file.write(f"\\node ({i}) at ({x},{y}) {{{i}}};\n")
                    for neighbor in neighbors:
                        file.write(f"\\draw[->] ({i}) -- ({neighbor+1});\n")
                file.write("\\end{tikzpicture}\n")
                file.write("\\end{document}\n")
            print(f"Graph exported to {file_path}")
        else:
            print("Invalid graph type")
