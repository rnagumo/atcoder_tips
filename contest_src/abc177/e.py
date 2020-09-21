
from math import gcd
from functools import reduce
from collections import defaultdict


def calc_factor(n):
    # O(N log log N)
    min_factor = list(range(n + 1))
    for i in range(2, n + 1):
        if min_factor[i] == i:
            for j in range(2 * i, n + 1, i):
                min_factor[j] = i
    return min_factor


def calc_prime_factor(n, min_factor):
    # O(log N)
    ctr = defaultdict(int)
    while n > 1:
        div = min_factor[n]
        while n % div == 0:
            ctr[div] += 1
            n //= div
    return ctr


N = int(input())
X = list(map(int, input().split()))

min_factor = calc_factor(10 ** 6 + 10)
pairwise = True
appeared = set()
for v in X:
    primes = calc_prime_factor(v, min_factor)
    for n in primes:
        if n in appeared:
            pairwise = False
        appeared.add(n)

if pairwise:
    print("pairwise coprime")
elif reduce(gcd, X) == 1:
    print("setwise coprime")
else:
    print("not coprime")
