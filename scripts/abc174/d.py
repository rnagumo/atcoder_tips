
N = int(input())
S = list(input())

cnt = S.count("R")
ans = S[cnt:].count("R")
print(ans)
