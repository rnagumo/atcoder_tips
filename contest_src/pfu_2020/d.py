
T = int(input())
MOD = 10 ** 9 + 7

for _ in range(T):
    N, A, B = map(int, input().split())

    if N - A - B >= 0:
        x_4 = (N - A - B + 2) * (N - A - B + 1) // 2
    else:
        x_4 = 0
    
    x_3 = x_4 * 2
    x_2 = (N - A + 1) * (N - B + 1) - x_3
    x_1 = x_2 ** 2 % MOD
    ans = (N - A + 1) ** 2 * (N - B + 1) ** 2 - x_1
    print(ans % MOD)
