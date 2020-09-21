
"""
https://atcoder.jp/contests/abc135/tasks/abc135_d
https://drken1215.hatenablog.com/entry/2020/04/23/194600

典型的な桁DPの問題．「13で割ったら5余るパターン」の数を求める．
ただし，'?'には0~9までの任意の数が入る．
"""

S = input()
n = len(S)
dp = [[0] * 13 for _ in range(n + 1)]
dp[0][0] = 1
MOD = 10 ** 9 + 7
for i in range(n):
    for j in range(13):
        if S[i] != "?":
            dp[i + 1][(j * 10 + int(S[i])) % 13] += dp[i][j]
        else:
            for k in range(10):
                dp[i + 1][(j * 10 + k) % 13] += dp[i][j]

    for j in range(13):
        dp[i + 1][j] %= MOD

print(dp[-1][5])
