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

# 3重ループが存在しており,O(V^3)
# 全点対最短経路問題では、ダイクストラ法を連続して⽤いるよりワーシャル・フロイド法に利がある場合がある

def WarshallFloyd(N,S,edges):
    inf = 10**9
    dist = [[inf for i in range(N)] for j in range(N)]
    for i in range(N):
        dist[i][i] = 0
    for i in range(len(edges)):# 隣接行列で初期化
        for node in edges[i]:
            dist[i][node[0]] = node[1]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
                            
    print(' '.join(map(str, dist[S])))
    #print(dist)

WarshallFloyd(N,S,edges)