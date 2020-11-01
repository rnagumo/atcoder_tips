
def count(x, n):
    if x <= n + 1:
        return x - 1
    return max(0, n - (x - n) + 1)


N, K = map(int, input().split())

res = 0
if K < 0:
    K = -K
for x in range(K + 2, 2 * N + 1):
    y = x - K
    res += count(x, N) * count(y, N)

print(res)
