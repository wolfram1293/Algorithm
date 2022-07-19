# nPkをMで割ったあまり
def nPk(N,K):
    M = 10**9 + 7 # 素数
    a = 1
    for i in range(N-K):
        a *= i+1
        a %= M
    b = a
    for i in range(N-K,N):
        b *= i+1
        b %= M
    ans = pow(a,M-2,M) #フェルマーの⼩定理より, 剰余の割り算 = M-2乗を掛ける
    ans *= b
    ans %= M
    return ans

N=5
K=3
nPk(N,K)

# nCkをMで割ったあまり
def nCk(N,K):
    M = 10**9 + 7 # 素数
    a = 1
    for i in range(N-K):
        a *= i + 1
        a %= M
    b = a
    for i in range(N-K,N):
        b *= i+1
        b %= M
    c = 1
    for i in range(K):
        c *= i+1
        c %= M
    ans = pow(a,M-2,M) #剰余の割り算 = M-2乗を掛ける
    ans *= pow(c,M-2,M)
    ans %= M
    ans *= b
    ans %= M
    return ans

N = 5
K = 3
nCk(N,K)
