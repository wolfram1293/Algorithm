T=int(input())
inf=1000000000
for i in range(T):
    N=int(input())
    A=input()
    A=[int(x.strip()) for x in A.split()]
    subA=0
    maxsubA= -inf
    back=0
    for j in range(N):
        subA+=A[j]
        if subA-A[back]>subA:
            subA=subA-A[back]
            back+=1
        if subA>maxsubA:
            maxsubA=subA                
    subA=0
    minsubA=inf
    for j in range(N):
        subA+=A[j]
        if subA-A[back]<subA:
            subA=subA-A[back]
            back+=1
        if subA<minsubA:
            minsubA=subA  
    
    if maxsubA>abs(minsubA):
        ans=maxsubA
    else:
        ans=abs(minsubA)
    print(ans)
         
         