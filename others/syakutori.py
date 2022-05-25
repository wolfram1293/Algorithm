def CI(A, M):
    N = len(A)
    count = [False] * M
    for i in range(N):
        if A[i] >= 0 and A[i] < M:
            count[A[i]] = True
    
    if all(count):
        return True
    else:
        return False
    
def syakutori(A, M):
    N = len(A)
    s = 0
    e = N-1
    l = 0
    r = 0
    while 1:
        #print(l,r,s,e,A[l:r+1])
        if CI(A[l:r+1], M):
            if r -l + 1 <= e - s + 1:
                s = l
                e = r
            if r - l + 1 >= M:
                l += 1
        else:
            if r < N - 1:
                r += 1
            else:
                break
    
    print(s, e, A[s:e+1])

M=2
A=[1,1,0,1]
print(A[2:4])
syakutori(A, M)