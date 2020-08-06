
"""
https://atcoder.jp/contests/abc162/tasks/abc162_e

1~Kの整数からなる長さNの数列{A_i}について，全てについてのf(A)=gcd(A[1],...,A[N])の和を
求める．

ある数x = f(A)となる場合の数は，1. 全ての要素がxの倍数である = (K//x)^N通り，2. 少なくとも
一つはxである = -(ctr[2x]+ctr[3x]+...)，で求められる．

あとは，ある数が実現される場合の数を足せばよい．ans = sum(x*f(x))
"""

N, K = map(int, input().split())

MOD = 10 ** 9 + 7
ans = 0
ctr = [0] * (K + 1)

for x in reversed(range(1, K + 1)):
    ctr[x] = pow(K // x, N, MOD)
    for y in range(2 * x, K + 1, x):
        ctr[x] -= ctr[y]

ans = 0
for n in range(1, K + 1):
    ans += n * ctr[n]
    ans %= MOD

print(ans)
