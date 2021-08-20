# 全域⽊（spanning tree）グラフにおいて，すべての頂点がつながっている⽊（閉路を持たない連結グラフ）
# 最⼩全域⽊（minimum spanning tree）全域⽊の中で辺の距離（コスト）の総和が最⼩になるもの

# 各ノードからの行き先、距離
edges = [[[1, 5], [2, 4]], #ノードA0
[[0, 5], [3, 3], [5, 9]], #ノードB1
[[0, 4], [3, 2], [4, 3]], #ノードC2
[[1, 3], [2, 2], [6, 7], [7, 5]], #ノードD3
[[2, 3], [6, 8]], #ノードE4
[[1, 9]], #ノードF5
[[3, 7], [4, 8], [7, 1]], #ノードG6
[[3, 5], [6, 1]]] #ノードH7

N=len(edges)
edges2 = [] # from,to,distance
for i in range(len(edges)):
    for node in edges[i]:
        edges2.append([i,node[0],node[1]])

# 辺ベースのアプローチ：クラスカル法
# 存在する辺を距離の短い順に並べて順に⼊れていき，閉路が出来ないことが確認できた場合は追加し，全部の辺をチェックしたら終了．
# 隣接リストの場合，辺の数をEとして，辺のソートにE log Eかかる
# 各辺を⼊れるかどうかの判断はUnion-Find⽊を使うとα(V)となり，これをE回やるので，E α(V)
# よって，アルゴリズム全体ではO(E log E)
import sys

class UnionFind: #UF木の実装
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.height = [0 for i in range(n)] # 各⽊の⾼さ

    def get_root(self, i):
        if self.parent[i] == i: # ⾃分が根ノードの場合
            return i
        else: # 経路圧縮しながら根ノードを探す
            self.parent[i] = self.get_root(self.parent[i])
            return self.parent[i]
    
    def unite(self, i, j):
        ri = self.get_root(i)
        rj = self.get_root(j)
        if ri != rj: # より⾼い⽅にマージ
            if self.height[ri] < self.height[rj]:
                self.parent[ri] = rj
            else:
                self.parent[rj] = ri
                if self.height[ri] == self.height[rj]:
                    self.height[ri] += 1
    
    def is_in_group(self, i, j):
        if self.get_root(i) == self.get_root(j):
            return True
        else:
            return False

def Kruskal(V, edges): #クラスカル法の実装
    e_sorted = [] # 距離で整列された辺
    for e in edges:
        e_sorted.append([e[2], e[0], e[1]]) # ソートのために先頭の要素を距離にする
    e_sorted.sort()
    uf_tree = UnionFind(V) # Union-Find⽊を使う
    mst = [] # 最⼩全域⽊の辺を保持するリスト
    min_d = 0
    for e in e_sorted:
        if uf_tree.is_in_group(e[1], e[2]) == False:
            uf_tree.unite(e[1], e[2]) # e[1]，e[2]を同じグループにする
            mst.append([e[1], e[2]]) # 最⼩全域⽊に追加
            min_d += e[0]

    #print(min_d)
    print(mst)
    
Kruskal(N, edges2)


