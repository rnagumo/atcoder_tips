
"""
https://atcoder.jp/contests/abc111/tasks/arc103_a

奇数要素，偶数要素それぞれで一つの数に統一する時に，書き換える要素の最小数を求める．ただし，
奇数・偶数はそれぞれ別の要素に書き換える．

奇数，偶数それぞれの最頻値を求めて，それ以外を書き換えれば良い．ただし，両者の最頻値が同じ
場合には，片方は二番目の最頻値に置き換える必要がある．それぞれの場合を求めて小さい方を求めれば
良い．アイデアは簡単だが，実装を簡潔に保つのが難しい．
"""

from collections import Counter

N = int(input())
X = list(map(int, input().split()))

evens = Counter(X[::2]).most_common()
odds = Counter(X[1::2]).most_common()

evens.append((0, 0))
odds.append((0, 0))

if evens[0][0] != odds[0][0]:
    print(N - evens[0][1] - odds[0][1])
else:
    print(min(N - evens[0][1] - odds[1][1], N - evens[1][1] - odds[0][1]))
