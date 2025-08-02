import heapq
from typing import List, Tuple

def dijkstra(n: int, edges: List[List[Tuple[int,int]]], s: int) -> Tuple[List[int], List[int]]:
    INF = 10**18
    dist = [INF]*n
    parent = [-1]*n
    dist[s] = 0
    pq: List[Tuple[int,int]] = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in edges[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))
    return dist, parent

def reconstruct(parent: List[int], t: int) -> List[int]:
    path = []
    while t != -1:
        path.append(t)
        t = parent[t]
    return list(reversed(path))

if __name__ == "__main__":
    n = 5
    edges = [[] for _ in range(n)]
    def add(u,v,w):
        edges[u].append((v,w))
        edges[v].append((u,w))
    add(0,1,4); add(0,2,1); add(2,1,2); add(1,3,1); add(2,3,5); add(3,4,3)
    dist, parent = dijkstra(n, edges, 0)
    print(dist)
    print(reconstruct(parent, 4))
