
"""
https://atcoder.jp/contests/abc121/tasks/abc121_d

A^(A+1)^...^Bを求めよ．

XORに関する二つの性質に気づく必要がある．

1. 同じ数字同士の排他的論理和は0になる: n^n = 0

この考え方を用いると，ある範囲の累積の排他的論理和は，累積和と同じ考え方で計算できる．
つまり，A^(A+1)^...^B = {0^1^...^(A-1)} ^ {0^1^...^B}

2. 偶数nとして，n^(n + 1)=1

偶数では最終ビットが0になるので，次の奇数は最終ビットに1が足されたものになる．
よって，両者の排他的論理和をとると，最終ビットの1のみが現れる．
この性質を使うと，以下のように累積の排他的論理和が計算される．

ex1)
0^1^2^3^4^5^6
= (0^1) ^ (2^3) ^ (4^5) ^ 6
= 1^1^1^6
= 1^6

ex2)
0^1^2^3^4^5^6^7
= (0^1) ^ (2^3) ^ (4^5) ^ (6^7)
= 1^1^1^1
= 0
"""

A, B = map(int, input().split())


def func(n):
    res = 0 if ((n + 1) // 2) % 2 == 0 else 1
    res ^= n if n % 2 == 0 else 0
    return res


print(func(B) ^ func(A - 1))
