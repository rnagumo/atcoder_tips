
N = int(input())
X = list(map(int, input().split()))
MOD = 10 ** 9 + 7

cnt = [0] * (N + 1)
for i in reversed(range(N)):
    cnt[i] = cnt[i + 1] + X[i] % MOD

res = 0
for i in range(N):
    res += X[i] * cnt[i + 1] % MOD
    res %= MOD
print(res)
