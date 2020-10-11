"""
for-loopの中の計算で，大きい数同士の掛け算は時間がかかるので，変形する．

(2^{cnt} - 1) * 2^{total - cnt}
= (2^{cnt} - 1) * 2^{-cnt} * 2^{total}
= (1 - 2^{-cnt}) * 2^{total}
= (1 - (2^{-1})^{cnt}) * 2^{total}

このように変形すると，後ろの2^{total}はくくりだせる．
2^{-1}はあらかじめ計算できる．
"""

H, W = map(int, input().split())
X = [list(map(lambda x: x == ".", input())) for _ in range(1, H + 1)]
MOD = 10 ** 9 + 7

ctr0 = [[0] * (W + 1) for _ in range(H + 1)]
for j in range(1, W + 1):
    for i in range(1, H + 1):
        if X[i - 1][j - 1]:
            ctr0[i][j] = ctr0[i - 1][j] + 1

    for i in reversed(range(1, H)):
        if X[i - 1][j - 1]:
            ctr0[i][j] = max(ctr0[i][j], ctr0[i + 1][j])

ctr1 = [[0] * (W + 1) for _ in range(H + 1)]
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if X[i - 1][j - 1]:
            ctr1[i][j] = ctr1[i][j - 1] + 1

    for j in reversed(range(1, W)):
        if X[i - 1][j - 1]:
            ctr1[i][j] = max(ctr1[i][j], ctr1[i][j + 1])

res = 0
inv = pow(2, MOD - 2, MOD)
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if X[i - 1][j - 1]:
            res += 1 - pow(inv, ctr0[i][j] + ctr1[i][j] - 1, MOD)
            res %= MOD

total = sum(sum(v) for v in X)
print(res * pow(2, total, MOD) % MOD)
