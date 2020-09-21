
"""
https://atcoder.jp/contests/abc117/tasks/abc117_d

配列{A}が与えられた時，0~Kまでの整数xに対して，以下のf(x)の最大値を求める．
f(x) = (x^A[0]) + ... + (x^A[N])

XORの計算の性質上，各bitは独立に計算できる．
Kより小さいという制約を外した時，f(x)を大きくするには，各桁で1の数を多くすれば良い．
XORを使えば，0/1を反転することができるので，各桁の1の数を多くしたときの最大量は
max(# of 0, # of 1)となる．
よって，まずは1となるビットの数を数える．

次に，各桁についてKより小さいという制約なしの時の和の最大値は以下で求められる．
sum_i {max(# of 0, # of 1) * 2**i}
これを下の桁から加算する．

Kより小さい数xは，ある桁iにおいてK_i==1のときx_i==0となる．
そして，その桁より下はどのような数であってもK以下の制約を満たす．
よって，ある桁iについてx_i==0となるときf(x)の値は以下で求められ，この最大値を求めれば良い．
tmp_i = (上位桁はKと同じ) + (その桁は0) + (下位桁は任意)

ここで，cntの計算だが，K_i==1のときはビットが反転するのでビットの数は(# of 0)，
K_i==0のときは(# of 1)となる点に注意する．これを，上位桁から順に足していけば良い．

余談だが，ビットシフトの優先順位は加減算よりも低い点に注意する．
"""

N, K = map(int, input().split())
X = list(map(int, input().split()))

# Calculate numbers of bits 1
bits = [0] * 40
for k in range(40):
    for v in X:
        bits[k] += v >> k & 1

# Take larger # of bits
ctr = [0] * 41
for k in range(40):
    ctr[k + 1] = ctr[k] + (max(N - bits[k], bits[k]) << k)

res = 0
cnt = 0
for i in reversed(range(40)):
    if K >> i & 1:
        res = max(res, cnt + (bits[i] << i) + ctr[i])
        cnt += (N - bits[i]) << i
    else:
        cnt += bits[i] << i

print(max(res, cnt))
