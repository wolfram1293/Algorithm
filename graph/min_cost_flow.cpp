#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <vector>
#include <cassert>
#include <algorithm>
#include <functional>
// 蟻本p200
// 辺を表す構造体 (行き先、容量、コスト、逆辺)
struct edge { int to, cap, cost, rev; };
const int V=4; // 頂点数
std::vector<edge> G[V]; // グラフの隣接リスト表現
int dist[V]; // 最短距離
int prevv[V], preve[V]; // 直前の頂点と辺
int INF=1000000000;
// fromからtoへ向かう容量cap、コストcostの辺をグラフに追加する
void add_edge(int from, int to, int cap, int cost) {
  G[from].push_back((edge){to, cap, cost, static_cast<int>(G[to].size())});
  G[to].push_back((edge){from, 0, -cost, static_cast<int>(G[from].size()) - 1});
}

// sからtへの流量fの最小費用流を求める
// 流せない場合は-1を返す
int min_cost_flow(int s, int t, int f) {
  int res = 0;
  while (f > 0) {
    // ベルマンフォード法により、s-t間最短路を求める
    std::fill(dist, dist + V, INF);
    dist[s] = 0;
    bool update = true;
    while (update) {
      update = false;
      for (int v = 0; v < V; v++) {
        if (dist[v] == INF) continue;
        for (int i = 0; i < G[v].size(); i++) {
          edge &e = G[v][i];
          if (e.cap > 0 && dist[e.to] > dist[v] + e.cost) {
            dist[e.to] = dist[v] + e.cost;
            prevv[e.to] = v;
            preve[e.to] = i;
            update = true;
          }
        }
      }
    }

    if (dist[t] == INF) {
      // これ以上流せない
      return -1;
    }
    // s-t間最短路に沿って目一杯流す
    int d = f;
    for (int v = t; v != s; v = prevv[v]) {
      d = std::min(d, G[prevv[v]][preve[v]].cap);
    }
    
    f -= d;
    res += d * dist[t];
    for (int v = t; v != s; v = prevv[v]) {
      edge &e = G[prevv[v]][preve[v]];
      e.cap -= d;
      G[v][e.rev].cap += d;
    }
  }
  return res;
}

int main(){
  add_edge(0,1, 3, 6);
  add_edge(0,2, 5, 2);
  add_edge(1,3, 4, 3);
  add_edge(2,1, 7, 3);
  add_edge(2,3, 6, 9);
  
  printf("%d\n",min_cost_flow(0, 3, 7));
	return 0;
}
