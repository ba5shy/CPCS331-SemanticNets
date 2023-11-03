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

# def displayGraph(graph):
#     pos = nx.spring_layout(graph)
    
#     # Create nodes trace
#     nodes_trace = go.Scatter(
#         x=[pos[node][0] for node in graph.nodes()],
#         y=[pos[node][1] for node in graph.nodes()],
#         mode='markers',
#         marker=dict(size=20, color='gray', opacity=0.9),
#         text=[node for node in graph.nodes()],
#         hoverinfo='text'
#     )

#     edge_labels = getEdgeLabels(graph)
    
#     # Create edges trace
#     edges_trace = go.Scatter(
#         x=[],
#         y=[],
#         line=dict(width=3, color='black'),
#         hoverinfo='none',
#         mode='lines'
#     )

#     for edge in graph.edges():
#         x0, y0 = pos[edge[0]]
#         x1, y1 = pos[edge[1]]
#         edges_trace['x'] += (x0, x1, None)
#         edges_trace['y'] += (y0, y1, None)

#     # Create a figure
#     fig = go.Figure(data=[nodes_trace, edges_trace])
    
#     # Add edge labels using annotations
#     for edge, label in edge_labels.items():
#         x0, y0 = pos[edge[0]]
#         x1, y1 = pos[edge[1]]
#         annotation = go.Annotation(
#             text=label,
#             x=(x0 + x1) / 2,
#             y=(y0 + y1) / 2,
#             showarrow=False,
#             font=dict(size=10),
#         )
#         fig.add_annotation(annotation)
    
#     # Update layout to add a title and make the plot more visually appealing
#     fig.update_layout(
#         title_text='Graph Visualization using Plotly',
#         showlegend=False,
#         hovermode='closest',
#         margin=dict(b=0, t=40, l=0, r=0),
#     )
    
#     # Show the plot
#     fig.show()

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
                    information += f'{j}: {details[j]}\n'
            else:
                information = f'Node {nodeName} has no additional details'
            break
    return information


def getNodeRelations(nodeName):
    if not nodeExists:
        return f'Node {nodeName} does not exist'
    
    graph = loadGraph()
    information = f'\nNode {nodeName} Relationships:\n'
    informationCheck = information

    # edge_details = G.get_edge_data(node1, node2)
    
    for i in graph.edges().data():
        if i[0] == nodeName or i[1] == nodeName:
            relationship = i[2]['relationship']
            information += f'{i[0]} {relationship} {i[1]}\n'

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


getNodeRelations("CPCS-203")