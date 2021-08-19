from collections import deque

V = 5
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 4], [3, 4]]

# ⼊⼒されたグラフがDAGである場合，全てのノードと辺は⾼々1回しかチェックされない O(V+E)

def topoSortDFS(V, edges):
    def check(v):
        if visited[v] == 1:
            raise Exception("not DAG") #[DAGになっていないので，エラーを返す]
        elif visited[v] == 0:
            visited[v] = 1 # 処理待ちにする
            for to_v in edges2[v]:
                check(to_v) # 再帰で呼び出す
            visited[v] = 2 # 処理済にする
            sorted_g.appendleft(v) # ソート済の先頭に追加

    # ノードをすでに⾒たかどうかを格納する配列
    # 0：未訪問，1：処理待ち，2：処理済
    visited = [0]*V
    edges2 = [[] for i in range(V)] #各頂点からつながる頂点のリストに変換
    for e in edges:
        edges2[e[0]].append(e[1])

    sorted_g = deque()
    # 全てのノードをチェックする
    for i in range(V):
        check(i)

    print(' '.join(map(str, sorted_g)))

topoSortDFS(V, edges)


# ist2018 3(4)
from collections import deque

def topoSortDFS2(V, edges):
    def dfs(u):
        visited[u] = True
        for v in edges2[u]:
            if visited[v] != True:
                dfs(v)
        s.appendleft(u)

    edges2 = [[] for i in range(V)] #各頂点からつながる頂点のリストに変換
    for e in edges:
        edges2[e[0]].append(e[1])

    visited = [False]*V # ノードをすでに⾒たかどうかを格納する配列
    s = deque()

    for v in range(V):
        if visited[v] != True:
            dfs(v)

    print(' '.join(map(str, s)))

topoSortDFS2(V, edges)
