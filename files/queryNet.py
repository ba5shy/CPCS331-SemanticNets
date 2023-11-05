# this file is to be used by the user to interact with the semantic net
# The user may  
#   - Create base graph
#   - Add or remove nodes or edges
#   - Query the net (relationships and nodes)

import graphFunctions as gf
import mainGraph as mg

def printMainMenu():
    print("------------------------------------------------------")
    print("1) Create Main Graph (overwrite current graph)")
    print("2) Add Node to Graph")
    print("3) Add Edge to Graph")
    print("4) Remove Node from Graph")
    print("5) Remove Edge from Graph")
    print("6) Query Net")
    print("7) Display Graph")
    print("8) Exit")
    print("------------------------------------------------------\n")

def printDisplayMenu():
    print("---------------------Choose Layout----------------------")
    print("1) Planar Layout")
    print("2) Kamada Kawai Layout")
    print("3) Spectral Layout")
    print("4) Command Line")
    print("5) Go Back")
    print("------------------------------------------------------\n")


graph = gf.loadGraph() # load graph from semanticNet.json

while 1:
    printMainMenu()
    choice = input("Enter Choice: ")
    
    try:
        choice = int(choice)
    except:
        print("Enter a Number ")

    if choice == 1: # create main graph
        graph = mg.createMainGraph()
        gf.saveGraph(graph)


    elif choice == 2: # add node to graph
        nodeName = input("Enter Node Name: ") # user enters node name
        duplicate = gf.checkDuplicate(graph, nodeName) # check if node with same name exists
        if not duplicate: # if not duplicate add node
            details = input('''Enter Details (Optional): format -> {"key": value, "key",: value}\n''')
            gf.addNodeUser(graph, nodeName, details)
        else: # else promt user to enter different name
            print(f'{nodeName} Node Already Exists')
            
    elif choice == 3: # add edge to graph
        # if nodes dont exist, edge creation will also create the nodes
        sourceNode = input("Enter source node name: ")
        destinationNode = input("Enter destination node name: ")
        relationship = input("Enter relationship between nodes (src -> dest): ")
        gf.addEdgeUser(graph, sourceNode, destinationNode, relationship)


    elif choice == 4: # remove node from graph
        nodeName = input("Enter node to remove: ")
        gf.removeNodeUser(graph, nodeName)
            
    
    elif choice == 5: # remove edge from graph
        sourceNode = input("Enter source node name: ")
        destinationNode = input("Enter destination node name: ")
        gf.removeEdgeUser(graph, sourceNode, destinationNode)


    elif choice == 6: # query net 
        nodeName = input("Enter node name: ")
        print(gf.getNodeInformation(nodeName))
        print(gf.getNodeRelations(nodeName))


    elif choice == 7:
        while 1:
            printDisplayMenu()
            displayChoice = input("Enter Choice: ")
            try:
                displayChoice = int(displayChoice)
            except:
                print("Enter a Number ")
            if displayChoice == 1:
                gf.displayGraphPlanarLayout(graph)
            elif displayChoice == 2:
                gf.displayGraphKamadaKawaiLayout(graph)
            elif displayChoice == 3:
                gf.displayGraphSpectralLayout(graph)
            elif displayChoice == 4:
                gf.displayGraphCommandLine(graph)
            elif displayChoice == 5:
                break


    elif choice == 8:
        break
    
         

    
