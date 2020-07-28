
"""1 <= N <= 50, 1 <= K <= 100と小さいので全探索すれば良い．"""

from collections import deque

N, K = map(int, input().split())
X = list(map(int, input().split()))

ans = 0
for a in range(K + 1):
    for b in range(K + 1 - a):
        if a + b > N:
            continue

        q = deque(X)
        tmp = []
        for _ in range(a):
            tmp.append(q.popleft())

        for _ in range(b):
            tmp.append(q.pop())

        tmp.sort(reverse=True)
        cnt = 0
        for _ in range(K - a - b):
            if tmp and tmp[-1] < 0:
                tmp.pop()

        ans = max(ans, sum(tmp))

print(ans)
