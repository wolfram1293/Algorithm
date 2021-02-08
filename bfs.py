from collections import deque

N,M,S,T=map(int,input().split())
edges=[[] for i in range(N)] #各頂点からつながる頂点のリスト
for i in range(M):
    a,b=list(map(int,input().split()))
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)

done = [0]*N #一度通った頂点を記録
def bfs(edges, start, end):
    waiting = deque()
    # 0: 未発⾒，1: 発⾒済だが未訪問，2: 訪問済
    done[start] = 2 # 開始ノードは訪問済
    for n in edges[start]:
        done[n] = 1 # 発⾒したが未訪問なので1
        waiting.append(n)
    while len(waiting):
        cur_node = waiting.popleft()
        if done[cur_node] != 2:
            done[cur_node] = 2 # 訪問したので2
            if(end == cur_node): print('=FOUND!=')
            for n in edges[cur_node]:
                if done[n] != 2:
                    done[n] = 1 # 未訪問なので1
                    waiting.append(n) # キュー追加
