import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import json
from graph_tools import *
import scipy as sp

def checkDuplicate(graph, nodeName):
    for i in list(graph.nodes): # make sure no node with same name
        if i == nodeName:
            return True # duplicate exists
    return False # no duplicate

def addNodeUser(graph, nodeName, details = None): # default value for details is null. If details are passed they will be used
    graph.add_node(nodeName, details = json.loads(details)) if details !=  None else graph.add_node(nodeName)
    print(f'{nodeName} Successfully added')
    saveGraph(graph)

def addEdgeUser(graph, sourceNode, destinationNode, relationship):
    graph.add_edge(sourceNode, destinationNode, relationship = relationship)
    saveGraph(graph)

def removeNodeUser(graph, nodeName):
    try:
        graph.remove_node(nodeName)
        print(f'{nodeName} Successfully Removed')
        saveGraph(graph) 
    except nx.exception.NetworkXError:
        print(f'Node {nodeName} Does Not Exist')
      

def removeEdgeUser(graph, sourceNode, destinationNode):
    try:
        graph.remove_edge(sourceNode, destinationNode)
        print(f'Edge {sourceNode} -> {destinationNode} Successfully Removed')
        saveGraph(graph)
    except nx.exception.NetworkXError:
        print(f'Edge {sourceNode} -> {destinationNode} Does Not Exist')
    

def addNode(graph, nodeName, details = None): # default value for details is null. If details are passed they will be used 
    graph.add_node(nodeName, details = details) if details !=  None else graph.add_node(nodeName)
    

def addEdge(graph, sourceNode, destinationNode, relationship):
    graph.add_edge(sourceNode, destinationNode, relationship = relationship)

def displayGraphPlanarLayout(graph):
    # Position the nodes using a spring layout algorithm
    pos = nx.planar_layout(graph)

    # Customize the node and edge attributes as needed
    node_size = 2000
    node_color = 'gray'
    font_size = 10
    font_color = 'black'
    edge_color = 'gray'

    # Draw the graph
    nx.draw(graph, pos, with_labels=True, node_size=node_size, node_color=node_color, font_size=font_size, font_color=font_color, edge_color=edge_color)
    edge_labels = getEdgeLabels(graph)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title("Graph Visualization")
    plt.show()

def displayGraphKamadaKawaiLayout(graph):
    # Position the nodes using a spring layout algorithm
    pos = nx.kamada_kawai_layout(graph)

    # Customize the node and edge attributes as needed
    node_size = 2000
    node_color = 'gray'
    font_size = 10
    font_color = 'black'
    edge_color = 'gray'

    # Draw the graph
    nx.draw(graph, pos, with_labels=True, node_size=node_size, node_color=node_color, font_size=font_size, font_color=font_color, edge_color=edge_color)
    edge_labels = getEdgeLabels(graph)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title("Graph Visualization")
    plt.show()


def displayGraphSpectralLayout(graph, centralNode = None):
    # Position the nodes using a spring layout algorithm
    pos = nx.spectral_layout(graph, center=["KAU"])

    # Customize the node and edge attributes as needed
    node_size = 2009
    node_color = 'gray'
    font_size = 10
    font_color = 'black'
    edge_color = 'gray'

    # Draw the graph
    nx.draw(graph, pos, with_labels=True, node_size=node_size, node_color=node_color, font_size=font_size, font_color=font_color, edge_color=edge_color)
    edge_labels = getEdgeLabels(graph)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title("Graph Visualization")
    plt.show()

def displayGraphCommandLine(graph):
    # display nodes of the graph
    # display details of the node 
    # also display relations of the graph

    for i in graph.nodes().data():
        print(f'Node Name -> {i[0]}')
        if len(i[1]) > 0:
            print("\t- Details:")
            details = i[1]['details']
            for j in details:
                print(f'\t\t{j}: {details[j]}')
        print("\t- Relations:")
        for j in graph.edges().data(): # for all edges in the graph
            if j[0] == i[0] or j[1] == i[0]: # i -> node name. j[0] src node, j[1] dest node.
                relationship = j[2]['relationship']
                print(f'\t\t{j[0]} {relationship} {j[1]}')

def getEdgeLabels(graph):
    # this method return the labels to use in displaying the graph
    edge_labels = {}

    for edge in graph.edges():
        relatioship = graph.get_edge_data(edge[0], edge[1]) # relatioship dictionary object -> {'relationship' : 'someRelationship'}
        edge_labels[edge] = relatioship['relationship'] # use the value of the 'relationship' key

    return edge_labels

def getNodeInformation(nodeName):
    if not nodeExists:
        return f'Node {nodeName} does not exist'

    graph = loadGraph()
    information = f'\nNode {nodeName} Information:\n'
    for i in graph.nodes().data():
        if i[0] == nodeName:
            if len(i[1]) > 0: # if node has details
                details = i[1]['details']
                for j in details: # add details to string
                    information += f'\t{j}: {details[j]}\n'
            else:
                information = f'Node {nodeName} has no additional details'
            break
    return information


def getNodeRelations(nodeName):
    if not nodeExists:
        return f'Node {nodeName} does not exist'
    
    graph = loadGraph()
    information = f'Node {nodeName} Relationships:\n'
    informationCheck = information

    # edge_details = G.get_edge_data(node1, node2)
    
    for i in graph.edges().data():
        if i[0] == nodeName or i[1] == nodeName:
            relationship = i[2]['relationship']
            information += f'\t{i[0]} {relationship} {i[1]}\n'

    # return information
    if information == informationCheck:
        return f'Node {nodeName} has no relationships'
    else:
        return information

def nodeExists(nodeName): # method to check if node exists in graph
    graph = loadGraph()

    for i in graph.nodes().data():
        if i[0] == nodeName:
            return True
    return False

def saveGraph(graph):
    # this method saves the graph into a JSON file so that it can be used to query the net
    with open('semanticNet.json', 'r+') as file:
        file.truncate(0)
        data = nx.node_link_data(graph)
        json.dump(data, file)

def loadGraph():
    # this method loads the graph from the JSON file 
    with open('semanticNet.json', 'r+') as file:
        data = json.load(file)
        graph = nx.node_link_graph(data)
    
    return graph

