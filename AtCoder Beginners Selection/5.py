N,A,B = map(int, input().split())
ans=0
for i in range(1,N+1):
  sumn=0
  n=i
  while n>0:
    sumn+=n%10
    n//=10
  if A<=sumn<=B:
    ans+=i
print(ans)