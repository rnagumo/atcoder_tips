
N = int(input())
X = list(map(int, input().split()))

appeared = [False] * 200_010
res = 0
for v in X:
    appeared[v] = True
    if res == v:
        while appeared[res]:
            res += 1

    print(res)
