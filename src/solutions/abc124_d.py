
"""
https://atcoder.jp/contests/abc124/tasks/abc124_d

0, 1からなる文字列のうち，K回まで連続した0を1に変換できる．この時，連続して並ぶ1の最大値は
幾つか．

まず，連続している部分は圧縮できるので，その変わり目のみを抜き出す．
次に，0の塊を連続して反転する．なぜならば，連続して反転した方が答えは大きくなるから．
よって，i~i+K番目の塊を反転する．

ここで，各塊の値に注意する．
S[i]=0: 0, 1, 0, ..., 1なので，j=i+2K番目までの和をとる．
S[i]=1: 1, 0, 1, 0, ..., 1なので，j=i+2K+1番目までの和をとる．

この点を注意し，配列の最後もしくはj番目までの和をとり，最大値を求める．
"""

N, K = map(int, input().split())
S = input()

q = [(S[0], 0)]
cur = S[0]
for i in range(1, N):
    if S[i] != cur:
        q.append((S[i], i))
        cur = S[i]

lim = len(q)
ans = []
for i in range(lim):
    if q[i][0] == "0":
        j = i + 2 * K
    else:
        j = i + 2 * K + 1

    if j < lim:
        ans.append(q[j][1] - q[i][1])
    else:
        ans.append(N - q[i][1])

print(max(ans))
