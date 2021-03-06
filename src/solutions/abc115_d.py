
"""
https://atcoder.jp/contests/abc115/tasks/abc115_d

次のルールで文字列を生成した時，前からX文字の中に"P"は何個存在するか？

S_0 = "P"
S_{i+1} = "B" + S_i + "P" + S_i + "B"

現在の文字列の前からn文字目が，一つ前の文字列の前から何文字目に相当するかを計算すれば良い．
前準備として，全体の文字数{a}，"P"の個数{p}を求めておく．
これは再起的に単純に計算できる．

次に，現在の文字列の前からn文字目までの"P"の個数を，一つ前の文字列から計算する．
func(n, x)として，nをレベル，xを前からの文字数とする．
この時，xの値によって条件分岐ができる．

* n == 0: xが非正の時は0，そうでなければ1を返す．
* x <= 1 + a[n-1]: つまり，S_nの前半分の文字列のみに注目する場合．この時，最初に一文字追加
されている分を除いたx-1文字目までを求めたい．また，xが非正になった時もこの条件で良い．n==0に
なるまで再帰的に計算される．
* x > 1 + a[n-1]: この時，後ろ半分の文字列に着目したい．前半分の"P"の数は前処理によって
p[n-1]で求まっている．再帰関数はでは，S_{n-1}の文字数a[n-1]と，今回足した2文字分を除去
した文字数までの値を計算する．
"""

N, X = map(int, input().split())

a = [1] * (N + 1)
p = [1] * (N + 1)
for i in range(N):
    a[i + 1] = a[i] * 2 + 3
    p[i + 1] = p[i] * 2 + 1


def func(n, x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + a[n - 1]:
        return func(n - 1, x - 1)

    return p[n - 1] + 1 + func(n - 1, x - 2 - a[n - 1])


print(func(N, X))
