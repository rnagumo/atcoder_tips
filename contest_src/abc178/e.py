
N = int(input())
X = [list(map(int, input().split())) for _ in range(N)]

z = [x + y for x, y in X]
w = [x - y for x, y in X]

print(max(max(z) - min(z), max(w) - min(w)))
