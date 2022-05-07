# DP フィボナッチ数列
n = 100
f = [0] * (n+1)

def Fibonacci1(n): # メモ化再帰
    if n<= 2:
        f[n] = 1
        return f[n]
    elif f[n] != 0:
        return f[n]
    else:
        f[n] = Fibonacci1(n-1) + Fibonacci1(n-2)
        return f[n]

Fibonacci1(n)