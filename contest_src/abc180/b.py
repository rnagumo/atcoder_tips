
N = int(input())
X = list(map(int, input().split()))

print(sum(map(lambda x: abs(x), X)))
print(sum(map(lambda x: x ** 2, X)) ** 0.5)
print(max(map(lambda x: abs(x), X)))
