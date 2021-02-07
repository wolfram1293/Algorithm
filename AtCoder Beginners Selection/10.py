import sys
N = int(input())
x=0
y=0
t=0
for i in range(N):
  ti,xi,yi = map(int, input().split())
  dt=ti-t
  dx=abs(xi-x)
  dy=abs(yi-y)
  if dt>=dx+dy and (dt-dx-dy)%2==0:
    t=ti
    x=xi
    y=yi
  else:
    print('No')
    sys.exit()
print('Yes')
