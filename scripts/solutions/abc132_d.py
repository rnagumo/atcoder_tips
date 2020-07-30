
"""
https://atcoder.jp/contests/abc132/tasks/abc132_d

K個の青玉，N-K個の赤玉から，青玉をi (0 <= i <= K + 1)個に分割する場合の数を求める．
comb(N-K+1, i): 赤玉の分割パターン
comb(K-1, i-1): 青玉の分割パターン

例）
N=8, K=5, i=1
xooxooox

comb(N-K+1, i) = 4: xxx -> 青玉の入る位置を，両端を含めた「隙間」の中からi個選ぶ
comb(K-1, i-1) = 1: ooooo -> 青玉の分割の位置を，両端を含めない「隙間」の中からi-1個選ぶ
"""

N, K = map(int, input().split())

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


for i in range(1, K + 1):
    res = comb(N - K + 1, i) * comb(K - 1, i - 1) % MOD
    print(res)
