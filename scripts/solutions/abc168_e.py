
"""
https://atcoder.jp/contests/abc168/tasks/abc168_e

ある組みについてA[i]*A[j] + B[i]*B[j] = 0とならないように要素を選ぶ場合の数．

題意を満たすには，以下の場合がある．
a=b=0: その要素一つのみを選ぶ．
a=0,b!=0 or a!=0,b=0: この二つの要素の組みは題意を満たす．この時，非ゼロの数の値は何でも
    よいので，適当に1にしておく．
a!=0,b!=0: 定数倍は考慮しないので，aとbの最大公約数で両者を割っておく．

以上より，題意を満たすのは，
(a, b), (b, a)の組みであり，かつ積の符号が異なるものである．
ここでは，a!=0, a*b>=0: (a, b)，それ以外: (b, a)としている．

数え上げる時には，(a, b)それぞれの数について，d[p][0]^2 + d[p][1]^2 - 1となる．
つまり，(a, b)の中の要素それぞれのin-out, (b, a)の中の要素それぞれのin-out，
全てが入らない場合を除くので-1である．
"""

from math import gcd

N = int(input())
X = [list(map(int, input().split())) for _ in range(N)]

d = {}
for a, b in X:
    if a == b == 0:
        pass
    elif a == 0:
        b = 1
    elif b == 0:
        a = 1
    else:
        v = gcd(a, b)
        a //= v
        b //= v

    if a != 0 and a * b >= 0:
        pair = (abs(a), abs(b))
        if pair not in d:
            d[pair] = [0, 0]
        d[pair][0] += 1
    else:
        pair = (abs(b), abs(a))
        if pair not in d:
            d[pair] = [0, 0]
        d[pair][1] += 1

MOD = 10 ** 9 + 7
zero = 0
ans = 1
for p in d:
    if p == (0, 0):
        zero = d[p][1]
    else:
        a, b = d[p]
        ans *= pow(2, a, MOD) + pow(2, b, MOD) - 1
        ans %= MOD

print((ans + zero - 1) % MOD)
