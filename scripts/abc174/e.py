
N, K = map(int, input().split())
X = list(map(int, input().split()))

ub = 10 ** 9 + 7
lb = 0
while ub - lb > 1:
    mid = (ub + lb) // 2

    res = 0
    for v in X:
        res += (v - 1) // mid

    if res <= K:
        ub = mid
    else:
        lb = mid

print(ub)
