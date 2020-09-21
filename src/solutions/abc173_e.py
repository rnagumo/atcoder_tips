
"""
https://atcoder.jp/contests/abc173/tasks/abc173_e

長さNの数列{A_i}の中からK個の要素を選ぶ時，その積の最大値を求める．

全ての要素が負の場合には，絶対値を小さくするように選ぶ．

全ての要素を選ぶ時(K==N)，全てを選ぶ．

それ以外の時には，要素の積は非負となるので，絶対値を大きくするように選ぶ．
pos, negから，2個ずつの積を取り出し，大きい方からK//2個を採択する．
ここで，pos, negにそれぞれ最大1個の要素が残り得るが，K<Nなので問題ない．
"""

N, K = map(int, input().split())
X = list(map(int, input().split()))

MOD = 10 ** 9 + 7

if K % 2 == 1 and all(v < 0 for v in X):
    # Minimize abs
    X.sort(key=lambda x: -x)
    ans = 1
    for i in range(K):
        ans = ans * X[i] % MOD
    print(ans)
elif K == N:
    # Select all
    ans = 1
    for i in range(K):
        ans = ans * X[i] % MOD
    print(ans)
else:
    # Select K elements to maximize their product
    pos = sorted(v for v in X if v >= 0)
    neg = sorted(-v for v in X if v < 0)

    ans = 1
    if K % 2 == 1:
        ans *= pos.pop()

    cand = []
    while len(pos) >= 2:
        tmp = pos.pop() * pos.pop()
        cand.append(tmp)

    while len(neg) >= 2:
        tmp = neg.pop() * neg.pop()
        cand.append(tmp)

    cand.sort(reverse=True)
    for i in range(K // 2):
        ans = ans * cand[i] % MOD

    print(ans)
