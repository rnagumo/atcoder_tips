
"""
https://atcoder.jp/contests/abc119/tasks/abc119_c

長さNの配列のそれぞれの要素に対して「使わない，Aに加算, Bに加算, Cに加算」としたときの，
全ての場合の最小値を求める．
計算量はO(4^N)．
"""

N, A, B, C = map(int, input().split())
X = [int(input()) for _ in range(N)]


def dfs(idx, a, b, c, cnt):
    if idx == N:
        if min(a, b, c) > 0:
            return abs(a - A) + abs(b - B) + abs(c - C) + cnt - 30
        else:
            return 10 ** 9

    res = 10 ** 9
    res = min(res, dfs(idx + 1, a, b, c, cnt))
    res = min(res, dfs(idx + 1, a + X[idx], b, c, cnt + 10))
    res = min(res, dfs(idx + 1, a, b + X[idx], c, cnt + 10))
    res = min(res, dfs(idx + 1, a, b, c + X[idx], cnt + 10))
    return res


print(dfs(0, 0, 0, 0, 0))
