# Given
# an
# integer
# array
# nums,
# return all
# the
# triplets[nums[i], nums[j], nums[k]]
# such
# that
# i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice
# that
# the
# solution
# set
# must
# not contain
# duplicate
# triplets.
#
# Example
# 1:
#
# Input: nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The
# distinct
# triplets
# are[-1, 0, 1] and [-1, -1, 2].
# Notice
# that
# the
# order
# of
# the
# output and the
# order
# of
# the
# triplets
# does
# not matter.
# Example
# 2:
#
# Input: nums = [0, 1, 1]
# Output: []
# Explanation: The
# only
# possible
# triplet
# does
# not sum
# up
# to
# 0.
# Example
# 3:
#
# Input: nums = [0, 0, 0]
# Output: [[0, 0, 0]]
# Explanation: The
# only
# possible
# triplet
# sums
# up
# to
# 0.
#
# Constraints:
#
# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    # n = len(nums)
    # myset = set()
    # nums.sort()
    # for i in range(n) :
    #     for j in range(i+1, n):
    #        for k in range(j+1, n):
    #            if nums[i] + nums[j] + nums[k] == 0 :
    #                myset.add((nums[i], nums[j], nums[k]))
    # out = []
    # for x in myset:
    #     out.append(list(x))
    # return out


    n = len(nums)
    myset = set()
    nums.sort()
    for i in range(n) :
        target = 0 - nums[i]
        l = i+1
        r = n-1
        while l < r :
            sum = nums[l] + nums[r]
            if sum == target :
                myset.add((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
            elif sum < target :
                l += 1
            else :
                r -= 1
    out = []
    for x in myset:
        out.append(list(x))
    return out

nums = [-1,0,1,2,-1,-4]
out = threeSum(nums)
print(out)


