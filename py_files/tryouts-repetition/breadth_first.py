my_graph={
    'A':['B','C'],
    'B':['D'],
    'C':['E'],
    'D':['F'],
    'E':[],
    'F':[]
    }   

def breadth_first(graph, src):
    queue=[src]
    
    while queue:
        current = queue.pop(0)
        print(current)
        queue = queue + graph[current]


breadth_first(my_graph,'A')