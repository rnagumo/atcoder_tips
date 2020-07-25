
from heapq import heappush, heappop

N, Q = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
Y = [list(map(int, input().split())) for _ in range(Q)]

MAX = 200001
hs = [[] for _ in range(MAX)]
gh = []
for i, (a, b) in enumerate(X):
    heappush(hs[b], (-a, i))  # (value, index)

for i in range(MAX):
    if hs[i]:
        heappush(gh, (-hs[i][0][0], hs[i][0][1], i))  # (value, index, place)

# Query
for c, d in Y:
    c -= 1
    old = X[c][1]

    # Insert new
    X[c][1] = d
    heappush(hs[d], (-X[c][0], c))
    heappush(gh, (-hs[d][0][0], hs[d][0][1], d))

    # Remove old
    # `old`リストを見るので，今回指定されたもの以外は`X[item[1]][1] == old`となる．
    # よって，`X[item[1]][1] != old`を見つけてくれば良い．
    while hs[old]:
        item = hs[old][0]
        if X[item[1]][1] != old:
            heappop(hs[old])
        else:
            break

    # まだ要素が残っている場合には，新しい`max`候補を`gh`に加える．
    if hs[old]:
        heappush(gh, (-hs[old][0][0], hs[old][0][1], old))

    # Print
    while True:
        mn = gh[0]  # mn = (value, index, place)

        # 以下の場合には，前の操作で変更されており正しい候補ではないので除外する
        # 1. 場所が変更されている場合
        # 2. その場所での最上位ではない
        if X[mn[1]][1] != mn[2] or hs[mn[2]][0][1] != mn[1]:
            heappop(gh)  # 現在の最上位アイテムを削除
            while hs[mn[2]]:
                item = hs[mn[2]][0]  # その場所のアイテムを持ってくる
                if X[item[1]][1] != mn[2]:
                    heappop(hs[mn[2]])  # 変更されているアイテムなので削除する
                else:
                    break

            # その場所の新しい候補を追加する
            if hs[mn[2]]:
                heappush(gh, (-hs[mn[2]][0][0], hs[mn[2]][0][1], mn[2]))
        else:
            break

    print(gh[0][0])
