import sys
import os 
import argparse 

from list import Vertex, List
from matrix import Matrix


parser=argparse.ArgumentParser()
parser.add_argument("-generate", action="store_true" , help="Generate random graph")
parser.add_argument("-user-provided", action="store_true" , help="Generate graph from user input")
args = parser.parse_args()

   
    
def chosenGraph(graph_type, graph):
    if args.generate:
        saturation = float(input("Enter saturation: "))
        nodes = int(input("Enter number of nodes: "))
        generation = graph.generate_graph(saturation, nodes)
        if graph_type == "Matrix":
            g = Matrix()
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

        elif graph_type == "List":
            g = List()
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
                    if generation is not None:
                        for i, neighbors in enumerate(generation):
                            print(f"{i + 1}: {neighbors}")                   
                    continue


                if action == "exit":
                    break

                if action == "back":
                    main()
                    break
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