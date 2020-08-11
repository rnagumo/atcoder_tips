
"""
https://atcoder.jp/contests/diverta2019-2/tasks/diverta2019_2_c

{A_i}の数列に対して，「x, yを取り出してx-yに置き換える」と言う処理をN回施した時，最後に残る
整数の最大値とその処理手順を求める．

1. 全て正：最初と最後の値以外を引く．
2. 全て負：最初以外の値を全て引く．
3. 正負ゼロ：同様に，正の最大値以外は全て引き，負は全て引く．
"""

N = int(input())
X = list(map(int, input().split()))

pos = sorted([v for v in X if v >= 0])
neg = sorted([v for v in X if v < 0], reverse=True)

ans = []
if not neg:
    # neg is empty
    cnt = pos[0]
    for v in pos[1:-1]:
        ans.append((cnt, v))
        cnt -= v
    ans.append((pos[-1], cnt))
    print(pos[-1] - cnt)
elif not pos:
    # pos is empty
    cnt = neg[0]
    for v in neg[1:]:
        ans.append((cnt, v))
        cnt -= v
    print(cnt)
else:
    # neg and pos exist
    for v in pos[:-1]:
        ans.append((neg[0], v))
        neg[0] -= v

    cnt = pos[-1]
    for v in neg:
        ans.append((cnt, v))
        cnt -= v
    print(cnt)

for v in ans:
    print(*v)
