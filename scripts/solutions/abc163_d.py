
"""
https://atcoder.jp/contests/abc163/tasks/abc163_d

0~NまでのN+1個の数の中から，K個以上の数を選んだとき，その和としてあり得るものの個数を求める．

0~Nまでの累積和を予め求めると，数の和をO(1)で計算できる．

選ぶ個数kをK~Nと変化させた時に，和の種類の個数を求めればよい．
k個選ぶ時，その和の最小値は小さい方からk個を撮った場合でありcount[k-1]，最大値は大きい方から
k個を撮った場合でありcount[-1]-count[-k-1]である．
"""

N, K = map(int, input().split())

MOD = 10 ** 9 + 7
count = [0] * (N + 1)
for i in range(1, N + 1):
    count[i] += count[i - 1] + i
    count[i] %= MOD

ans = 1
for k in range(K, N + 1):
    ans += (count[-1] - count[-k - 1]) - count[k - 1] + 1
    ans %= MOD
print(ans)
