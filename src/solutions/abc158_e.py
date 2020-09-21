
"""
https://atcoder.jp/contests/abc158/tasks/abc158_e

文字列Sの部分列で，ある素数Pで割り切れるものの個数．

P == 2or5: 最後の一桁が割り切れるかで，全体が割り切れるかが決まる．よって，割り切れる数を
探して，それを右端とする部分列は全て割り切れる．

P == else: このとき，10とPは互いに素である．N[i]=i文字目より右側の部分列とすると，S[i:j]
がPで割り切れるかは，N[i]==N[j] mod Pであるかに依存する．よって，同じmodの組みの数を
求めればよい．
"""

from collections import defaultdict

N, P = map(int, input().split())
S = input()

if P == 2 or P == 5:
    ans = 0
    for i in range(N):
        if int(S[i]) % P == 0:
            ans += i + 1
    print(ans)
else:
    ctr = defaultdict(int)
    ctr[0] = 1
    cur = 0
    for i in reversed(range(N)):
        cur = (cur + int(S[i]) * pow(10, N - i - 1, P)) % P
        ctr[cur] += 1

    ans = 0
    for v in ctr.values():
        ans += v * (v - 1) // 2
    print(ans)
