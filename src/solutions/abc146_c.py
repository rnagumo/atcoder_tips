
"""
https://atcoder.jp/contests/abc146/tasks/abc146_c

A * N + B * d(N) <= Xとなる最大の整数Nを求める．
X <= 10^18より，可能な範囲を二分探索で求める．
"""

A, B, X = map(int, input().split())

ub = 10 ** 9 + 1
lb = 0
while ub - lb > 1:
    mid = (ub + lb) // 2

    n = mid
    res = A * n
    dn = 0
    while n > 0:
        dn += 1
        n //= 10
    res += B * dn

    if res <= X:
        lb = mid
    else:
        ub = mid

print(lb)
