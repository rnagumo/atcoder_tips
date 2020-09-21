
"""
https://atcoder.jp/contests/tokiomarine2020/tasks/tokiomarine2020_c

配列{X}について，K回以下の操作を繰り返した時の配列を示す．
* 各要素について，i-X[i]~i+X[i]までに1を足す．

以下の二つのことに気づく必要がある．
* ある程度の回数（実際にはO(logN)）を繰り返すと，配列の全ての値がNに収束する．
* 範囲への積算には，累積和のテクニックを使うとO(N)で計算できる．

計算量はO(N logN)
"""

N, K = map(int, input().split())
X = list(map(int, input().split()))

x = X[:] + [0]
for _ in range(K):
    if all(v == N for v in x[:-1]):
        break

    new = [0] * (N + 1)
    for i in range(N):
        new[max(0, i - x[i])] += 1
        new[min(N, i + x[i] + 1)] -= 1

    for i in range(N):
        new[i + 1] += new[i]
    x = new[:]

print(*x[:-1])
