
N = int(input())
MOD = 10 ** 9 + 7

dp = [0] * (N + 1)
dp[0] = 1
for i in range(N + 1):
    for v in range(3, N + 1):
        if i - v >= 0:
            dp[i] += dp[i - v]
            dp[i] %= MOD

print(dp[-1] % MOD)
