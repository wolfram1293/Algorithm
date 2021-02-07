N = int(input())
A = list(map(int, input().split()))
count=[0]*N
for i in range(N):
  while A[i]%2==0:
    A[i]=A[i]/2
    count[i]+=1
print(min(count))