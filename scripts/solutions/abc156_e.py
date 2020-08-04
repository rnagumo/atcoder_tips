
"""
https://atcoder.jp/contests/abc156/tasks/abc156_e

[1, 1, ..., 1]の長さNの配列を，K回だけ1ずつ移動させたときの，各インデックスの数の場合の数．

* K >= N - 1の場合には，全ての場合を表現できる．よって，N + (N - 1): 位置と仕切り位置の
並び順の中から仕切り位置N-1個を選ぶ．

* そうでない場合には，0の位置の個数は0~Kである．0の位置の個数をkとすると，0の位置をN個の中
からk個選び，かつN-1個の配列の隙間から残りの隙間N-1-k個の仕切りの位置を選ぶ．
"""

N, K = map(int, input().split())

MAX = 4 * 10 ** 5 + 1
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


if N - 1 <= K:
    print(comb(2 * N - 1, N - 1))
else:
    # zero: 0 ~ K
    ans = 0
    for n in range(K + 1):
        ans += comb(N, n) * comb(N - 1, N - n - 1)
        ans %= MOD
    print(ans)
