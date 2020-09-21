S = input()

cnt = 0
for i in range(3):
    if S[i] == "R":
        cnt += 1

    if cnt > 0 and S[i] == "S":
        break

print(cnt)
