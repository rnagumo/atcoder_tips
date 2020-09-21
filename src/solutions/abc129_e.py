
"""
桁DPの問題

num: 今より上の桁の`1`の数 ((0, 1), (1, 0)の2通り)
length: 残りの桁数 ((0, 1), (1, 0), (0, 0)の3通り)
"""

L = input()
MOD = 10 ** 9 + 7

res = 0
num = 0
n = len(L)
for i in range(n):
    length = n - i - 1
    if L[i] == "1":
        res = (res + pow(2, num, MOD) * pow(3, length, MOD))
        num += 1

res = (res + pow(2, num, MOD)) % MOD
print(res)
