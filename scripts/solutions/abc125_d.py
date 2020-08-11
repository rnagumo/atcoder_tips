
"""
https://atcoder.jp/contests/abc125/tasks/abc125_d

配列{X}に対して，隣合う数に-1を掛ける操作を繰り返した時の，和の最大値．


"""

N = int(input())
X = list(map(int, input().split()))

y = [abs(v) for v in X]
if sum(v < 0 for v in X) % 2 == 0:
    print(sum(y))
else:
    print(sum(y) - 2 * min(y))
