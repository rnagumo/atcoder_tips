
"""
https://atcoder.jp/contests/abc136/tasks/abc136_e

ある数に+1, 別の数に-1という演算をK回以下行うとき，全ての要素を割り切る正の整数の最大値．

* 総和は変わらないので，その約数が候補となる．
* その候補の倍数との差（つまり余り）の小さい方を-1，大きい方を+1の対象とする．
  -1の演算回数がK回以下であり，かつ両者の演算回数が等しい場合には，その場合は実現する．
* 累積和を使うと，O(N)で求めることができる．

計算量は，約数を求めるのにO(sqrt(max(A)*N))，後半はソートがボトルネックとなりO(NlogN)，
つまり，O(sqrt(max(A)*N)*NlogN)である．A <= 10^6, N<=500より，O(sqrt(5*10^8)*60)
~ O(10^6)程度なので十分に高速である．
"""

N, K = map(int, input().split())
X = list(map(int, input().split()))


def calc_divisor(x):
    divisor = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            divisor.append(i)
            if i != x // i:
                divisor.append(x // i)
    return divisor


divisor = calc_divisor(sum(X))
ans = 0
for v in divisor:
    cand = sorted(x % v for x in X)
    cs1 = [0] * (N + 1)
    for i in range(N):
        cs1[i + 1] = cs1[i] + cand[i]

    cs2 = [0] * (N + 1)
    for i in reversed(range(N)):
        cs2[i] = cs2[i + 1] + v - cand[i]

    for a, b in zip(cs1, cs2):
        if a <= K and a == b:
            ans = max(ans, v)
            break

print(ans)
