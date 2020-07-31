
"""
https://atcoder.jp/contests/abc133/tasks/abc133_e

木の塗り分けの問題．距離が2以下のノードは別の色で塗る．

* 親と自身以外の色で，子の色を塗る．
色の選び方: comb(K - 2, len(graph[v]) - 1)
色の塗り方: fac[len(graph[v]) - 1]

* ただし，根ノードは親がないので，別に計算する．
"""

from collections import deque

N, K = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N - 1)]

graph = [[] for _ in range(N + 1)]
for a, b in X:
    graph[a].append(b)
    graph[b].append(a)

MAX = 10 ** 5 + 1
MOD = 10 ** 9 + 7

# Factorial
fac = [0] * (MAX + 1)
fac[0] = 1
fac[1] = 1

# Inverse
inv = [0] * (MAX + 1)
inv[1] = 1

# Inverse factorial
finv = [0] * (MAX + 1)
finv[0] = 1
finv[1] = 1

for i in range(2, MAX + 1):
    fac[i] = fac[i - 1] * i % MOD
    inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD


def comb(n, k):
    if n < k or k < 0:
        return 0
    return (fac[n] * finv[k] * finv[n - k]) % MOD


visited = [False] * (N + 1)
visited[1] = True
ans = K * comb(K - 1, len(graph[1])) * fac[len(graph[1])] % MOD  # node 1
q = deque([1])
while q:
    u = q.popleft()
    for v in graph[u]:
        if visited[v]:
            continue

        ans *= comb(K - 2, len(graph[v]) - 1) * fac[len(graph[v]) - 1]
        ans %= MOD
        visited[v] = True
        q.append(v)

print(ans)
