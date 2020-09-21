
"""
https://atcoder.jp/contests/abc138/tasks/abc138_e

文字列Sの繰り返しの中から，文字列Tを生成するときの最小長を求める．
Sの各文字のインデックスのリストを作り，Tの各文字について最小のインデックスを求める．
現在のインデックスより後ろに次の文字のインデックスがない場合には，
次の繰り返しの先頭のインデックスを使うことになる．よって，繰り返し回数がインクリメントされる．

計算量は，最悪でもO(len(T) log len(S))．
"""

from collections import defaultdict
from bisect import bisect_right

S = input()
T = input()

ctr = defaultdict(list)
for i, s in enumerate(S):
    ctr[s].append(i)

i = -1
cnt = 0
flag = False
for t in T:
    if t not in ctr:
        flag = True
        break

    j = bisect_right(ctr[t], i)
    if j == len(ctr[t]):
        idx = ctr[t][0]
    else:
        idx = ctr[t][j]

    if i >= idx:
        cnt += 1
    i = idx

if flag:
    print(-1)
else:
    print(cnt * len(S) + i + 1)
