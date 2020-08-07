
"""
https://atcoder.jp/contests/abc167/tasks/abc167_f


'(', ')'の括弧列N個を，正しい括弧列として結合できるかを判定する．

'('=+1, ')'=-1として，負にならなず，かつ最後が0になるように結合する．
部分文字列の末尾が正のものを最初に結合し，後から負のものを結合する．
ctrには両者を分けて保存する．

次に，上昇分は前から，下降分は後ろから結合することを考える．
それぞれ上昇幅の大きいものから貪欲に結合するとよい．現時点から途中で負にならないかを確認
しつつ，最終的な上昇分を加算していく．

下降分まで計算し終わった後で，両者の最終到達点が等しいことを確認する．
"""

N = int(input())
X = [input() for _ in range(N)]

ctr = [[], []]
for s in X:
    t = [0] * (len(s) + 1)
    for j in range(len(s)):
        t[j + 1] = t[j] + int(s[j] == "(") - int(s[j] == ")")

    if t[-1] > 0:
        ctr[0].append((min(t), t[-1]))
    else:
        ctr[1].append((min(t) - t[-1], -t[-1]))

flag = True
tmp = 0
for i in range(2):
    cur = 0
    for m, c in sorted(ctr[i], reverse=True):
        flag &= cur + m >= 0
        cur += c

    if i == 0:
        tmp = cur
    else:
        flag &= tmp == cur

if flag:
    print("Yes")
else:
    print("No")
