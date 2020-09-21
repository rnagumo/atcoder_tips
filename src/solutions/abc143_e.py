
"""
https://atcoder.jp/contests/abc143/tasks/abc143_e

クエリされた点対間の「給油回数」を求める．

Warshall-Floydで全点対間の最短経路を求める．
到達できる点対間は1とする．そうでない場合には，給油回数を重ねることになる．
"""

N, M, L = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(M)]
Q = int(input())
Y = [list(map(int, input().split())) for _ in range(Q)]

INF = 10 ** 9 + 7
graph = [[INF] * N for _ in range(N)]
count = [[INF] * N for _ in range(N)]
for i in range(N):
    graph[i][i] = 0
    count[i][i] = 0

for a, b, c in X:
    graph[a - 1][b - 1] = c
    graph[b - 1][a - 1] = c

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(N):
    for j in range(N):
        if i != j and graph[i][j] <= L:
            count[i][j] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            count[i][j] = min(count[i][j], count[i][k] + count[k][j])

for s, t in Y:
    if count[s - 1][t - 1] == INF:
        print(-1)
    else:
        print(count[s - 1][t - 1] - 1)
