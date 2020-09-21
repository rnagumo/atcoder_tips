
N = input()
res = 0
for v in N:
    res += int(v)

if res % 9 == 0:
    print("Yes")
else:
    print("No")
