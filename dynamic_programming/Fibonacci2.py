def Fibonacci2(n): # 漸化式方式
    f = [0] * (n+1)
    f[1] = 1
    if n >= 2:
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]
    return f[n]

n = 100
Fibonacci2(n)
