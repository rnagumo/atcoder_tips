
X, K, D = map(int, input().split())

n = abs(X) // D
if n <= K:
    if X >= 0:
        res = X - D * n
        if (K - n) % 2 == 1:
            print(abs(res - D))
        else:
            print(res)
    else:
        res = X + D * n
        if (K - n) % 2 == 1:
            print(abs(res + D))
        else:
            print(abs(res))
else:
    if X >= 0:
        res = X - D * K
    else:
        res = X + D * K
    print(abs(res))
