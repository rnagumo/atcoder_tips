
"""
https://atcoder.jp/contests/abc147/tasks/abc147_d

配列Aについて，(A[i] XOR A[j]) for all i < jを求める．

XORはビットごとに独立なので，それぞれのビットで和を計算する．
A[i]==A[j]のときA[i] XOR A[j] == 0, A[i]!=A[j]のときA[i] XOR A[j] == 1なので，
和はA[i]!=A[j]の組の数である．A[i]={0, 1}より，これは(#0 * #1)に等しい．
"""

N = int(input())
X = list(map(int, input().split()))

MOD = 10 ** 9 + 7
ans = 0
for b in range(61):
    ctr = [0, 0]
    for i in range(N):
        ctr[X[i] >> b & 1] += 1

    ans += (1 << b) * ctr[0] * ctr[1]
    ans %= MOD

print(ans)
