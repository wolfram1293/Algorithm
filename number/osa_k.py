def eratosthenes2(n):
    D=[-1]*(n+1)
    D[0]=0
    D[1]=1
    for i in range(2, n+1):
        if D[i] == -1:
            D[i] = i
            for j in range(i*i, n+1, i):
                if D[j] == -1:
                    D[j] = i
    return D
