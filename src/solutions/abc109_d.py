
"""
https://atcoder.jp/contests/abc109/tasks/abc109_d

二次元のマスに書かれている数を1のみ増減する．一つのマスは一度しか選べず，そのマスを-1して
上下左右のマスのどれかを+1する．そうして，偶数のマスの数を最大化する．

マスを一筆書きして，奇数の1をずっと繰り越していく．先にインデックスのリストを作っておくと
実装量が減る．
"""

H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]

ans = []
idx_list = [(i, j) if i % 2 == 0 else (i, W - j - 1)
            for i in range(H) for j in range(W)]
for i, (u, v) in enumerate(idx_list[:-1]):
    if X[u][v] % 2 == 1:
        x, y = idx_list[i + 1]
        X[x][y] += 1
        ans.append((u + 1, v + 1, x + 1, y + 1))

print(len(ans))
for t in ans:
    print(*t)
