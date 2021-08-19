import sys
import heapq

#edges = [[]for i in range(N)]
#edges[a].append([b,d])
# 各ノードからの行き先、距離
edges = [[[1, 5], [2, 4]], #ノードA0
[[0, 5], [3, 3], [5, 9]], #ノードB1
[[0, 4], [3, 2], [4, 3]], #ノードC2
[[1, 3], [2, 2], [5, 1], [6, 7]], #ノードD3
[[2, 3], [6, 8]], #ノードE4
[[1, 9], [3, 1], [6, 2], [7, 5]], #ノードF5
[[3, 7], [4, 8], [5, 2], [7, 2]], #ノードG6
[[5, 5], [6, 2]]] #ノードH7

N = len(edges)
S = 0
# ヒープを使うダイクストラ
# ヒープから最短距離を持つ未確定のノードを取り出す 最短経路⻑が更新された頂点をヒープに追加する.
# 頂点V、辺の数Eとしてヒープの更新logEをE回これがそれぞれ追加、取り出しより、O(E logE)
# 重複するノードをヒープに追加せず直接更新出来る場合、ヒープの更新logVをそれぞれ追加E回、取り出しV回よりO((E+V)logV)

def Dijkstra(N,S,edges):
    done = [False]*N
    inf = 10**9
    dist = [inf]*N
    dist[S] = 0
    heap = []
    heapq.heappush(heap,[dist[S],S])
    while heap:
        node=heapq.heappop(heap)[1]
        if not done[node]:
            for e in edges[node]:
                if dist[e[0]] > dist[node]+e[1]:
                    dist[e[0]] = dist[node]+e[1]
                    heapq.heappush(heap,[dist[e[0]],e[0]])
        done[node] = True

    for i in range(N):
        if dist[i] == inf:
            dist[i] = 'INF'
    
    print(' '.join(map(str, dist)))

Dijkstra(N,S,edges)