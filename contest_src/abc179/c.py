
N = int(input())

ans = 0
for a in range(1, 10 ** 6 + 1):
    for b in range(1, 10 ** 6 + 1):
        if a * b >= N:
            break
        ans += 1

print(ans)
