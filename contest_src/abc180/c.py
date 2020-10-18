
def calc_divisor(x):
    # O(sqrt(N))
    divisor = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            divisor.append(i)
            if i != x // i:
                divisor.append(x // i)
    return divisor


N = int(input())
print(*sorted(calc_divisor(N)), sep="\n")
