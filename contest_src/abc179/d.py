
N, K = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(K)]
MOD = 998244353

dp = [0] * N
sdp = [0] * (N + 1)
dp[0] = 1
sdp[1] = 1

for i in range(1, N):
    for l, r in X:
        dp[i] += sdp[max(0, i - l + 1)] - sdp[max(0, i - r)]
        dp[i] %= MOD
    sdp[i + 1] = sdp[i] + dp[i]
    sdp[i + 1] %= MOD

print(dp[-1])
