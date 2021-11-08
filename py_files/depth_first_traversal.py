def depth_first_print(graph,source):
    '''
    prints nodes from given graph starting at source node in depth first manner
    :param graph: dictionary (adjacency list)
    :param source: string (key of graph dictionary)
    '''

    node_stack=[source]

    while node_stack:
        next_node=node_stack.pop()

        print(next_node)
        for adjacent_node in graph[next_node]:
            node_stack.append(adjacent_node)


def depth_first_print_recursive(graph,source):
    '''
    prints recursively nodes from given graph starting at source node in depth first manner
    :param graph: dictionary (adjacency list)
    :param source: string (key of graph dictionary)
    '''
    print(source)
    adjacents=graph[source]

    for adjacent in adjacents:
        depth_first_print_recursive(graph,adjacent)

my_graph={
    'A':['B','C'],
    'B':['D'],
    'C':['E'],
    'D':['F'],
    'E':[],
    'F':[]
    }   


depth_first_print(my_graph,'A')
depth_first_print_recursive(my_graph,'A')