N = int(input())
d = [int(input()) for i in range(N)]
d.sort()
ans=1
for i in range(1,N):
  if d[i-1]<d[i]:
    ans+=1 
print(ans)