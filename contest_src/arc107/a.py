
def func(x, MOD=998244353):
    return x * (x + 1) // 2 % MOD


A, B, C = map(int, input().split())
MOD = 998244353

print(func(A) * func(B) * func(C) % MOD)
