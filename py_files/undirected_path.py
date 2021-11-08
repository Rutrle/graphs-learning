edges = [['I','J'],
        ['K','I'],
        ['M','K'],
        ['K','L'],
        ['O','N']
        ]


def build_graph(edges):
    graph={}
    for edge in edges:
        [a,b]=edge
        if a not in graph:
            graph[a]=[]

        if b not in graph:
            graph[b]=[]
        
        graph[a].append(b)
        graph[b].append(a)

    return graph


def has_path(graph, src, dst, visited=set()):
    print(f'visited: {visited}')
    if src in visited:
        return False
        
    print('src: ',src)
    if src == dst:
        return True

    visited.add(src)
    for adjacent in graph[src]:
        if has_path(graph, adjacent, dst,visited):
            return True

    return False



graph=build_graph(edges)

k=has_path(graph,'I','N')
print(60*'-')
l=has_path(graph,'I','K')

print(k,l)