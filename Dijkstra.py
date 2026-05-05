def Dijkstra_TAS(G, src, dest):
    dst = [infty] * G.order
    dst[src] = 0
    P = [None] * G.order
    P[src] = -1
    H = Heap(G.order)
    H.push(src, 0)

    while not H.isempty():
        (x, _) = H.pop()
        if x == dest:
            return(dst, P)
    
        for y in G.adjlists[x]:
            if dst[x] + G.costs[(x, y)] < dst[y]:
                dst[y] = dst[x] + G.costs[(x, y)]
                if P[y] == None:
                    H.push(y, dst[y])
                else:
                    H.update(y, dst[y])
                P[y] = x
    return (dst, P)


