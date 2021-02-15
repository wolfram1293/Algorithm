def eratosthenes2(n):
    lim=int(n**0.5)
    d=[i+1 for i in range(2,n,2)]
    D=[2]*(n+1)
    D[0]=D[1]=-1
    while True:
        p=d[0]
        if lim<p:
            for x in d:
                D[x]=x
            break
        D[p]=p
        d2=[]
        for x in d:
            if x%p!=0:
                d2.append(x)
            else:
                D[x]=p
        d=d2
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
elif maxc==1:
    print('pairwise coprime')
else:
    print('setwise coprime')