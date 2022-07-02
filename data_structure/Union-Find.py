# Algo2021 11 UF rankを保持、より⾼い⽅にマージ
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

# 根の親の値にサイズの情報を持たせる 要素が根（ルート）の場合は-(そのグループの要素数)を格納する (根の親の値にランク（木の高さ）の情報を保持してもいい)
# 汎用バージョン 参考 https://note.nkmk.me/python-union-find/

class UnionFind():
    def __init__(self, n):
        self.parent = [-1] * n
        self.n = n

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


# 文字列やタプル((0, 0), )などを要素とする場合
# 文字列と番号のペアの辞書を用意
l = ['A', 'B', 'C', 'D', 'E']

d = {x: i for i, x in enumerate(l)}
print(d)
# {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}

d_inv = {i: x for i, x in enumerate(l)}
print(d_inv)
# {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E'}

uf_s = UnionFind(len(l))
print(uf_s)
# 0: [0]
# 1: [1]
# 2: [2]
# 3: [3]
# 4: [4]

uf_s.union(d['A'], d['D'])
uf_s.union(d['D'], d['C'])
uf_s.union(d['E'], d['B'])
print(uf_s)
# 0: [0, 2, 3]
# 4: [1, 4]

print(d_inv[uf_s.find(d['D'])])
# A

print(uf_s.size(d['D']))
# 3

print(uf_s.same(d['A'], d['D']))
# True

print([d_inv[i] for i in uf_s.members(d['D'])])
# ['A', 'C', 'D']

print([d_inv[i] for i in uf_s.roots()])
# ['A', 'E']

print(uf_s.group_count())
# 2


# 元のクラスを継承したクラス。__init__()で2つの辞書を生成して入出力時に使う。
class UnionFindLabel(UnionFind):
    def __init__(self, labels):
        assert len(labels) == len(set(labels))

        self.n = len(labels)
        self.parent = [-1] * self.n
        self.d = {x: i for i, x in enumerate(labels)}
        self.d_inv = {i: x for i, x in enumerate(labels)}

    def find_label(self, x):
        return self.d_inv[super().find(self.d[x])]

    def union(self, x, y):
        super().union(self.d[x], self.d[y])

    def size(self, x):
        return super().size(self.d[x])

    def same(self, x, y):
        return super().same(self.d[x], self.d[y])

    def members(self, x):
        root = self.find(self.d[x])
        return [self.d_inv[i] for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [self.d_inv[i] for i, x in enumerate(self.parent) if x < 0]


l = ['A', 'B', 'C', 'D', 'E']
ufl = UnionFindLabel(l)
print(ufl)
# A: ['A']
# B: ['B']
# C: ['C']
# D: ['D']
# E: ['E']

ufl.union('A', 'D')
ufl.union('D', 'C')
ufl.union('E', 'B')
print(ufl)
# A: ['A', 'C', 'D']
# E: ['B', 'E']

print(ufl.find_label('D'))
# A

print(ufl.size('D'))
# 3

print(ufl.same('A', 'D'))
# True

print(ufl.members('D'))
# ['A', 'C', 'D']

print(ufl.roots())
# ['A', 'E']

print(ufl.group_count())
# 2

print(ufl.all_group_members())
# {'A': ['A', 'C', 'D'], 'E': ['B', 'E']}


# ist2021 3

class UnionFind: #UF木の実装
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.sizes = [1 for i in range(n)]
        self.time = [0 for i in range(n)]

    def find(self, i):
        while self.parent[i] != i:
            i = self.parent[i]
        return i
    
    def unite(self, t, a, b):
        i = self.find(a)
        j = self.find(b)
        self.parent[i] = j
        if i != j: # より⾼い⽅にマージ
            if self.sizes[i] > self.sizes[j]:
                self.parent[i] = i
                self.parent[j] = i
                self.sizes[i] += self.sizes[j]
                self.time[i] = t
                self.time[j] = t
            else:
                self.sizes[j] += self.sizes[i]
                self.time[j] = t
                self.time[i] = t

    def size(self, a):
        return self.sizes[self.find(a)]
    
    def find_time(self, a, b):
        if a == b: return 0
        elif self.time[a] < self.time[b]:
            if self.parent[a] == b: return self.time[a]
            a = self.parent[a]
            return self.find_time(a, b)
        else:
            if self.parent[b] == a: return self.time[b]
            b = self.parent[b]
            return self.find_time(a, b)

uf = UnionFind(6)
uf.unite(1,0,1)
uf.unite(2,1,2)
uf.unite(3,3,4)
uf.unite(4,1,3)
uf.find_time(0,3)
