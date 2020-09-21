
"""
https://atcoder.jp/contests/abc155/tasks/abc155_d

整数列のペアの積の，小さい方からK番目の数を求める．

積が負，ゼロ，正になる場合それぞれに分けて，二分探索．
積がある値midより小さいペアの数は，大きい方から尺取り法を使えばO(N)で求められる．
"""

N, K = map(int, input().split())
X = list(map(int, input().split()))

neg = sorted(-v for v in X if v < 0)
pos = sorted(v for v in X if v > 0)
nonneg = sorted(v for v in X if v >= 0)

cnt_neg = len(neg)
cnt_pos = len(pos)

pair_pos = cnt_pos * (cnt_pos - 1) // 2 + cnt_neg * (cnt_neg - 1) // 2
pair_neg = cnt_pos * cnt_neg
pair_zro = N * (N - 1) // 2 - pair_pos - pair_neg

if pair_neg >= K:
    # Negative
    ub = 10 ** 18 + 1
    lb = 0
    while ub - lb > 1:
        mid = (ub + lb) // 2

        # Count
        cnt = 0
        j = 0
        for v in reversed(neg):
            while j < cnt_pos and v * pos[j] < mid:
                j += 1
            cnt += cnt_pos - j

        if cnt < K:
            ub = mid
        else:
            lb = mid

    print(-lb)
elif pair_neg + pair_zro >= K:
    print(0)
else:
    # Non-negative
    ub = 10 ** 18 + 1
    lb = 0
    while ub - lb > 1:
        mid = (ub + lb) // 2
        cnt = 0

        # Negative count
        j = 0
        for v in reversed(neg):
            if v ** 2 <= mid:
                cnt -= 1
            while j < cnt_neg and v * neg[j] < mid:
                j += 1
            cnt += j

        # Positive count
        j = 0
        for v in reversed(pos):
            if v ** 2 <= mid:
                cnt -= 1
            while j < cnt_pos and v * pos[j] < mid:
                j += 1
            cnt += j

        # Remove duplicate
        cnt //= 2

        if cnt + pair_neg + pair_zro < K:
            lb = mid
        else:
            ub = mid

    print(lb)
