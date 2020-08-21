
"""
https://drken1215.hatenablog.com/entry/2020/08/17/182700

```
ans = []
for u in range(N):
    v = P[u] - 1
    cnt = C[v]
    val = cnt
    jump = 1

    # Jump to limit or loop
    while v != u and jump < K:
        v = P[v] - 1
        cnt += C[v]
        val = max(val, cnt)
        jump += 1

    # Reduce residual to < K
    if jump < K:
        res = max(0, K // jump - 2)
        cnt += cnt * res
        val = max(val, cnt)
        jump += jump * res

    # Residual steps
    while jump < K:
        v = P[v] - 1
        cnt += C[v]
        val = max(val, cnt)
        jump += 1

    ans.append(val)

print(max(ans))
```
"""

N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

lim = 60
nex = [[0] * N for _ in range(lim)]
val = [[0] * N for _ in range(lim)]
cnd = [[0] * N for _ in range(lim)]

for i in range(N):
    nex[0][i] = P[i] - 1
    val[0][i] = C[i]
    cnd[0][i] = C[i]

for d in range(lim - 1):
    for i in range(N):
        nex[d + 1][i] = nex[d][nex[d][i]]
        val[d + 1][i] = val[d][i] + val[d][nex[d][i]]
        cnd[d + 1][i] = max(cnd[d][i], val[d][i] + cnd[d][nex[d][i]])

res = -10 ** 9
for i in range(N):
    sum_ = 0
    offset = i
    for d in reversed(range(lim)):
        if K & 1 << d:
            res = max(res, sum_ + cnd[d][offset])
            sum_ += val[d][offset]
            offset = nex[d][offset]

print(res)
