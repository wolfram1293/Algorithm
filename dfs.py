
#edges=[[] for i in range(N)] 
#各頂点からつながる頂点のリスト
edges = [
[1, 2],#ノードA
[0, 3, 5],#ノードB
[0, 3, 4],#ノードC
[1, 2, 5],#ノードD
[2, 6],#ノードE
[1, 3, 7],#ノードF
[4],#ノードG
[5]]#ノードH
N = len(edges)

#全てのノードを1度訪れ，全ノードを処理するまでに全ての辺を1通りチェックする．
#ノードの数をV，辺の数をEとする．隣接リストの場合，つながっているノードのみを処理することになるので,O(V+E)．

done = [0]*N #一度通った頂点を記録
def dfs(edges, start, end):
    waiting = []
    # 0: 未発⾒，1: 発⾒済だが未訪問，2: 訪問済
    done[start] = 2 # 開始ノードは訪問済
    for n in edges[start]:
        done[n] = 1 # 発⾒したが未訪問なので1
        waiting.append(n)
    while len(waiting):
        cur_node = waiting.pop()
        if done[cur_node] != 2:
            done[cur_node] = 2 # 訪問したので2
            if(end == cur_node): print('=FOUND!=')
            for n in edges[cur_node]:
                if done[n] != 2:
                    done[n] = 1 # 未訪問なので1
                    waiting.append(n)

dfs(edges, 0, 6)

#再帰版
done = [0]*N #一度通った頂点を記録
def dfs_re(edges, start, end):
    if len(edges[start])==0 or done[start]==1:
        return
    if start==end:
        print('=FOUND!=')
    done[start]=1
    for n in edges[start]:
        dfs_re(edges,n, end)

dfs_re(edges,0,6)
