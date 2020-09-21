
"""
https://atcoder.jp/contests/abc125/tasks/abc125_d

配列{X}に対して，隣合う数に-1を掛ける操作を繰り返した時の，和の最大値．

偶数個の負の数は全て正の数にできる．奇数個の場合には一個残るので，絶対値の小さいものを負にする．

もしくはdpを使う．dp[i][0]: 正, dp[i][1]: 負を表す．
初期状態はdp[0][1]は取り得ないので無効な値を入れる．
解はdp[-1][0]である（最後の要素のみを反転することはできないので）．

```python
dp = [[0, 0] for _ in range(N + 1)]
dp[0][1] = -10**9
for i in range(N):
    dp[i + 1][0] = max(dp[i][0] + X[i], dp[i][1] - X[i])
    dp[i + 1][1] = max(dp[i][0] - X[i], dp[i][1] + X[i])

print(dp[-1][0])
```
"""

N = int(input())
X = list(map(int, input().split()))

y = [abs(v) for v in X]
if sum(v < 0 for v in X) % 2 == 0:
    print(sum(y))
else:
    print(sum(y) - 2 * min(y))
