import networkx as nx
import plotly.graph_objs as go
import json
import scipy as sp

def addNode(graph, nodeName, details = None): # default value for details is null. If details are passed they will be used 
    graph.add_node(nodeName, details = details) if details !=  None else graph.add_node(nodeName)

def addEdge(graph, sourceNode, destinationNode, relationship):
    graph.add_edge(sourceNode, destinationNode, relationship = relationship)

def removeNode(graph, nodeName):
    pass    

def removeEdge(graph, sourceNode, destinationNode, relationship):
    pass

# def displayGraph(graph):
#     pos = nx.spring_layout(graph)
#     nx.draw(
#         graph, pos, edge_color='black', width=3, linewidths=1,
#         node_size=2000, node_color='gray', alpha=0.9,
#         labels={node: node for node in graph.nodes()}
#     )

#     edge_labels = getEdgeLabels(graph)

#     nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
#     plt.show() # display the graph
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
def displayGraph(graph):
    pos = nx.kamada_kawai_layout(graph)  # Use Kamada-Kawai layout for better results

    nodes_trace = go.Scatter(
        x=[pos[node][0] for node in graph.nodes()],
        y=[pos[node][1] for node in graph.nodes()],
        mode='markers',
        marker=dict(size=20, color='gray', opacity=0.9),
        text=[node for node in graph.nodes()],
        hoverinfo='text'
    )

    edge_labels = getEdgeLabels(graph)

    edges_trace = go.Scatter(
        x=[],
        y=[],
        line=dict(width=3, color='black'),
        hoverinfo='none',
        mode='lines'
    )

    for edge in graph.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edges_trace['x'] += (x0, x1, None)
        edges_trace['y'] += (y0, y1, None)

    fig = go.Figure(data=[nodes_trace, edges_trace])

    for edge, label in edge_labels.items():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        annotation = go.Annotation(
            text=label,
            x=(x0 + x1) / 2,
            y=(y0 + y1) / 2,
            showarrow=False,
            font=dict(size=10),
        )
        fig.add_annotation(annotation)

    fig.update_layout(
        title_text='Graph Visualization using Plotly',
        showlegend=False,
        hovermode='closest',
        margin=dict(b=0, t=40, l=0, r=0),
    )

    fig.show()

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
