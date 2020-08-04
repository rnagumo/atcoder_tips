
"""
https://atcoder.jp/contests/abc154/tasks/abc154_f

r1 <= i <= r2, c1 <= j <= c2を満たすグリッド内の各点への経路の総和．

一個右へ行くには，r列のうちのどこかの点から右へいけばよいので，以下のように分解できる．
f(r + 1, c) = f(r, 0) + f(r, 1) + ... + f(r, c)

また，ある点への経路は，縦と横の経路の並び替えなので以下で求まる．
f(r, c) = {r+c}_C_c
"""

r1, c1, r2, c2 = map(int, input().split())

MAX = 2 * 10 ** 6 + 1
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


def f(r, c):
    return fac[r + c] * finv[r] * finv[c] % MOD


ans = 0
for i in range(c1, c2 + 1):
    ans += f(r2, i + 1) - f(r1 - 1, i + 1)
    ans %= MOD
print(ans)
