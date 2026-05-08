def Kruskal(G):
    edgeList = []
    for x in range(G.order):
        for y in G.adjlists[x]:
            if x > y:
                edgeList.append((G.costs[(x, y)], x, y))
    edgeList.sIort(reverse = True)
    
    P = [-1] * G.order
    T = graph.Graph(G.order, directed=False, costs=True)
    n = 0
    while n < G.order - 1 and edgeList != []:
        (c, x, y) = edgeList.pop()
        if union2(x, y, P):
            T.addedge(x, y, c)
            n += 1

    if n < G.order - 1:
        raise Exception ("Not connected")
    return T

