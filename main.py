import sys
import os 
import argparse 
from graph import Graph
import math

CURRENT_DIR = os.path.dirname(__file__)

parser=argparse.ArgumentParser()
parser.add_argument("-generate", action="store_true" , help="Generate random graph")
parser.add_argument("-user-provided", action="store_true" , help="Generate graph from user input")
args = parser.parse_args()

def chosenGraph(graph_type, graph):
    if args.generate:
        saturation = float(input("Enter saturation: "))
        nodes = int(input("Enter number of nodes: "))
        generation = graph.generate(saturation, nodes, graph_type)
        print(f"---Graph type: {graph_type}---")
        print("Type Help for list of commands")
        while True:
            action = input('action> ').lower()
            if action == "help":
                print("Help".center(50, "-"))
                print("List of commands:")
                print("Print - print graph")
                print("Find - find edge from _ to _ ")
                print("BFS - breath first search")
                print("DFS - depth first search")
                print("Back - back to main menu")
                print("Exit - exit program")
                print("-".center(50, "-"))
                continue

            if action == "print":
                if graph_type == "Matrix":
                    graph.print_matrix()
                elif graph_type == "List":
                    graph.print_list(generation,graph_type)
                continue

            if action == "exit":
                break

            if action == "back":
                main()
                break

            if action == "find":
                graph.find_edge(graph_type, generation)
                continue

            if action == "bfs":
                graph.bfs(graph_type, generation, int(input("Enter starting vertex: ")))
                continue

            if action == "dfs":
                graph.dfs(graph_type, generation)
                continue

            if action == "khan":
                graph.khan(graph_type, generation)
                continue
            if action == "tarjan":
                graph.tarjan(graph_type, generation)
                continue
            
            if action == "export":
                graph.export_to_tikz(graph_type, generation,os.path.join(CURRENT_DIR, f"tikzpicture{graph_type}.txt"))
                continue

            else:
                print("Invalid command")

    elif args.user_provided:
        user = graph.user_provided_graph(graph_type)
        print(f"---Graph type: {graph_type}---")
        print("Type Help for list of commands")
        while True:
            action = input('action> ').lower()
            if action == "help":
                print("Help".center(50, "-"))
                print("List of commands:")
                print("Print - print graph")
                print("Find - find edge from _ to _ ")
                print("BFS - breath first search")
                print("DFS - depth first search")
                print("Back - back to main menu")
                print("Exit - exit program")
                print("Khan - topological sort using Khan's algorithm")
                print("-".center(50, "-"))
                continue

            if action == "print":
                if graph_type == "Matrix":
                    graph.print_matrix()
                elif graph_type == "List":
                    graph.print_list(user,graph_type)
                continue

            if action == "exit":
                break

            if action == "back":
                main()
                break

            if action == "find":
                graph.find_edge(graph_type,user)
                continue

            if action == "bfs":
                graph.bfs(graph_type, user, int(input("Enter starting vertex: "))-1)
                print()
                continue

            if action == "dfs":
                graph.dfs(graph_type, user)
                print()
                continue

            if action == "khan":
                graph.khan(graph_type, user)

            if action == "tarjan":
                graph.tarjan(graph_type, user)
                continue

            if action == "export":
                graph.export_to_tikz(graph_type, user,os.path.join(CURRENT_DIR, f"tikzpicture{graph_type}.txt"))
                continue
            else:
                print("Invalid command")
    else:
        print("Please provide an argument -generate or -user-provided")
        sys.exit(1)

def main():
    graph = Graph()
    if args.generate:
        command = input("Choose graph type: Matrix or List: ")
        if command == "Matrix":
            chosenGraph("Matrix", graph)
        elif command == "List":
            chosenGraph("List", graph)
    elif args.user_provided:
        command = input("Choose graph type: Matrix or List: ")
        if command == "Matrix":
            chosenGraph("Matrix", graph)
        elif command == "List":
            chosenGraph("List", graph)
    else:
        print("Please provide an argument -generate or -user-provided")
        sys.exit(1)

        

if __name__ == "__main__":
    main()