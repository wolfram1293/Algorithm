V = 5
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 4], [3, 4]] #頂点from toのリスト

# Khanのアルゴリズム
from collections import deque

# ⼊⼒されたグラフがDAGである場合，全てのノードと辺は⾼々1回しかチェックされない O(V+E)
def topoSortKhan(V,edges):
    E = len(edges)
    indeg = [0]*V # ⼊次数を格納する配列
    outedge = [[] for _ in range (V)] # 出⼒辺を保持する配列
    for e in edges: # ⼊次数と出⼒辺の情報を整理する
        indeg[e[1]] += 1
        outedge[e[0]].append(e[1])

    sorted_g = list(v for v in range(V) if indeg[v]==0) # ソート済のノードを格納する配列 最初に⼊次数0のものを⼊れておく
    deq = deque(sorted_g) # ⼊次数0のノードを処理するためのdeque

    while deq: # ⼊次数0のノードがある限り繰り返す
        v = deq.popleft() # deq.pop()でもよい
        for u in outedge[v]: # vからつながるすべてのノードu
            E -= 1
            indeg[u] -= 1 # E,uの⼊次数を1減らす
            if indeg[u] == 0: # uの⼊次数が0
                deq.append(u) # uをdeqとsorted_gに⼊れる
                sorted_g.append(u)
    if E != 0:
        raise Exception("not DAG") # DAGになっていないので，エラーを返す
    print(' '.join(map(str, sorted_g)))

topoSortKhan(V, edges)


# ist2018 3(6)ans
# Sへのpushタイミング、ループ検出なし以外はKhanと同じ

from collections import deque

# 辺を参照する回数は, degreeの前計算の際にE回と操作1~2(while)の際にE回で合わせて2E回. 
# Qへのpush・popの回数とSへのpushの回数はそれぞれV回なので,計算量はO(E+V).
def topoSortBFS(V, edges):
    degree = [0]*V
    Q = deque() # キューとする
    S = []
    for e in edges:
        degree[e[1]] += 1 # すべての頂点について,degreeで入ってくる辺の本数を数える
    for i in range(V): # 0ならQにpush
        if degree[i] == 0:
            Q.append(i)
    
    edges2 = [[] for i in range(V)] # 各頂点からつながる頂点のリストに変換
    for e in edges:
        edges2[e[0]].append(e[1])

    while Q: # Qが空になるまで
        u = Q.popleft() # キューQからpop、Sにpush
        S.append(u)
        for v in edges2[u]: # uから出ているすべての辺について, degree[v]を1減らす.このとき0となった場合は,頂点vをQにpush
            degree[v] -= 1
            if degree[v] == 0:
                Q.append(v)

    print(' '.join(map(str, S)))

topoSortBFS(V, edges)
