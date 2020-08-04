
"""
https://atcoder.jp/contests/abc174/tasks/abc174_f
参考: https://atcoder.jp/contests/abc174/submissions/15614919

配列Cの中で，ある区間[l, r]にある数の種類を答える．

二つのデータ構造を使って情報を管理する．
* last_appeared: 各種類の数の，一番右に出現したインデックス
* bit: 一番右の数である種類の数

クエリの右端の昇順にソートする．Q個のクエリに対して，尺取り法の要領で配列を見ていくことで，
定数オーダーで走査できる．
"""


class BIT:
    # 1-indexed
    def __init__(self, n):
        self.size = n + 1
        self.bit = [0] * self.size

    def add(self, i, x):
        """Add x to a[i]."""
        while i < self.size:
            self.bit[i] += x
            i += i & -i

    def sumup(self, i):
        """Sum a[1]~a[i]."""
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def query(self, i, j):
        """Sum a[i]~a[j]."""
        return self.sumup(j) - self.sumup(i - 1)


N, Q = map(int, input().split())
C = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(Q)]

ans = [0] * Q
last_appeared = [0] * (N + 1)
bit = BIT(N + 1)
rm = 0
for i, (l, r) in sorted(enumerate(X), key=lambda x: x[1][1]):
    # 新しくrm~rの区間が追加されるので，そこに出てくる数の右端情報を更新する
    for j in range(rm + 1, r + 1):
        # 位置j-1にある石が既に出てきている場合には，bit(一番右である数の種類数)から引く
        if last_appeared[C[j - 1]] > 0:
            bit.add(last_appeared[C[j - 1]], -1)

        # 新しい「一番右端のインデックス」
        last_appeared[C[j - 1]] = j
        bit.add(j, 1)

    # 尺取り法の左端
    rm = r

    # クエリに答える
    ans[i] = bit.query(l, r)

print(*ans, sep="\n")
