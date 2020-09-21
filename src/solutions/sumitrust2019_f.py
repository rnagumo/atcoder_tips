
"""
https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_f

時間t1, t2で以下の速さで点が移動する．交差する回数を数える．
点A: a1, a2
点B: b1, b2

各時間での移動距離の差d1, d2をみる．d1 < 0を仮定する．
1. d1==d2: 時間t1+t2で同じ位置にいるので，無限回交差する．
2. d1+d2<0: 一度の移動で交差できないので，一度も交差しない．
3. d1+d2>0: 最初の移動量d1に対して，d1+d2の分だけ少しずつ差が開いていく．
    t1, t2で一回ずつ，計2回交差する．ただし，最初だけ1回である．
    また，最後にちょうど一度交差する場合も考慮する．
"""

t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

d1 = t1 * (a1 - b1)
d2 = t2 * (a2 - b2)

if d1 > 0:
    d1 *= -1
    d2 *= -1

if d1 + d2 == 0:
    print("infinity")
elif d1 + d2 < 0:
    print(0)
else:
    cnt = -d1 // (d1 + d2)
    t = -d1 % (d1 + d2)
    ans = 2 * cnt + int(t != 0)
    print(ans)
