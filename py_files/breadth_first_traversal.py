
def breadth_first_print(graph,source):
    '''
    prints nodes from given graph starting at source node in breadth first manner
    :param graph: dictionary (adjacency list)
    :param source: string (key of graph dictionary)
    '''

    node_queue=[source]

    while node_queue:
        next_node=node_queue.pop(0)

        print(next_node)
        for adjacent_node in graph[next_node]:
            node_queue.append(adjacent_node)

my_graph={
    'A':['B','C','G'],
    'B':['D'],
    'C':['E'],
    'D':['F'],
    'E':[],
    'F':[],
    'G':[]
    }   

breadth_first_print(my_graph,'A')