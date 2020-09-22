
N = int(input())
X = [list(map(int, input().split())) for _ in range(N)]

ok = False
for i in range(N - 2):
    ok |= ((X[i][0] == X[i][1]) and ((X[i + 1][0] == X[i + 1][1]))
           and (X[i + 2][0] == X[i + 2][1]))

if ok:
    print("Yes")
else:
    print("No")
