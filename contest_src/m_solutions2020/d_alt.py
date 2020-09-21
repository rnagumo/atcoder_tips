
N = int(input())
X = list(map(int, input().split()))

dp = [0] * N
dp[0] = 1000
for i in range(1, N):
    dp[i] = dp[i - 1]
    for j in range(i):
        n = dp[j] // X[j]
        dp[i] = max(dp[i], dp[j] + (X[i] - X[j]) * n)

print(dp[-1])
