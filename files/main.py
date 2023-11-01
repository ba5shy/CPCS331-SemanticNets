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
gf.addNode(university, "Math") # create Math node

# link Physics, Chemistry, and Math nodes
gf.addEdge(university, "Physics", "SCIENCES_Department", "is_a") # Physics is a SCIENCES_Department
gf.addEdge(university, "Chemistry", "SCIENCES_Department", "is_a") # Chemistry is a SCIENCES_Department
gf.addEdge(university, "Math", "SCIENCES_Department", "is_a") # Math is a SCIENCES_Department

# create ENG nodes
gf.addNode(university, "Mechanical ENG") # create Mechanical Eng node
gf.addNode(university, "Computer ENG") # create Computer ENG node
gf.addNode(university, "Industrial ENG") # create Industrial ENG node

# link Mechanical, Computer, and Industrial ENG nodes
gf.addEdge(university, "Mechanical ENG", "ENG_Department", "is_a") # Mechanical ENG is a ENG_Department
gf.addEdge(university, "Computer ENG", "ENG_Department", "is_a") # Computer ENG is a ENG_Department
gf.addEdge(university, "Industrial ENG", "ENG_Department", "is_a") # Industrail ENG is a ENG_Department

# add courses to FCIT-CS
gf.addNode(university, "202", details={
    'Course Name': 'Programming I',
    'Department': 'CS',
    'Course Code': 'CPCS-202'
})
gf.addNode(university, "203", details={
    'Course Name': 'Programming II',
    'Department': 'CS',
    'Course Code': 'CPCS-203'
})
gf.addNode(university, "331", details={
    'Course Name': 'Artificial Intelligence I',
    'Department': 'CS',
    'Course Code': 'CPCS-331'
})

# link courses to CS department
gf.addEdge(university, "CS", "202", "Offers")
gf.addEdge(university, "CS", "203", "Offers")
gf.addEdge(university, "CS", "331", "Offers")

# add courses to FCIT-IT
gf.addNode(university, "221", details={
    'Course Name': 'Technical Writing',
    'Department': 'IT',
    'Course Code': 'CPIT-221'
})
gf.addNode(university, "201", details={
    'Course Name': 'Introduction to Computing',
    'Department': 'IT',
    'Course Code': 'CPIT-201'
})
gf.addNode(university, "110", details={
    'Course Name': 'Programming and Problem Solving',
    'Department': 'IT',
    'Course Code': 'CPIT-110'
})

# link courses to IT department
gf.addEdge(university, "IT", "221", "Offers")
gf.addEdge(university, "IT", "201", "Offers")
gf.addEdge(university, "IT", "110", "Offers")

# add courses to FCIT-IS
gf.addNode(university, "334", details={
    'Course Name': 'Introduction to Software Project Management',
    'Department': 'IS',
    'Course Code': 'CPIS-334'
})
gf.addNode(university, "428", details={
    'Course Name': 'Professional Computing Issues',
    'Department': 'IS',
    'Course Code': 'CPIS-428'
})
gf.addNode(university, "210", details={
    'Course Name': 'Computer Architecture and Organization',
    'Department': 'IS',
    'Course Code': 'CPIS-210'
})

# link courses to IS department
gf.addEdge(university, "IS", "334", "Offers")
gf.addEdge(university, "IS", "428", "Offers")
gf.addEdge(university, "IS", "210", "Offers")

# add courses to SCIENCES-Physics
gf.addNode(university, "110", details={
    'Course Name': 'General Physics I',
    'Department': 'Physics',
    'Course Code': 'PHYS-110'
})
gf.addNode(university, "202", details={
    'Course Name': 'General Physics II',
    'Department': 'Physics',
    'Course Code': 'PHYS-202'
})
gf.addNode(university, "203", details={
    'Course Name': 'General Physics III',
    'Department': 'Physics',
    'Course Code': 'PHYS-203'
})

# link courses to Physics department
gf.addEdge(university, "Physics", "110", "Offers")
gf.addEdge(university, "Physics", "202", "Offers")
gf.addEdge(university, "Physics", "203", "Offers")


# add courses to SCIENCES-Chemistry
gf.addNode(university, "110", details={
    'Course Name': 'General Chemistry I',
    'Department': 'Chemistry',
    'Course Code': 'CHEM-110'
})
gf.addNode(university, "202", details={
    'Course Name': 'General Chemistry II',
    'Department': 'Chemistry',
    'Course Code': 'CHEM-202'
})
gf.addNode(university, "205", details={
    'Course Name': 'Introduction to Natural Sciences',
    'Department': 'Chemistry',
    'Course Code': 'CHEM-203'
})

# link courses to Chemistry department
gf.addEdge(university, "Chemistry", "110", "Offers")
gf.addEdge(university, "Chemistry", "202", "Offers")
gf.addEdge(university, "Chemistry", "203", "Offers")


# add courses to SCIENCES-Math
gf.addNode(university, "110", details={
    'Course Name': 'Calculus I',
    'Department': 'Math',
    'Course Code': 'MATH-110'
})
gf.addNode(university, "202", details={
    'Course Name': 'Calculus II',
    'Department': 'Math',
    'Course Code': 'MATH-202'
})
gf.addNode(university, "203", details={
    'Course Name': 'Calculus III',
    'Department': 'Math',
    'Course Code': 'MATH-203'
})

# link courses to Math department
gf.addEdge(university, "Math", "110", "Offers")
gf.addEdge(university, "Math", "202", "Offers")
gf.addEdge(university, "Math", "203", "Offers")


#gf.displayGraph(university)
gf.saveGraph(university)

