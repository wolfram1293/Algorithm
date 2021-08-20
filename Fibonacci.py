# 再帰
def Fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return Fibonacci(n-1) + Fibonacci(n-2)

Fibonacci(40)

# 漸化式
def Fibonacci2(n):
    A = [0] * (n+1)
    for i in range(n+1):
        if i == 0: A[i] = 0
        elif i == 1: A[i] = 1
        else:  A[i] = A[i-1] + A[i-2]
    
    return A[n]

Fibonacci2(40)

# 一般項から
import numpy 
# 繰り返し2乗法の実装
def self_pow(x,n):
    ans = 1
    while n:
        if n % 2:
            ans *= x
        x *= x
        n >>= 1
    return ans

def Fibonacci3(n):
    sqrt = numpy.sqrt(5)
    f = (1/sqrt)*(self_pow((1+sqrt)/2,n) - self_pow((1-sqrt)/2,n))
    return round(f)

Fibonacci3(40)