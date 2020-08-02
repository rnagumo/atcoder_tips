
"""
https://atcoder.jp/contests/abc151/tasks/abc151_e

有限個の集合Xに対し，f(X) = max(X) - min(X)と定義する．
N個の整数列AからK個を選ぶ全ての場合のf(X)の和を求める．

sum f(X) = sum max(X) - sum min(X)となるので，各数について自身が最大・最小になる場合の数
を求めればよい．また，値が同じでも添字で区別できるので，値の重複については考慮しなくてよい．
最大・最小になる場合は，自身より大きい（小さい）数の中からK-1個を選べばよい．
"""

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


N, K = map(int, input().split())
X = list(map(int, input().split()))
X.sort()

ans = 0
for i in range(N):
    # Max
    ans += X[i] * comb(i, K - 1) % MOD
    ans %= MOD

    # Min
    ans -= X[i] * comb(N - i - 1, K - 1) % MOD
    ans %= MOD

print(ans)
