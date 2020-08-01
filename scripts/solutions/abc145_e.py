
"""
https://atcoder.jp/contests/abc145/tasks/abc145_e

時刻Tの間に，各要素のbの和を最大にするように選ぶ．
aだけのコストがかかる．ただし，配列の最後はコストを無視できる．
"""

N, T = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * (T + 1) for _ in range(N + 1)]
dp[0][0] = 0
X.sort()

for i in range(N):
    for j in range(T + 1):
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        if dp[i][j] >= 0 and j < T:
            k = min(T, j + X[i][0])
            dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + X[i][1])

print(max(dp[-1]))
