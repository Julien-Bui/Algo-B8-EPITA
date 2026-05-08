def Prim(G, x=0):
    T = graph.Graph(G.order, False, costs = True)
    costs = [infty] * G.order
    costs[x] = 0
    p = [None] * G.order
    inSol = [False] * G.order
    H = heap.Heap(G.order)
    inSol[x] = True
    
    for _ in range(G.order - 1):
        for y in G.adjlists[x]:
            if not inSol[y] and G.costs[(x, y)] < costs[y]:
                costs[y] = G.costs[(x, y)]
                if p[y] == None:
                    H.push(y, costs[y])
                else:
                    H.update(y, costs[y])
                p[y] = x
        if H.is_empty():
            raise Exception ("Not connected")
        (_, x) = H.pop()  
        inSol[x] = True
        T.addedge(x, p[x], costs[x])        
        
    return T

