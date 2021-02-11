#根の親の値にサイズの情報を持たせる
class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


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



class UnionFindLabel(UnionFind):
    def __init__(self, labels):
        assert len(labels) == len(set(labels))

        self.n = len(labels)
        self.parents = [-1] * self.n
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
        return [self.d_inv[i] for i, x in enumerate(self.parents) if x < 0]


