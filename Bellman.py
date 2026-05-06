def _tri_topo(G,x, sommet, L):
    sommet[x] = True
    for y in G.adjlists[x]:
        if not sommet[y]:
            _tri_topo(G, y,sommet, L)
    L.append(x)

def tri_topo(G):
    sommet = [False] * G.order
    L = []
    for i in range(G.order):
        if not sommet[i]:
            _tri_topo(G, i , sommet, L)

    return L

def Bellman(G, src, dest = None):
    dist = [infty] * G.order
    dist[src] = 0
    P = [None] * G.order
    P[src] = -1
    order = tri_topo(G)

    while order:
        x = order.pop()
        if x == dest:
            return (dist, P)
        for y in G.adjlists[x]:
            if dist[x] + G.costs[(x, y)] < dist[y]:
                dist[y] = dist[x] + G.costs[(x, y)]
                P[y] = x

    return (dist, P)

