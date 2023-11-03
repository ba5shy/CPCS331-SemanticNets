# main file only creates the initial graph, adds the nodes and the edges. 
# Querying the net is done through the queryNet.py file
# The user can also add and delete nodes using the queryNet.py file≠

# networkx is installed using pip in a virtual environment
# networkx is an external library that helps with the creation of Graphs
import networkx as nx
import graphFunctions as gf 
# the domain is a university 
# create a directed graph called university

def createMainGraph():

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
    gf.addNode(university, "CPCS-202", details={
        'Course Name': 'Programming I',
        'Department': 'CS'
    })
    gf.addNode(university, "CPCS-203", details={
        'Course Name': 'Programming II',
        'Department': 'CS'
    })
    gf.addNode(university, "CPCS-331", details={
        'Course Name': 'Artificial Intelligence I',
        'Department': 'CS'
    })

    # link courses to CS department
    gf.addEdge(university, "CS", "CPCS-202", "Offers")
    gf.addEdge(university, "CS", "CPCS-203", "Offers")
    gf.addEdge(university, "CS", "CPCS-331", "Offers")

    # add courses to FCIT-IT
    gf.addNode(university, "CPIT-221", details={
        'Course Name': 'Technical Writing',
        'Department': 'IT'
    })
    gf.addNode(university, "CPIT-201", details={
        'Course Name': 'Introduction to Computing',
        'Department': 'IT'
    })
    gf.addNode(university, "CPIT-110", details={
        'Course Name': 'Programming and Problem Solving',
        'Department': 'IT'
    })

    # link courses to IT department
    gf.addEdge(university, "IT", "CPIT-221", "Offers")
    gf.addEdge(university, "IT", "CPIT-201", "Offers")
    gf.addEdge(university, "IT", "CPIT-110", "Offers")

    # add courses to FCIT-IS
    gf.addNode(university, "CPIS-334", details={
        'Course Name': 'Introduction to Software Project Management',
        'Department': 'IS'
    })
    gf.addNode(university, "CPIS-428", details={
        'Course Name': 'Professional Computing Issues',
        'Department': 'IS'
    })
    gf.addNode(university, "CPIS-210", details={
        'Course Name': 'Computer Architecture and Organization',
        'Department': 'IS'
    })

    # link courses to IS department
    gf.addEdge(university, "IS", "CPIS-334", "Offers")
    gf.addEdge(university, "IS", "CPIS-428", "Offers")
    gf.addEdge(university, "IS", "CPIS-210", "Offers")

    # add courses to SCIENCES-Physics
    gf.addNode(university, "PHYS-110", details={
        'Course Name': 'General Physics I',
        'Department': 'Physics'
    })
    gf.addNode(university, "PHYS-202", details={
        'Course Name': 'General Physics II',
        'Department': 'Physics'
    })
    gf.addNode(university, "PHYS-203", details={
        'Course Name': 'General Physics III',
        'Department': 'Physics'
    })

    # link courses to Physics department
    gf.addEdge(university, "Physics", "PHYS-110", "Offers")
    gf.addEdge(university, "Physics", "PHYS-202", "Offers")
    gf.addEdge(university, "Physics", "PHYS-203", "Offers")


    # add courses to SCIENCES-Chemistry
    gf.addNode(university, "CHEM-110", details={
        'Course Name': 'General Chemistry I',
        'Department': 'Chemistry'
    })
    gf.addNode(university, "CHEM-202", details={
        'Course Name': 'General Chemistry II',
        'Department': 'Chemistry'
    })
    gf.addNode(university, "CHEM-203", details={
        'Course Name': 'Introduction to Natural Sciences',
        'Department': 'Chemistry'
    })

    # link courses to Chemistry department
    gf.addEdge(university, "Chemistry", "CHEM-110", "Offers")
    gf.addEdge(university, "Chemistry", "CHEM-202", "Offers")
    gf.addEdge(university, "Chemistry", "CHEM-203", "Offers")


    # add courses to SCIENCES-Math
    gf.addNode(university, "MATH-110", details={
        'Course Name': 'Calculus I',
        'Department': 'Math'
    })
    gf.addNode(university, "MATH-202", details={
        'Course Name': 'Calculus II',
        'Department': 'Math'
    })
    gf.addNode(university, "MATH-203", details={
        'Course Name': 'Calculus III',
        'Department': 'Math'
    })

    # link courses to Math department
    gf.addEdge(university, "Math", "MATH-110", "Offers")
    gf.addEdge(university, "Math", "MATH-202", "Offers")
    gf.addEdge(university, "Math", "MATH-203", "Offers")


    # add courses to ENG-Mechanical Engineering
    gf.addNode(university, "MENG-270", details={
        'Course Name': 'Mechanics of Materials',
        'Department': 'Mechanical ENG'
    })
    gf.addNode(university, "MENG-364", details={
        'Course Name': 'Machine Dynamics',
        'Department': 'Mechanical ENG'
    })
    gf.addNode(university, "MENG-408", details={
        'Course Name': 'Reverse Engineering',
        'Department': 'Mechanical ENG'
    })

    # link courses to Mechanical ENG department
    gf.addEdge(university, "Mechanical ENG", "MENG-270", "Offers")
    gf.addEdge(university, "Mechanical ENG", "MENG-364", "Offers")
    gf.addEdge(university, "Mechanical ENG", "MENG-408", "Offers")


    # add courses to ENG-Computer Engineering
    gf.addNode(university, "EE-202", details={
        'Course Name': 'Object-Oriented Computer Programming',
        'Department': 'Computer ENG'
    })
    gf.addNode(university, "EE-250", details={
        'Course Name': 'Basic Electrical Circuits',
        'Department': 'Computer ENG'
    })
    gf.addNode(university, "EE-331", details={
        'Course Name': 'Principles of Automatic Control',
        'Department': 'Computer ENG'
    })

    # link courses to Computer ENG department
    gf.addEdge(university, "Computer ENG", "EE-202", "Offers")
    gf.addEdge(university, "Computer ENG", "EE-250", "Offers")
    gf.addEdge(university, "Computer ENG", "EE-331", "Offers")


    # add courses to ENG-Industrial Engineering
    gf.addNode(university, "IE-255", details={
        'Course Name': 'Engineering Economy',
        'Department': 'Industrial ENG'
    })
    gf.addNode(university, "IE-311", details={
        'Course Name': 'Operations Research I',
        'Department': 'Industrial ENG'
    })
    gf.addNode(university, "IE-331", details={
        'Course Name': 'Probability and Engineering Statistics',
        'Department': 'Industrial ENG'
    })

    # link courses to Computer ENG department
    gf.addEdge(university, "Industrial ENG", "IE-255", "Offers")
    gf.addEdge(university, "Industrial ENG", "IE-311", "Offers")
    gf.addEdge(university, "Industrial ENG", "IE-331", "Offers")

    # create student nodes 
    gf.addNode(university, "Khalid", details={
        'studentID': 1,
        'major': 'Math'
    })
    gf.addNode(university, "Mohammad", details={
        'studentID': 2,
        'major': 'IT'
    })
    gf.addNode(university, "Ahmad", details={
        'studentID': 3,
        'major': 'IS'
    })
    gf.addNode(university, "Nawaf", details={
        'studentID': 4,
        'major': 'CS'
    })

    # link students with departments
    gf.addEdge(university, "Khalid", "Math", "Majors_in")
    gf.addEdge(university, "Mohammad", "IT", "Majors_in")
    gf.addEdge(university, "Ahmad", "IS", "Majors_in")
    gf.addEdge(university, "Nawaf", "CS", "Majors_in")
    
    # link students with courses
    gf.addEdge(university, "Khalid", "MATH-203", "enrolled_in")

    gf.addEdge(university, "Mohammad", "CPIT-221", "enrolled_in")
    gf.addEdge(university, "Mohammad", "CPIT-201", "enrolled_in")

    gf.addEdge(university, "Ahmad", "CPIS-334", "enrolled_in")
    gf.addEdge(university, "Ahmad", "CPIS-210", "enrolled_in")

    gf.addEdge(university, "Nawaf", "CPCS-203", "enrolled_in")
    gf.addEdge(university, "Nawaf", "CPCS-331", "enrolled_in")
    
    return university