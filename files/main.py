# main file only creates the graph, adds the nodes and the edges. 
# Querying the net is done through the queryNet.py file

# networkx is installed using pip in a virtual environment
# networkx is an external library that helps with the creation of Graphs
import networkx as nx
import graphFunctions as gf
# the domain is a university 
# create a directed graph called university
university = nx.DiGraph()

gf.addNode(university, "KAU") # create KAU node
gf.addNode(university, "FCIT") # create FCIT node
gf.addNode(university, "SCIENCES") # create SCIENCES node
gf.addNode(university, "ENG") # create ENG node

# link colleges with KAU
gf.addEdge(university, "KAU", "FCIT", "contains") # link KAU and FCIT (KAU contains (->) FCIT)
gf.addEdge(university, "KAU", "SCIENCES", "contains") # link KAU and SCIENCEs (KAU contains (->) SCIENCEs)
gf.addEdge(university, "KAU", "ENG", "contains") # link KAU and ENG (KAU contains (->) ENG)


# create departments for each faculty (college)
gf.addNode(university, "FCIT_Department")
gf.addNode(university, "SCIENCES_Department")
gf.addNode(university, "ENG_Department")

#link departments to colleges
gf.addEdge(university, "FCIT", "FCIT_Department", "has") # link FCIT and Departments (FCIT has (->) Departments)
gf.addEdge(university, "SCIENCES", "SCIENCES_Department", "has") # link SCIENCES and Departments (SCIENCES has (->) Departments)
gf.addEdge(university, "ENG", "ENG_Department", "has") # link ENG and Departments (ENG has (->) Departments)

# create FCIT nodes
gf.addNode(university, "CS") # create CS node
gf.addNode(university, "IT") # create IT node
gf.addNode(university, "IS") # create IS node

# link CS, IT, and IS nodes
gf.addEdge(university, "CS", "FCIT_Department", "is_a") # CS is a FCIT_Department
gf.addEdge(university, "IT", "FCIT_Department", "is_a") # IT is a FCIT_Department
gf.addEdge(university, "IS", "FCIT_Department", "is_a") # IS is a FCIT_Department


# create SCIENCES nodes
gf.addNode(university, "Physics") # create phyiscs node
gf.addNode(university, "Chemistry") # create chemistry node
gf.addNode(university, "Biology") # create biology node

# link Physics, Chemistry, and Biology nodes
gf.addEdge(university, "Physics", "SCIENCES_Department", "is_a") # Physics is a SCIENCES_Department
gf.addEdge(university, "Chemistry", "SCIENCES_Department", "is_a") # Chemistry is a SCIENCES_Department
gf.addEdge(university, "Biology", "SCIENCES_Department", "is_a") # Biology is a SCIENCES_Department

# create ENG nodes
gf.addNode(university, "Mechanical ENG") # create Mechanical Eng node
gf.addNode(university, "Computer ENG") # create Computer ENG node
gf.addNode(university, "Industrial ENG") # create Industrial ENG node

# link Physics, Chemistry, and Biology nodes
gf.addEdge(university, "Mechanical ENG", "ENG_Department", "is_a") # Mechanical ENG is a ENG_Department
gf.addEdge(university, "Computer ENG", "ENG_Department", "is_a") # Computer ENG is a ENG_Department
gf.addEdge(university, "Industrial ENG", "ENG_Department", "is_a") # Industrail ENG is a ENG_Department

gf.displayGraph(university)



