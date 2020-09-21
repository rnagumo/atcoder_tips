
"""
https://atcoder.jp/contests/abc119/tasks/abc119_d

無限遠の点を付与することで，二分探索の実装が楽になる．
あとは，とり得る通過点の組み合わせ4通りを全て試し，最も値の小さいものを取得する．
"""

from bisect import bisect_right

A, B, Q = map(int, input().split())
INF = 10 ** 18
S = [-INF] + [int(input()) for _ in range(A)] + [INF]
T = [-INF] + [int(input()) for _ in range(B)] + [INF]
X = [int(input()) for _ in range(Q)]

for x in X:
    b = bisect_right(S, x)
    d = bisect_right(T, x)
    res = INF
    for s in [S[b - 1], S[b]]:
        for t in [T[d - 1], T[d]]:
            dist_0 = abs(x - s) + abs(s - t)
            dist_1 = abs(x - t) + abs(t - s)
            res = min(res, dist_0, dist_1)

    print(res)
