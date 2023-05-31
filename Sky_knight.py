from collections import deque

X, Y = 300, 300

def bfs_maze(gx, gy):
    map = [[-1 for i in range(2 * Y + 1)] for j in range(2 * X + 1)]
    waiting = deque()
    waiting.append([Y, X])
    map[Y][X] = 0
    dydx = [[1, 2], [-1, 2], [1, -2], [-1, -2], [2, 1], [-2, 1], [2, -1], [-2, -1]]
    while len(waiting):
        y, x = waiting.popleft()
        if y == gy and x == gx:
            break
        for i in range(8): #8方向について行けるか検証
            dy, dx = dydx[i]
            ny, nx = y + dy, x + dx
            if 0 <= ny < 2 * Y + 1 and 0 <= nx < 2 * X + 1 and map[ny][nx] == -1:
                waiting.append([ny, nx])
                map[ny][nx] = map[y][x] + 1
    
    return map[gy][gx]

x, y = map(int, input().split())
print(bfs_maze(x + X, y + Y))
