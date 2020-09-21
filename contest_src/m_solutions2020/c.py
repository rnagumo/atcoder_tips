
from collections import deque

N, K = map(int, input().split())
X = list(map(int, input().split()))

q = deque(X[:K])
for i in range(K, N):
    u = q.popleft()
    if u < X[i]:
        print("Yes")
    else:
        print("No")
    q.append(X[i])
