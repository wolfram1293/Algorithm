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
    