
"""
https://atcoder.jp/contests/abc172/tasks/abc172_d

正の整数xに対し，その約数の個数をf(x)とする．
この時，sum_1^N (n*f(n))を求める．

最初に考えたのがこちらの解放．
Nまでの各数の約数を求めることは，各数の倍数を求めることに等しい．
よって，ある数の倍数のカウントを順に+1していけばよい．
ただし，この解放の計算量はたぶんO(N logN)なのでかなりギリギリ．
```
ctr = [1] * (N + 1)
for n in range(2, N + 1):
    for v in range(n, N + 1, n):
        ctr[v] += 1

ans = 0
for n in range(1, N + 1):
    ans += n * ctr[n]
print(ans)
```

実は，カウントを数えて後で和を取らなくてもよい．
ある数xについて，Nまでの自身の倍数の和は，等比数列の和を用いてO(1)で求まる．
x + 2x + 3x + ... + mx = m(m - 1)/2 * x
こうすれば，カウントを保持せずとも和を計算でき，計算量はO(N)となる．
"""

N = int(input())

ans = 0
for n in range(1, N + 1):
    m = N // n
    ans += m * (m + 1) // 2 * n
print(ans)
