import sys
import heapq

#edges=[[]for i in range(N)]
#edges[a].append([b,d])
edges = [[[1, 5], [2, 4]], #ノードA0
[[0, 5], [3, 3], [5, 9]], #ノードB1
[[0, 4], [3, 2], [4, 3]], #ノードC2
[[1, 3], [2, 2], [5, 1], [6, 7]], #ノードD3
[[2, 3], [6, 8]], #ノードE4
[[1, 9], [3, 1], [6, 2], [7, 5]], #ノードF5
[[3, 7], [4, 8], [5, 2], [7, 2]], #ノードG6
[[5, 5], [6, 2]]] #ノードH7

N=len(edges)
S=0

def dijkstra(N,S,edges):
    done=[False]*N
    inf=10**9
    dist=[inf]*N
    dist[S]=0
    heap=[]
    heapq.heappush(heap,[dist[S],S])
    while heap:
        node=heapq.heappop(heap)[1]
        if not done[node]:
            for e in edges[node]:
                if dist[e[0]]>dist[node]+e[1]:
                    dist[e[0]]=dist[node]+e[1]
                    heapq.heappush(heap,[dist[e[0]],e[0]])
        done[node]=True

    for i in range(N):
        if dist[i]==inf:
            dist[i]='INF'
    
    print(' '.join(map(str, dist)))

dijkstra(N,S,edges)