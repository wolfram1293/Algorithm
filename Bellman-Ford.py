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
S=0
edges2 = []
for i in range(len(edges)):
    for node in edges[i]:
        edges2.append([i,node[0],node[1]])

# 始点，終点，距離の順．
'''
edges2 = [[0, 1, 5], [0, 2, 4], [1, 0, 5], [1, 3, 9], [1, 5, 9],
[2, 0, 4], [2, 3, 2], [2, 4, 3], [3, 1, 9], [3, 2, 2], [3, 5, 1],
[3, 6, 7], [4, 2, 3], [4, 6, 8], [5, 1, 9], [5, 3, 1], [5, 6, 2],
[5, 7, 5], [6, 3, 7], [6, 4, 8], [6, 5, 2], [6, 7, 2], [7, 5, 5],
[7, 6, 2]]
'''

# ダイクストラと違い,最短距離の選択を⾏わず更新毎に全ての辺に対しての計算を毎回⾏う
# 負の経路があっても計算可能,負の閉路があってもそれを検知可能
# 頂点V、辺の数Eとして,2重ループの1つ⽬はV，2つ⽬は毎回すべての辺をチェックするのでEよって全体ではO(VE)

def BellmanFord(N,S,edges):
    inf=10**9
    dist = [inf]*N
    dist[S] = 0
    # whileではなく，|N|回のforループにする．
    # 辺の情報をすべて見ることを1ループとすると1ループするたびに最低でも1つの頂点についての最短距離は求まる
    # 頂点の数をNとするとN−1回のループでグラフ全体の最短距離が求まる
    # もしi=N-1で更新があれば，それは負の閉路の存在を表す．
    for i in range(N):
        for e in edges:
            if dist[e[1]] > e[2] + dist[e[0]]:
                dist[e[1]] = e[2] + dist[e[0]]
                # 負の閉路の検知
                if i==N-1: return -1
    print(' '.join(map(str, dist)))

BellmanFord(N,S,edges2)