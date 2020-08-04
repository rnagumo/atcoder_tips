
"""
https://atcoder.jp/contests/abc155/tasks/abc155_e

典型的な桁DPの問題

dp[i][0]: i桁目で，確定している（ちょうど払う）数
dp[i][1]: i桁目で，一つ上の桁の紙幣を1枚多く出して，お釣りをもらう場合
"""

N = input()

lim = len(N)
dp = [[0, 0] for _ in range(lim + 1)]
dp[0][1] = 1
for i in range(lim):
    n = int(N[i])
    dp[i + 1][0] = min(dp[i][0] + n, dp[i][1] + 10 - n)
    dp[i + 1][1] = min(dp[i][0] + n + 1, dp[i][1] + 10 - n - 1)

print(dp[-1][0])
