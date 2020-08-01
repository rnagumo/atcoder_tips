
"""
https://atcoder.jp/contests/abc139/tasks/abc139_e

試合順Xを満たすような順序の決め方を求める．

試合(i, j)を一つのノードに見立て，ある試合(i, j)の後に試合(k, l)をする場合に，
両者のノード間に辺をひく．

また，あるノードの全ての親を訪れた後に，そのノードは実行可能となる．
これを表現するために，親ノードの数をparentsとして持ち，親を訪れるたびに1ずつひく．
そして，parentsの値が0になったとき，そのノードを訪れる．

dequeの初期値は，初めから親ノードの数が0のものに限る．
下の実装では自分同士の対戦(i, i)も含めることになるが，graph[(i, i)]は空なので問題ない．
"""

from collections import deque

N = int(input())
X = [list(map(int, input().split())) for _ in range(N)]

graph = [[] for _ in range(N * N)]
parents = [0] * (N * N)
for i, nodes in enumerate(X):
    for j1, j2 in zip(nodes[:-1], nodes[1:]):
        n1 = max(i, j1 - 1) * N + min(i, j1 - 1)
        n2 = max(i, j2 - 1) * N + min(i, j2 - 1)
        graph[n1].append(n2)
        parents[n2] += 1

dist = [0] * (N * N)
visited = [False] * (N * N)
q = deque()
for i, v in enumerate(parents):
    if v == 0:
        q.append(i)
        visited[i] = True
        dist[i] = 1

while q:
    u = q.popleft()
    for v in graph[u]:
        if visited[v]:
            continue

        parents[v] -= 1
        if parents[v] == 0:
            visited[v] = True
            dist[v] = dist[u] + 1
            q.append(v)

print(max(dist) if all(visited) else -1)
