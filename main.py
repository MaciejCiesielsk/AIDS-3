import sys
import os 
import argparse 

parser=argparse.ArgumentParser()
parser.add_argument("-generate", action="store_true" , help="Generate random graph")
parser.add_argument("-user-provided", action="store_true" , help="Generate graph from user input")
args = parser.parse_args()

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

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
    
    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False
        
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors))

class Matrix:
    vertices = {}
    edges = []
    edge_indices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges)+1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
        else:
            return False
    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = 1
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = 1
            return True
        else:
            return False
        
    def print_graph(self):
        for i in range(0, len(self.edges)):
            print(str(i) + str(self.edges[i]))
    
def chosenGraph(graph_type, graph):
    if args.generate:
        if graph_type == "Matrix":
            graph = Matrix()
            print(f"---Graph type: {graph_type}---")
            print("Type Help for list of commands")
            
            while True:
                action = input('action> ').lower()
                print(action)
                if action == "help":
                    print("Help".center(50, "-"))
                    print("List of commands:")
                    print("Print - print graph")
                    print("Find - find edge from _ to _ ")
                    print()
                    print("Exit - exit program")
                    continue

                if action == "print":
                    graph.print_graph()
                    continue
                if action == "exit":
                    break

        elif graph_type == "List":
            graph = List()
        for i in range(0, 5):
            graph.add_vertex(Vertex(str(i)))
        edges = ['01', '12', '23', '34', '40']
        for edge in edges:
            graph.add_edge(edge[:1], edge[1:])
        graph.print_graph()
    elif args.user_provided:
        if graph_type == "Matrix":
            graph = Matrix()
        else:
            graph = List()
        for i in range(0, 5):
            graph.add_vertex(Vertex(str(i)))
        edges = ['01', '12', '23', '34', '40']
        for edge in edges:
            graph.add_edge(edge[:1], edge[1:])
        graph.print_graph()
    else:
        print("Please provide an argument -generate or -user-provided")
        sys.exit(1)






def main():
    graph_matrix = Matrix()
    graph_list = List()
    if args.generate:
        command=input("Choose graph type: Matrix or List: ")
        if command == "Matrix":
            chosenGraph("Matrix", graph_matrix)
        elif command == "List":
            chosenGraph("List", graph_list)
    elif args.user_provided:
        command=input("Choose graph type: Matrix or List: ")
        if command == "Matrix":
            chosenGraph("Matrix", graph_matrix)
        elif command == "List":
            chosenGraph("List", graph_list)
    else:
        print("Please provide an argument -generate or -user-provided")
        sys.exit(1)

        

if __name__ == "__main__":
    main()