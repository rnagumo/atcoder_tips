
"""
https://atcoder.jp/contests/abc123/tasks/abc123_d

配列{A}, {B}, {C}の中から一つずつ要素を選ぶ時に，大きい方からK個を示す．

貪欲にするとO(N^3)かかるので，計算時間を減らしたい．

# 解法1

二つの配列の要素の和を全探索した後，もう一つの配列との和を求める．

1. {A}, {B}の和を求めてソートする: O(N^2 + N^2 log N^2)
2. 上述の上位K個と，{C}との和を求める: O(NK)
3. ソートして上位K個を求める: O(NK log NK)

```
res = []
for a in A:
    for b in B:
        res.append(a + b)

res.sort(reverse=True)

res2 = []
for v in res[:K]:
    for c in C:
        res2.append(v + c)

res2.sort(reverse=True)
for i in range(K):
    print(res2[i])
```

# 解法2

heapqを使って大きい順にK個を探索する．インデックスも同時に持たせることで，次の最大値候補を
計算できるようにする．計算量はO(N log N + K log K)

```
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

pq = []
heappush(pq, (-A[0] - B[0] - C[0], 0, 0, 0))
appeared = set((0, 0, 0))

for _ in range(K):
    # Pop maximum value
    val, i, j, k = heappop(pq)
    print(-val)

    # Add next value
    if i + 1 < X and (i + 1, j, k) not in appeared:
        heappush(pq, (-A[i + 1] - B[j] - C[k], i + 1, j, k))
        appeared.add((i + 1, j, k))

    if j + 1 < Y and (i, j + 1, k) not in appeared:
        heappush(pq, (-A[i] - B[j + 1] - C[k], i, j + 1, k))
        appeared.add((i, j + 1, k))

    if k + 1 < Z and (i, j, k + 1) not in appeared:
        heappush(pq, (-A[i] - B[j] - C[k + 1], i, j, k + 1))
        appeared.add((i, j, k + 1))
```

# 解法3

上からK番目に入り得る値のみを列挙して，ソートする．枝刈り全探索によってO(K^2)で求まる．

```
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

res = []
for i in range(X):
    for j in range(Y):
        for k in range(Z):
            if (i + 1) * (j + 1) * (k + 1) <= K:
                res.append(A[i] + B[j] + C[k])
            else:
                break

res.sort(reverse=True)
for i in range(K):
    print(res[i])
```
"""

from heapq import heappop, heappush


X, Y, Z, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

pq = []
heappush(pq, (-A[0] - B[0] - C[0], 0, 0, 0))
appeared = set((0, 0, 0))

for _ in range(K):
    # Pop maximum value
    val, i, j, k = heappop(pq)
    print(-val)

    # Add next value
    if i + 1 < X and (i + 1, j, k) not in appeared:
        heappush(pq, (-A[i + 1] - B[j] - C[k], i + 1, j, k))
        appeared.add((i + 1, j, k))

    if j + 1 < Y and (i, j + 1, k) not in appeared:
        heappush(pq, (-A[i] - B[j + 1] - C[k], i, j + 1, k))
        appeared.add((i, j + 1, k))

    if k + 1 < Z and (i, j, k + 1) not in appeared:
        heappush(pq, (-A[i] - B[j] - C[k + 1], i, j, k + 1))
        appeared.add((i, j, k + 1))
