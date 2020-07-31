
"""
https://atcoder.jp/contests/abc132/tasks/abc132_e

各ノードで複数の状態を用意して，その間の遷移を考える．
"""

from heapq import heappop, heappush

N, M = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(M)]
S, T = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for u, v in X:
    graph[u].append(v)

INF = 10 ** 9 + 7
d = [[INF] * 3 for _ in range(N + 1)]
d[S][0] = 0
pq = []
heappush(pq, (0, S))

while pq:
    _, u = heappop(pq)
    for v in graph[u]:
        for i in range(3):
            if d[v][(i + 1) % 3] > d[u][i] + 1:
                d[v][(i + 1) % 3] = d[u][i] + 1
                heappush(pq, (d[v][(i + 1) % 3], v))

if d[T][0] == INF:
    print(-1)
else:
    print(d[T][0] // 3)
