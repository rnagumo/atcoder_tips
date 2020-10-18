
X, Y, A, B = map(int, input().split())

res = 0
while X < Y and (A - 1) * X < B:
    X *= A
    res += 1

if X >= Y:
    print(res - 1)
else:
    print(res + (Y - X - 1) // B)
