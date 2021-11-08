graph = {
    'F':['G','I'],
    'G':['H'],
    'H':[],
    'I':['G','K'],
    'J':['I'],
    'K':[]
}

def depth_first_has_path(graph,src,dst):
    if src ==dst:
        return True
    else:
        for adjacent_node in graph[src]:
            if depth_first_has_path(graph,adjacent_node,dst):
                return True
        
        return False
    
def breadth_first_has_path(graph,src,dst):

    node_queue = [src]
    while node_queue:
        current=node_queue.pop(0)
        if current == dst:
            return True
        for adjacent in graph[current]:
            node_queue.append(adjacent)
    return False



print(depth_first_has_path(graph,'F','K'))

print(depth_first_has_path(graph,'F','J'))

print(breadth_first_has_path(graph,'F','K'))
print(breadth_first_has_path(graph,'F','J'))