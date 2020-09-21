
"""
https://atcoder.jp/contests/abc146/tasks/abc146_e

累積和Sとした時，i < j, (S[j] - S[i]) % K == j - iとなる組の数を求める．

式変形すると，(S[j] - j) % K == (S[i] - i) % Kとなるj - K < i < jを求めることになる．
Kの区間がスライドしていくので，範囲を飛び出した値は，カウンターから引けばよい．
"""

from collections import defaultdict

N, K = map(int, input().split())
X = list(map(int, input().split()))

cs = [0] * (N + 1)
for i in range(N):
    cs[i + 1] = cs[i] + X[i]

y = [(cs[i] - i) % K for i in range(N + 1)]
ctr = defaultdict(int)
ans = 0
for i in range(N + 1):
    ans += ctr[y[i]]
    ctr[y[i]] += 1
    if i - K + 1 >= 0:
        ctr[y[i - K + 1]] -= 1

print(ans)
