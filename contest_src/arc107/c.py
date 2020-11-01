class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        elif self.rank[x] < self.rank[y]:
            x, y = y, x

        self.par[y] = x
        self.size[x] += self.size[y]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]


N, K = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

MAX = 100
MOD = 998244353

fac = [0] * (MAX + 1)
fac[0] = 1
fac[1] = 1

for i in range(2, MAX + 1):
    fac[i] = fac[i - 1] * i % MOD

# Column
tree = UnionFind(N)
for i in range(N):
    for j in range(i + 1, N):
        if all(X[i][k] + X[j][k] <= K for k in range(N)):
            tree.unite(i, j)

res = 1
for i in range(N):
    if i == tree.find(i):
        res *= fac[tree.get_size(i)]
        res %= MOD

# Row
tree = UnionFind(N)
for i in range(N):
    for j in range(i + 1, N):
        if all(X[k][i] + X[k][j] <= K for k in range(N)):
            tree.unite(i, j)

for i in range(N):
    if i == tree.find(i):
        res *= fac[tree.get_size(i)]
        res %= MOD

print(res)
