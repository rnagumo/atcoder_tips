
"""
https://atcoder.jp/contests/nomura2020/tasks/nomura2020_c

i段目の葉の数がX[i]であるような二分木の，ノードの数の和を求める．

ある段のノード数から葉の数を引いた2倍までが，次の段のノード数の上限である．
あとは，上限と実際のノード数の小さい方を足していけばよい．
"""

N = int(input())
X = list(map(int, input().split()))

# Upper limit
cnt = [0] * (N + 1)
cnt[0] = 1
for i in range(N):
    cnt[i + 1] = (cnt[i] - X[i]) * 2

if all(cnt[i] >= X[i] for i in range(N + 1)):
    ans = 0
    cur = 0
    for i in reversed(range(N + 1)):
        cur += X[i]
        ans += min(cnt[i], cur)
    print(ans)
else:
    print(-1)
