import networkx as nx
import matplotlib.pyplot as plt
import json

def addNode(graph, nodeName):
    graph.add_node(nodeName)

def addEdge(graph, sourceNode, destinationNode, relationship):
    graph.add_edge(sourceNode, destinationNode, relationship = relationship)

def removeNode(graph, nodeName):
    pass    

def removeEdge(graph, sourceNode, destinationNode, relationship):
    pass

def displayGraph(graph):
    pos = nx.spring_layout(graph)
    nx.draw(
        graph, pos, edge_color='black', width=3, linewidths=1,
        node_size=2000, node_color='gray', alpha=0.9,
        labels={node: node for node in graph.nodes()}
    )

    edge_labels = getEdgeLabels(graph)

    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.show() # display the graph

def getEdgeLabels(graph):
    # this method return the labels to use in displaying the graph
    edge_labels = {}

    for edge in graph.edges():
        relatioship = graph.get_edge_data(edge[0], edge[1]) # relatioship dictionary object -> {'relationship' : 'someRelationship'}
        edge_labels[edge] = relatioship['relationship'] # use the value of the 'relationship' key

    return edge_labels

def saveGraph(graph):
    # this method saves the graph into a JSON file so that it can be used to query the net
    with open('semanticNet.json', 'r+') as file:
        data = nx.node_link_data(graph)
        json.dump(data, file)

def loadGraph():
    # this method loads the graph from the JSON file 
    with open('semanticNet.json', 'r+') as file:
        data = json.load(file)
        graph = nx.node_link_graph(data)
    
    return graph