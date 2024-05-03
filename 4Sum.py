# Given
# an
# array
# nums
# of
# n
# integers,
# return an
# array
# of
# all
# the
# unique
# quadruplets[nums[a], nums[b], nums[c], nums[d]]
# such
# that:
#
# 0 <= a, b, c, d < n
# a, b, c, and d
# are
# distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You
# may
# return the
# answer in any
# order.
#
# Example
# 1:
#
# Input: nums = [1, 0, -1, 0, -2, 2], target = 0
# Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
# Example
# 2:
#
# Input: nums = [2, 2, 2, 2, 2], target = 8
# Output: [[2, 2, 2, 2]]
#
# Constraints:
#
# 1 <= nums.length <= 200
# -109 <= nums[i] <= 109
# -109 <= target <= 109

def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    nums.sort()
    myset = set()
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1,n):
                    if nums[i]+nums[j]+nums[k]+nums[l] == target:
                        myset.add((nums[i], nums[j], nums[k], nums[l]))

    out = []
    for x in myset:
        out.append(list(x))
    return out


#use 3 sum
def fourSum2(nums, target):
    n = len(nums)
    myset = set()
    nums.sort()
    for i in range(n):
        for j in range(i+1,n):
            l = j+1
            r = n-1
            t = target - nums[i] - nums[j]
            while l < r:
                sum = nums[l] + nums[r]
                if sum < t :
                    l += 1
                elif sum > t :
                    r -= 1
                else :
                    myset.add((nums[i], nums[j], nums[l], nums[r]))
                    l += 1
                    r -= 1

    out = []
    for x in myset:
        out.append(list(x))
    return out


def fourSum3(nums, target):
    n = len(nums)
    out = []
    nums.sort()
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1] : continue
        for j in range(i+1,n):
            if j > i+1 and nums[j] == nums[j-1] :continue
            l = j+1
            r = n-1
            t = target - nums[i] - nums[j]
            while l < r:
                if l > j+1 and nums[l] == nums[l-1]:
                    l += 1
                    continue
                if r < n-1 and nums[r] == nums[r+1]:
                    r -= 1
                    continue
                sum = nums[l] + nums[r]
                if sum == t:
                    out.append([nums[i], nums[j], nums[l], nums[r]])
                    l+= 1
                    r-= 1
                elif sum < t:
                    l+= 1
                else:
                    r -= 1
    return out
nums = [-2,-1,-1,1,1,2,2]
target = 0

print(fourSum(nums, target))
print(fourSum2(nums, target))
print(fourSum3(nums, target))