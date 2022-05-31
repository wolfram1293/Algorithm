def main(lines):
    N = int(lines[0])
    P = list(map(int, lines[1].split()))
    edges = [[] for i in range(N)]
    for i in range(N-1):
        edges[i+1].append(P[i]-1)
        edges[P[i]-1].append(i+1)
    
    ans = [0] * N
    for i in range(N):
        ans[i] = 1
        waiting = []
        depth = [0] * N
        done = [0] * N
        done[i] = 1 # 開始ノードは訪問済
        depth[i] = 0

        for n in edges[i]:
            depth[n] = 1
            waiting.append(n)
            
        while len(waiting):
            cur_node = waiting.pop()
            if done[cur_node] != 1:
                done[cur_node] = 1 # 訪問した
                ans[i] += 1 

                for n in edges[cur_node]:
                    if done[n] != 1:
                        depth[n] = depth[cur_node] + 1
                        if depth[n] > 3:
                            break
                        waiting.append(n)
    
    print(*ans)