def BellManFord(G, src):
    dist = [infty] * G.order
    dist[src] = 0
    P = [None] * G.order
    P[src] = -1
    i = 1
    change = True

    while i <= G.order and change:
        change = False
        for x in range(G.order):
            if dist[x] != infty:
                for y in G.adjlists[x]:
                    if dist[x] + G.costs[(x, y)] < dist[y]:
                        dist[y] = dist[x] + G.costs[(x, y)]
                        P[y] = x
                        change = True
        i += 1

    return (change, dist, P)
