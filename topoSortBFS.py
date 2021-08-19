# ist2018 3(6)ans

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

V = 5
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 4], [3, 4]] #頂点from toのリスト

topoSortBFS(V, edges)