def CI2(M, count): # 三項演算式が使いたかっただけ
    return True if sum(a > 0 for a in count) == M else False
    
def syakutori2(A, M):
    N = len(A)
    s = 0
    e = N - 1
    l = 0
    r = 0
    count = [0] * M
    if A[0] >= 0 and A[0] < M:
            count[A[0]] += 1
    while 1:
        #print(l,r,s,e,A[l:r+1],count)
        if CI2(M, count):
            if r - l <= e - s:
                s = l
                e = r
            if r - l + 1 >= M:
                if A[l] >= 0 and A[l] < M:
                    count[A[l]] -= 1
                l += 1
        else:
            if r < N - 1:
                r += 1
                if A[r] >= 0 and A[r] < M:
                    count[A[r]] += 1
            else:
                break
    
    print(s, e, A[s:e+1])

M = 2
A = [1,1,0,1]
syakutori2(A, M)