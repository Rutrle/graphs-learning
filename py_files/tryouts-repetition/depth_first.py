my_graph={
    'A':['B','C'],
    'B':['D'],
    'C':['E'],
    'D':['F'],
    'E':[],
    'F':['V'],
    'V':['N','M'],
    'N':[],
    'M':[],
    }   

def depth_first(graph, src):
    stack=[src]

    while stack:
        current=stack.pop()
        print(current)
        stack = stack + graph[current]

def rec_depth_first(graph,src):
    print(src)
    for node in graph[src]:
        rec_depth_first(graph,node)

def has_path(graph, src, dst):
    if src == dst:
        return True
    for node in graph[src]:
        if has_path(graph, node, dst):
            return True
    
    return False

depth_first(my_graph,'A')
print('-'*160)
rec_depth_first(my_graph,'A')

print(has_path(my_graph,'A','M'))
print(has_path(my_graph,'M','N'))