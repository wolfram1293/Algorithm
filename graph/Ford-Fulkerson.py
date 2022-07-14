# 最大流(max flow)問題
# フォード・ファルカーソン法
# ノード数V，最⼤流の最適値をF 最悪の場合，新しい経路が⾒つかっても最⼤流が1つしか増やせない-> F回の最⼤流値の更新が発⽣
# 経路探索のためには⾼々Vのノードを訪れる．隣接⾏列の場合，辺のチェックのために，毎回O(V)個の操作が必要
# 隣接⾏列の場合 O(FV^2)
def FordFulkerson(edges,start,end):
    # s ‒ e間においてある1つのパスで流せる流量を返す
    def dfs_ff(s, e, flow): # 引数: DFSの開始ノード，DFSの終了ノード，DFSの開始ノードの前のノードまでに流せる最⼤流量
        if (s == e): return flow # sとeが⼀緒のノードなら今までの最⼤流量をそのまま返す
        visited[s] = True # ノードsを訪問したと記録
        for i in range(len(edges[s])):# 流せる容量がある辺をすべてチェック
            if edges[s][i] > 0 and not visited[i]: # まだ⾒ていない辺があればDFS
                f = dfs_ff(i, e, min(flow, edges[s][i])) # 今までの最⼤流量とノードs‒i間の流量のうち，⼩さい⽅を使ってdfs_ffを再帰で呼び出す
                if f > 0:
                    edges[s][i] -= f
                    edges[i][s] += f
                    return f
        return 0
    
    N = len(edges)
    max_flow = 0
    while True:
        visited = [False] * N # 毎回のDFSで使う訪問フラグ
        f = dfs_ff(start,end,10**9) # DFS実⾏
        if f == 0: break # もう流せないなら終了
        max_flow += f
    return max_flow

edges = [[0, 10, 10, 0, 0, 0],
[0, 0, 0, 4, 8, 0],
[0, 0, 0, 7, 4, 0],
[0, 0, 0, 0, 0, 8],
[0, 0, 0, 0, 0, 12],
[0, 0, 0, 0, 0, 0]]
FordFulkerson(edges,0,5)

# 隣接リストでの実装 O(FE)
def FordFulkerson2(edges,start,end):
    # s ‒ e間においてある1つのパスで流せる流量を返す
    def dfs_ff(s, e, flow): # 引数: DFSの開始ノード，DFSの終了ノード，DFSの開始ノードの前のノードまでに流せる最⼤流量
        if (s == e): return flow # sとeが⼀緒のノードなら今までの最⼤流量をそのまま返す
        visited[s] = True # ノードsを訪問したと記録
        for i in range(len(edges[s])):# 流せる容量がある辺をすべてチェック
            edge = edges[s][i] # edge[0] = to, edge[1] = s-toに流せる最大量
            if edge[1] > 0 and not visited[edge[0]]: # まだ⾒ていない辺があればDFS
                f = dfs_ff(edge[0], e, min(flow, edge[1])) # 今までの最⼤流量とノードs‒to間の流量のうち，⼩さい⽅を使ってdfs_ffを再帰で呼び出す
                if f > 0:
                    edge[1] -= f
                    for j in range(len(edges[edge[0]])): # 逆辺のフロー更新(効率化したい)
                        if edges[edge[0]][j][0] == s:
                            edges[edge[0]][j][1] += f
                    return f
        return 0
    
    N = len(edges)
    max_flow = 0
    while True:
        visited = [False] * N # 毎回のDFSで使う訪問フラグ
        f = dfs_ff(start,end,10**9) # DFS実⾏
        if f == 0: break # もう流せないなら終了
        max_flow += f
    return max_flow

edges = [[0, 10, 10, 0, 0, 0],
[0, 0, 0, 4, 8, 0],
[0, 0, 0, 7, 4, 0],
[0, 0, 0, 0, 0, 8],
[0, 0, 0, 0, 0, 12],
[0, 0, 0, 0, 0, 0]]
edges2 = [[] for i in range(len(edges))]
for i in range(len(edges)):
    for j in range(len(edges)):
        if edges[i][j] != 0:
            edges2[i].append([j,edges[i][j]])
            edges2[j].append([i,0])

FordFulkerson2(edges2,0,5)
