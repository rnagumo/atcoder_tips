
S = input()
T = input()

n = len(S)
m = len(T)
res = n + 1
for i in range(n - m + 1):
    cnt = 0
    for j in range(m):
        cnt += int(S[i + j] != T[j])
    res = min(res, cnt)

print(res)
