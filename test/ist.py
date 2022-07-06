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