
N, X, M = map(int, input().split())

res = 0
a = X
appeared = []
circle = []
index = [-1] * M
for i in range(N):
    if index[a] != -1:
        for j in range(index[a], i):
            circle.append(appeared[j])
        break

    index[a] = i
    appeared.append(a)
    res += a
    a = pow(a, 2, M)

N -= len(appeared)
if N == 0:
    print(res)
    exit()

accm = [0] * (len(circle) + 1)
for i in range(len(circle)):
    accm[i + 1] = accm[i] + circle[i]

q = N // len(accm)
r = N % len(accm)
res += accm[-1] * q + accm[r]

print(res)
