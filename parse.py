def parseFile(fileName):
    f = open(fileName,'r')
    graph = {}
    nodes = []
    maxW = float(0)
    for line in f:
        split = line.split(" ")
        w = int(split[3][8:-2])
        if w>maxW:
            maxW = float(w)
    f = open(fileName,'r')
    for line in f:
        split = line.split(" ")
        node1 = int(split[0])
        node2 = int(split[2])
        if node1 not in nodes:
            nodes.append(node1)
        if node2 not in nodes:
            nodes.append(node2)
        w = int(split[3][8:-2])/maxW
        graph = addToGraph(graph,node1,node2,w)
    nodes.sort()
    return (nodes,graph)

def addToGraph(graph,v1,v2,w):
    if v1 not in graph.keys():
        graph[v1] = {}
    if v2 not in graph.keys():
        graph[v2] = {}
    try:
        w2 = graph[v2][v1]
        avg = (w + w2)/2.0
        w = avg
    except:
        avg = 0
    graph[v1][v2] = w
    graph[v2][v1] = w
    return graph
