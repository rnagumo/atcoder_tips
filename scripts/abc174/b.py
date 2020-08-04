
N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for a, b in X:
    if a ** 2 + b ** 2 <= D ** 2:
        ans += 1

print(ans)
