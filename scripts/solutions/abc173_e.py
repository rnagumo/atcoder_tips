
N, K = map(int, input().split())
X = list(map(int, input().split()))
MOD = 10 ** 9 + 7

pos = sorted(v for v in X if v >= 0)
neg = sorted(-v for v in X if v < 0)

ok = False  # True: ans>=0, False: ans<0
if pos:
    if N == K:
        # Select all -> number of negatives must be even
        ok = len(neg) % 2 == 0
    else:
        ok = True
else:
    # All negative and even number is selected
    ok = K % 2 == 0

ans = 1
if ok:
    # ans >= 0
    if K % 2 == 1:
        ans = ans * pos.pop() % MOD

    # 答えは正になる→二つの数の積は必ず正になる．
    cand = []
    while len(pos) >= 2:
        x = pos.pop() * pos.pop()
        cand.append(x)

    while len(neg) >= 2:
        x = neg.pop() * neg.pop()
        cand.append(x)

    cand.sort(reverse=True)
    for i in range(K // 2):
        ans = ans * cand[i] % MOD
else:
    # ans <= 0
    cand = sorted(X, key=lambda x: abs(x))
    for i in range(K):
        ans = ans * cand[i] % MOD

print(ans)
