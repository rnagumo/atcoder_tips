
N = int(input())
X = list(map(int, input().split()))

res = 0
cur = X[0]
for v in X:
    res += max(0, cur - v)
    cur = max(cur, v)

print(res)
