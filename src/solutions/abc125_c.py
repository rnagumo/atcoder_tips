
"""
https://atcoder.jp/contests/abc125/tasks/abc125_c

配列{X}において，各要素X_i以外の最大公約数の最大値を求める．

ある要素X_i以外の数の最大公約数は，gcd(gcd(X_{0:i-1}), gcd(X_{i+1:N}))で求められる．
よって，前後から累積した時の最大公約数を予め計算しておくことで，各要素についてはO(logA)で
最大公約数を計算できる．

計算量はO(N log A1 + N log An)
"""

from math import gcd

N = int(input())
X = list(map(int, input().split()))

left = [0] * (N + 2)
right = [0] * (N + 2)

for i in range(N):
    left[i + 1] = gcd(left[i], X[i])

for i in reversed(range(N)):
    right[i + 1] = gcd(right[i + 2], X[i])

ans = 1
for i in range(N):
    ans = max(ans, gcd(left[i], right[i + 2]))

print(ans)
