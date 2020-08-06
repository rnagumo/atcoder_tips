
"""
https://atcoder.jp/contests/abc157/tasks/abc157_e

文字列Sに対して，以下の処理を順に行う．
1. l~rの文字の種類の数を答える
2. l文字目をcに変更する

BITを使って，各文字が何文字目にあるのかを保持する．
"""


class BIT:
    # 1-indexed
    def __init__(self, n):
        self.size = n + 1
        self.bit = [0] * self.size

    def add(self, i, x):
        # Add x to a[i]
        while i < self.size:
            self.bit[i] += x
            i += i & -i

    def sumup(self, i):
        # Sum a[1]~a[i]
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def query(self, i, j):
        # Sum a[i]~a[j]
        return self.sumup(j) - self.sumup(i - 1)


N = int(input())
S = list(input())
Q = int(input())
X = [input().split() for _ in range(Q)]

MAX = 5 * 10 ** 5 + 2
d = dict()
for c in range(ord("a"), ord("z") + 1):
    s = chr(c)
    d[s] = BIT(MAX)

for i, v in enumerate(S):
    d[v].add(i + 1, 1)

for q, *x in X:
    if q == "1":
        i = int(x[0])
        c = x[1]

        d[c].add(i, 1)
        d[S[i - 1]].add(i, -1)
        S[i - 1] = c
    else:
        l, r = map(int, x)

        ans = 0
        for c in range(ord("a"), ord("z") + 1):
            ans += int(d[chr(c)].query(l, r) > 0)
        print(ans)
