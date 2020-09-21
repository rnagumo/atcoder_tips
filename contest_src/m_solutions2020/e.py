
N = int(input())
X = [list(map(int, input().split())) for _ in range(N)]

ctr_x = [[0] * N for _ in range(2 ** N)]
ctr_y = [[0] * N for _ in range(2 ** N)]
for bit in range(2 ** N):
    for i in range(N):
        tmp_x = abs(X[i][0])
        tmp_y = abs(X[i][1])
        for j in range(N):
            if bit >> j & 1:
                tmp_x = min(tmp_x, abs(X[i][0] - X[j][0]))
                tmp_y = min(tmp_y, abs(X[i][1] - X[j][1]))

        ctr_x[bit][i] = tmp_x
        ctr_y[bit][i] = tmp_y

ans = [10 ** 12] * (N + 1)
for bit in range(2 ** N):
    cnt = bin(bit).count("1")
    for i in reversed(range(bit + 1)):
        i &= bit
        cost = 0
        for j in range(N):
            if not bit >> j & 1:
                cost += min(ctr_x[i][j], ctr_y[bit - i][j]) * X[j][2]
        ans[cnt] = min(ans[cnt], cost)

print(*ans, sep="\n")
