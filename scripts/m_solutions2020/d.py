
N = int(input())
X = list(map(int, input().split()))

cur = 1000
for i in range(N - 1):
    if X[i] < X[i + 1]:
        stocks = cur // X[i]
    else:
        stocks = 0

    cur += (X[i + 1] - X[i]) * stocks

# Last
print(cur)
