N=int(input())
A = list(map(int,input().split()))
mod=1000000007
ans=0
sumA=sum(A)
for i in range(N-1):
  sumA-=A[i]
  a=A[i]*sumA
  a%=mod
  ans+=a
  ans%=mod
print(ans)
