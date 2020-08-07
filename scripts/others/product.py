
"""
https://www.geeksforgeeks.org/product-of-all-subarrays-of-an-array/

Product of all Subarrays of an Array

Input: arr[] = {2, 4}
Output: 64
    Here, subarrays are [2], [2, 4], [4]
    Prodcuts are 2, 8, 4
    Product of all Subarrays = 64

Input : arr[] = {10, 3, 7}
Output : 30870
    Here, subarrays are [10], [10, 3], [10, 3, 7], [3], [3, 7], [7]
    Prodcuts are 10, 30, 210, 3, 21, 7
    Product of all Subarrays = 27783000
"""

X = list(map(int, input().split()))
n = len(X)


def solution_n3(x, n):
    ans = 1
    for i in range(n):
        for j in range(i, n):
            for k in range(i, j + 1):
                ans *= x[k]
    return ans


def solution_n2(x, n):
    res = 1
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= x[j]
            res *= prod
    return res


print(solution_n3(X, n))
print(solution_n2(X, n))
