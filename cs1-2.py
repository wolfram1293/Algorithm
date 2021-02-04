T=int(input())

for k in range(T):
    N=int(input())
    A=input()
    N=7
    A='-4 3 4 5 2 6 -9'
    A=[int(x.strip()) for x in A.split()]
    note=[[0 for i in range(N)] for j in range(N)]
    note[0][0]=A[0]
    for i in range(1,N):
        note[0][i]=note[0][i-1]+A[i]
    for i in range(1,N):
        for j in range(N):
            note[i][j]=note[i-1][j]-A[i-1]

    maxsubA=max(list(map(lambda x: max(x), note)))
    minsubA=abs(min(list(map(lambda x: min(x), note))))
    if maxsubA>minsubA:
        ans=maxsubA
    else:
        ans=minsubA
    print(ans)