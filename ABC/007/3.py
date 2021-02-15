from collections import deque

H,W=map(int,input().split())
sy,sx=map(int,input().split())
gy,gx=map(int,input().split())
A=[]
for i in range(H):
    A.append(list(input()))
d=[[-1 for i in range(W)] for j in range(H)] #スタートからの距離を入れるリスト

def bfs(sx,sy,gx,gy,A):
    waiting = deque()
    waiting.append([sy,sx])
    d[sy][sx]=0
    while len(waiting):
        y,x=waiting.popleft()
        if y==gy and x==gx:
            break
        for i in range(4): #縦横の4方向について行けるか検証
            ny,nx=y+[1,0,-1,0][i],x+[0,1,0,-1][i]
            if 0<=ny<H and 0<=nx<W and d[ny][nx]==-1 and A[ny][nx]!='#':
                waiting.append([ny,nx])
                d[ny][nx]=d[y][x]+1
    return d[gy][gx]

print(bfs(sx-1,sy-1,gx-1,gy-1,A))
