
"""
配列へのアクセスはO(1)といえど，配列が大きいと時間がかかる．
よって，配列の大きさを小さくしたい．

1. 今回の問題の制約「列あたりの個数制限」を用いる．
列あたりの個数制限なので，行を移ると状態が0にリセットされる．
この性質を使うと，dp配列に行情報はいらないことになる．

```python
dp = [[0] * 4 for _ in range(C + 1)]
for i in range(1, R + 1):
    # Vertical transition
    for j in range(1, C + 1):
        dp[j][0] = max(dp[j])
        for k in range(1, 4):
            dp[j][k] = 0

    # Horizontal or picking-up transition
    for j in range(1, C + 1):
        for k in reversed(range(4)):
            dp[j][k] = max(dp[j][k], dp[j - 1][k])
            if items[i][j] and k < 3:
                dp[j][k + 1] = max(dp[j][k + 1], dp[j][k] + items[i][j])
```

2. 状態に応じて別の配列を用意する．

"""


R, C, K = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(K)]

items = [[0] * (C + 1) for _ in range(R + 1)]
for r, c, v in X:
    items[r][c] = v

dp0 = [[0] * (C + 1) for _ in range(R + 1)]
dp1 = [[0] * (C + 1) for _ in range(R + 1)]
dp2 = [[0] * (C + 1) for _ in range(R + 1)]
dp3 = [[0] * (C + 1) for _ in range(R + 1)]
for i in range(1, R + 1):
    for j in range(1, C + 1):
        dp0[i][j] = max(dp1[i - 1][j], dp2[i - 1][j], dp3[i - 1][j])

        dp3[i][j] = max(dp3[i][j], dp3[i][j - 1])
        dp2[i][j] = max(dp2[i][j], dp2[i][j - 1])
        dp1[i][j] = max(dp1[i][j], dp1[i][j - 1])
        dp0[i][j] = max(dp0[i][j], dp0[i][j - 1])

        if items[i][j]:
            dp3[i][j] = max(dp3[i][j], dp2[i][j] + items[i][j])
            dp2[i][j] = max(dp2[i][j], dp1[i][j] + items[i][j])
            dp1[i][j] = max(dp1[i][j], dp0[i][j] + items[i][j])

print(max(dp1[-1][-1], dp2[-1][-1], dp3[-1][-1]))
