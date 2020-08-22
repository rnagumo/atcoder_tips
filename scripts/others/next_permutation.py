
"""
https://leetcode.com/problems/next-permutation/

次のpermutationを求める．
1, 2, 3 -> 1, 3, 2
5, 9, 1, 4, 3 -> 5, 9, 3, 1, 4

最初は昇順，ある位置でおかしな値をとり，次は降順になる．
"""

nums = list(map(int, input().split()))

i = len(nums) - 2
while i >= 0 and nums[i] >= nums[i + 1]:
    i -= 1

if i >= 0:
    j = len(nums) - 1
    while j >= 0 and nums[j] <= nums[i]:
        j -= 1
    nums[i], nums[j] = nums[j], nums[i]

start = i + 1
end = len(nums) - 1
while start < end:
    nums[start], nums[end] = nums[end], nums[start]
    start += 1
    end -= 1

print(nums)
