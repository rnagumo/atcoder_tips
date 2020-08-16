
N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

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
