import sys
from collections import deque

step = int(input()) 
H, W = map(int, input().split())
c = []
trainers = []
for i in range(H):
    c.append(list(input()))
    for j in range(W):
        if c[i][j] == 'A':
            ay = i
            ax = j
        elif c[i][j] == 'B':
            by = i
            bx = j
        elif not (c[i][j] == '#' or c[i][j] == '.'):
            trainers.append([c[i][j], i, j])

def bfs_maze(sx,sy,gx,gy,A,H,W):
    d = [[-1 for i in range(W)] for j in range(H)]
    waiting = deque()
    waiting.append([sy,sx])
    d[sy][sx] = 0
    while len(waiting):
        y, x = waiting.popleft()
        if y == gy and x == gx:
            break
        for i in range(4): #縦横の4方向について行けるか検証
            ny, nx = y + [1,0,-1,0][i], x + [0,1,0,-1][i]
            if 0 <= ny < H and 0 <= nx < W and d[ny][nx] == -1 and (A[ny][nx] == '.' or A[ny][nx] == 'A' or A[ny][nx] == 'B'):
                waiting.append([ny,nx])
                d[ny][nx] = d[y][x] + 1
    
    return d

def add_trainers(trainers, H, W): # データ数多い
    sights = deque()
    for v in trainers:
        if v[0] == 'N':
            mode = 'y'
            start = v[1] - 1
            goal = -1
            div = -1
        elif v[0] == 'E':
            mode = 'x'
            start = v[2] + 1
            goal = W
            div = 1
        elif v[0] == 'S':
            mode = 'y'
            start = v[1] + 1
            goal = H
            div = 1
        else:
            mode = 'x'
            start = v[2] - 1
            goal = -1
            div = -1
            
        sight = []
        for i in range(start, goal, div):
            if mode == 'x':
                if c[v[1]][i] != '.':
                    break
                sight.append([v[1], i])
            else:
                if c[i][v[2]] != '.':
                    break
                sight.append([i, v[2]])
        sights.append(sight)

    return sights

def bfs_maze2(sx,sy,gx,gy,d,H,W,ans1):
    waiting = deque()
    waiting.append([gy,gx])
    path = deque()
    path.append([gy, gx])
    formerpaths = [[[] for i in range(W)] for j in range(H)]
    formerpaths[gy][gx].append(path)
    while len(waiting):
        y, x = waiting.popleft()
        if y == sy and x == sx:
            break
        cnt = 0
        formerpath = formerpaths[y][x]
        for i in range(4): #縦横の4方向について行けるか検証
            ny, nx = y + [1,0,-1,0][i], x + [0,1,0,-1][i]
            if 0 <= ny < H and 0 <= nx < W and d[ny][nx] == d[y][x] - 1:
                waiting.append([ny, nx])
                for p in formerpath:
                    p.appendleft([ny, nx])
                    formerpaths[ny][nx].append(p)

    return formerpath
        
def count_battle(paths, sights_original):
    list_nbattle = []
    for path in paths:
        sights = sights_original
        nbattle = 0
        for v in path:
            y, x = v[0], v[1]
            n = len(sights)
            for i in range(n):
                flag = 1
                sight = sights.popleft()
                for s in sight:
                    if s == [y, x]:
                        nbattle += 1
                        flag = 0
                        break
                if flag:
                    sights.append(sight)

        list_nbattle.append(nbattle)

    return list_nbattle 

d = bfs_maze(ax,ay,bx,by,c,H,W)
ans1 = d[by][bx]
sights = add_trainers(trainers, H, W)
if step == 3:
    paths= bfs_maze2(ax,ay,bx,by,d,H,W,ans1)
else:
    x = bx
    y = by
    paths =[]
    path = deque()
    path.append([y, x])
    for j in range(ans1-1 , -1, -1):
        for i in range(4): #縦横の4方向について行けるか検証
            ny, nx = y + [1,0,-1,0][i], x + [0,1,0,-1][i]
            if 0 <= ny < H and 0 <= nx < W and d[ny][nx] == j:
                path.appendleft([ny,nx])
                y, x = ny, nx
                break
                
    paths.append(path)

list_nbattle = count_battle(paths, sights)
ans2 = max(list_nbattle)

print(ans1, ans2)
