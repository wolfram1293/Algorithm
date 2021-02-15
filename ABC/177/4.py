class UnionFind():
    def __init__(self, n):
        self.n = n
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

N,M=map(int,input().split())
uf=UnionFind(N)
for i in range(M):
  A,B=map(int,input().split())
  uf.unite(A-1,B-1)

ans=0
for i in range(N):
  ans=max(ans,uf.size(i))
  
print(ans)
