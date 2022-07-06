# ist 2022 3
def CountTinS(S,T,k):
    cnt = 0
    N = len(S)
    M = len(T)
    for i in range(N-M+1):
        for j in range(M):
            if S[i+j] != T[j]:
                break
            if j == M-1:
                cnt +=1
    return cnt

S = [1,2,0,2,1,0,2,1]
T = [2,1]
k = 3
CountTinS(S,T,k)

# O(n)ver
def CountTinS2(S,T,k):
    def matchTinS(numS):
        return True if numS == numT else False
        
    cnt = 0
    N = len(S)
    M = len(T)
    numS = 0
    numT = 0
    for i in range(M):
        numS += S[i] * pow(k,M-i-1)
        numT += T[i] * pow(k,M-i-1)
    for i in range(N-M+1):
        if i > 0:
            numS = (numS - S[i-1] * pow(k,M-1)) * k + S[i+M-1]
        if matchTinS(numS):
            cnt +=1
    return cnt

S = [1,2,0,2,1,0,2,1]
T = [2,1]
k = 3
CountTinS2(S,T,k)

# nazo?

import numpy as np
import matplotlib.pyplot as plt
plt.axes().set_aspect('equal', 'datalim')
n = 10
N = np.arange(1, n+1)
x = (N ** 3) * np.exp(-N) * np.sin(np.pi/N)
plt.plot(N, x, marker=".")
plt.show

y = np.array([len(N), max(x), np.where(x == min(x))[0].tolist()[0]])
print(y)

a = np.random.normal(loc = 1, scale = np.sqrt(100), size  = 5)
b = 2 * np.random.rand(5) - 1
X = np.matrix([a, b])
print(X)
