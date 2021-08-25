# 最⼩費⽤流(min cost flow)
# プライマルデュアル法 
# sからtへの流量fの最小費用流を求める 流せない場合は-1を返す
# 蟻本p200参照
# ノード数V，エッジ数E，設定流量をFとする 最⼩コスト経路探索のためにはベルマンフォード法を使うとO(EV)必要．（隣接リストを使う場合）
# さらに，流量を1ずつしか増やせないのが最悪のケース．よって，O(FEV)
# ポテンシャルと呼ばれる⼯夫をするとダイクストラ法を使うことができる．
# この場合，O(FV^2)．ヒープを使うダイクストラ法を使えば， O(F(V+E)logV)に計算量を減らせる
def PrimalDual(G,s,t,f):
    V = len(G) # 頂点数
    prev_v = [0 for i in range(V)] # 直前の頂点
    prev_e = [0 for i in range(V)] # 直前の辺
    inf = 10**9
    res = 0 # 最⼩費⽤
    while f > 0:
        # ベルマンフォード法で最短路を求める(負の経路が存在するため)
        dist = [inf] * V # 最短距離
        dist[s] = 0
        update = True
        while update:
            update = False
            for v in range(V):
                if dist[v] == inf: continue
                for i in range(len(G[v])):
                    edge = G[v][i] # vからの辺 (行き先、容量、コスト、逆辺)
                    if edge[1] > 0 and dist[edge[0]] > dist[v] + edge[2]: # 最短距離を更新
                        dist[edge[0]] = dist[v] + edge[2]
                        prev_v[edge[0]] = v # 直前の頂点、辺も記録
                        prev_e[edge[0]] = i
                        update = True

        if dist[t] == inf: # これ以上流せないなら-1
            return -1

        d = f # 流量
        v = t
        # 最短路に沿ってできる限り流すというのを繰り返す
        while  v != s: # tからsまで
            d = min(d, G[prev_v[v]][prev_e[v]][1]) # 最短路に沿ってprev_vをたどって流せる量が最も少ないエッジの容量を流量とする
            v = prev_v[v]
        
        f -= d # 流したい量からdを引く
        res += d * dist[t] # コストをd流す分加算
        v = t
        while  v != s: # tからsまで
            G[prev_v[v]][prev_e[v]][1] -= d # 最短路に沿ってprev_vをたどって流した量dだけ容量を引く
            G[v][G[prev_v[v]][prev_e[v]][3]][1] += d # 逆辺は流した量dだけ容量を足す
            v = prev_v[v]
            
    return res

# アルゴリズム2021 
# 12最小費用流の例
V = 4 # 頂点数
G = [[] for i in range(V)] # グラフの隣接リスト表現
# fからtへ向かう容量cap、コストcostの辺をグラフに追加する
def add_edge(f,t,cap,cost):
    G[f].append([t,cap,cost,len(G[t])]) # 辺を表す (行き先、容量、コスト、逆辺) 逆辺(追加した時点でのlen(G[t])は下で追加する逆辺のindexを表す)
    G[t].append([f,0,-cost,len(G[f])-1]) # 逆辺の逆辺のindexは上ですでにappendされているのでlen(G[f])-1

add_edge(0, 1, 3, 6)
add_edge(0, 2, 5, 2)
add_edge(1, 3, 4, 3)
add_edge(2, 1, 7, 3)
add_edge(2, 3, 6, 9)
#print(G)
PrimalDual(G,0,3,7)

