
N = int(input())
X = list(map(int, input().split()))

res = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if (X[i] != X[j] and X[j] != X[k] and X[i] != X[k]):
                less = max(X[i], X[j], X[k])
                if sum([X[i], X[j], X[k]]) - less > less:
                    res += 1

print(res)
