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

N=int(input())
A=list(map(int,input().split()))
maxA=max(A)
D=eratosthenes2(maxA)
count=[0]*(maxA+1)
for x in A:
    pre=x+1
    while x>1:
        if pre!=D[x]:
            count[D[x]]+=1
            pre=D[x]
        x//=D[x]
maxc=max(count)
if maxc==N:
    print('not coprime')
elif maxc<=1:
    print('pairwise coprime')
else:
    print('setwise coprime')