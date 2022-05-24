#str
s = input() 
#int
s = int(input()) 
#float
s = float(input())

#list(str)
s = input().split()
#list(int)
s = list(map(int, input().split()))

#N行
N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))
#N行(list内包表記)
A = [int(input()) for _ in range(N)]

#N行(2次元)
N = int(input())
xy = [map(int, input().split()) for _ in range(N)]
x, y = [list(i) for i in zip(*xy)]

#N行(2次元)intとstr混合
N = int(input())
list = []
for i in range(N):
    a, b=input().split()
    list.append([int(a), b])

#行列
N, M = map(int,input().split()) 
A = [list(map(int, input().split())) for l in range(M)]
