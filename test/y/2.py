import sys

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if -self.parent[y] > -self.parent[x]:
            x, y = y, x

        self.parent[x] += self.parent[y]
        self.parent[y] = x
    
    def find(self, x): # 要素xが属するグループの根を返す
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.find(self.parent[x]) # 経路圧縮 根を調べる際に、調べた要素の親を根に変更しつなぎ直す
            return self.parent[x]

    def size(self, x): # 要素xが属するグループの要素数
        return -self.parent[self.find(x)]

    def same(self, x, y): # 同じグループに属するかどうかを返す
        return self.find(x) == self.find(y)

    def members(self, x): # 要素xが属するグループに属する要素をリストで返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self): # すべての根の要素をリストで返す
        return [i for i, x in enumerate(self.parent) if x < 0]

    def group_count(self): # グループの数を返す
        return len(self.roots())

n, m, k = map(int, input().split())
c = list(map(int, input().split()))

uf = UnionFind(n)
for i in range(m):
    u, v = map(int, input().split())
    uf.unite(u-1,v-1)

prevc = c

for i in range(1,k+1):
    roots = uf.roots()
    for v in roots:
        cntc = {}
        for v2 in uf.members(v):
            if prevc[v2] not in cntc:
                cntc[prevc[v2]] = 1
            else:
                cntc[prevc[v2]] += 1
        maxc = [max(cntc)]
        maxc2 = min(maxc)
        for v2 in uf.members(v):
            c[v2] = maxc2

    prevc = c

for ci in c:
    print(ci)

# fixed
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if -self.parent[y] > -self.parent[x]:
            x, y = y, x

        self.parent[x] += self.parent[y]
        self.parent[y] = x
    
    def find(self, x): # 要素xが属するグループの根を返す
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.find(self.parent[x]) # 経路圧縮 根を調べる際に、調べた要素の親を根に変更しつなぎ直す
            return self.parent[x]

    def size(self, x): # 要素xが属するグループの要素数
        return -self.parent[self.find(x)]

    def same(self, x, y): # 同じグループに属するかどうかを返す
        return self.find(x) == self.find(y)

    def members(self, x): # 要素xが属するグループに属する要素をリストで返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self): # すべての根の要素をリストで返す
        return [i for i, x in enumerate(self.parent) if x < 0]

    def group_count(self): # グループの数を返す
        return len(self.roots())

n, m, k = 3,1,2
c = [1,2,3]

uf = UnionFind(n)
for i in range(m):
    u, v = 2,3
    uf.unite(u-1,v-1)

for i in range(1,k+1):
    prevc = c
    roots = uf.roots()
    for v in roots:
        cntc = {}
        for v2 in uf.members(v):
            if prevc[v2] not in cntc:
                cntc[prevc[v2]] = 1
            else:
                cntc[prevc[v2]] += 1
        maxc = [v[0] for v in cntc.items() if v[1] == max(cntc.values())]
        maxc2 = min(maxc)
        for v2 in uf.members(v):
            c[v2] = maxc2

for ci in c:
    print(ci)

'''
UnionFind木を用いた実装
prevcはcのバックアップ
cntcはつながっているノードの各色の数をカウントする辞書
maxcは色の数が最大となるノードのリスト
maxc2は色の数が最大となるノードのリストのうち色番号の最小値を出力する

バグがあり、テストケースに正解できなかったが、
maxc = [v[0] for v in cntc.items() if v[1] == max(cntc.values())]
とすれば意図していた動作はすると考えられる。

しかし、この題意の理解だと一度色が変わったら次は変わらないと思われ、題意の理解を間違えたと考えている。
'''

'''
最初はナイーブに１日ずつカウントを進めていき、７のつく日とそれ以外で分け、ポイントを足していく方針で実装した。
計算量は７のつく日の判定はO(日付の桁数)より、高々O(log(ｎ))、日を進めていくカウントはO(かかる日数)より、高々O(ｎ)、よって全体では高々O(ｎ log(ｎ))である。

しかし、これで実行制限時間に引っかかったため、高速化を考えた。
次に7がつく日付の判定をO(1)とし、全体の計算量O(n)としたが、実行時間が足りなかったため、それ以上の高速化を考えた。

かかる日数は高々int(n/a)より、その中の7がつく日の数をカウントして、かかる日数をそれから逆算的に引いていく方法を実装しようとしたが実装が間に合わなかった。
'''
