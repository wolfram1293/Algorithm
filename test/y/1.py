import sys

n, k = map(int, input().split())

for i in range(n): # 簡単な処理のため、入力データの処理と出力を同時に行った
    s, t = input().split()
    t = int(t)
    if t >= k:
        print(s)
