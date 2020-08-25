
"""
https://atcoder.jp/contests/abc120/tasks/abc120_d

グラフのエッジを一つずつ減らした時に，繋がっていないノードの組みの数を求めよ．

いくつかの事実に気づく必要がある．
* ノードが互いに連結かを調べるにはUnionFindを使えば良いが，エッジの削除には対応していない．
* エッジを減らすのではなく，逆から増やしていくという考えをとる．
* 元々連結の場合にはノードの組の数は変わらず，連結でない場合には互いのノードの集合同士が
  つながる．
"""


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


N, M = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(M)]

tree = UnionFind(N + 1)
res = [N * (N - 1) // 2]
for a, b in reversed(X[1:]):
    if not tree.is_same(a, b):
        num0 = tree.get_size(a)
        num1 = tree.get_size(b)
        res.append(res[-1] - num0 * num1)
    else:
        res.append(res[-1])
    tree.unite(a, b)

print(*res[::-1], sep="\n")
