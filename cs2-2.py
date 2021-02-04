#!/usr/bin/python3
class UnionFind():
    def __init__(self, n):
        self.parents = [-1]*n

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

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

def solve(n, d, x, y):
  """Returns the sizes of groups in descending order."""
  # Write your solution here.
  #
  # Warning: Printing unwanted or ill-formatted data to output will cause
  # the test cases to fail.
  uf = UnionFind(n)
  for i in range(d):
    uf.unite(x[i]-1,y[i]-1)
  roots = uf.roots()
  s = []
  for i in range(len(roots)):
    s.append(uf.size(roots[i]))
  s.sort(reverse=True)
  return s

def main():
  case_count = int(input())
  for case_id in range(1, case_count + 1):
    input()  # Skip empty line.
    n = int(input())
    d = int(input())
    x = []
    y = []
    for _ in range(d):
      xi, yi = input().split()
      x.append(int(xi))
      y.append(int(yi))
    s = solve(n, d, x, y)
    print('Case #{}: {}'.format(case_id, ' '.join(map(str, s))))
if __name__ == '__main__':
  main()