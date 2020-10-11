
H, W = map(int, input().split())
X = [input() for _ in range(H)]

res = 0
visited = [[False] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if X[i][j] == "#":
            continue

        if j < W - 1 and X[i][j + 1] == ".":
            res += 1
        if i < H - 1 and X[i + 1][j] == ".":
            res += 1

print(res)
