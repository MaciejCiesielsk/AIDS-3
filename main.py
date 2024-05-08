import sys
import os 
import argparse 
from zadanie3.graph import Graph


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
                print("Breath - breath first search")
                print("Depth - depth first search")
                print("Back - back to main menu")
                print("Exit - exit program")
                print("-".center(50, "-"))
                continue

            if action == "print":
                print(generation)
                continue

            if action == "exit":
                break

            if action == "back":
                main()
                break

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
                print("Breath - breath first search")
                print("Depth - depth first search")
                print("Back - back to main menu")
                print("Exit - exit program")
                print("-".center(50, "-"))
                continue

            if action == "print":
                print(user)
                continue

            if action == "exit":
                break

            if action == "back":
                main()
                break

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