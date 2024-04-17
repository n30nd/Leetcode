# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    n = len(nums)
    for i in range(n) :
        for j in range(i+1, n):
            if nums[i] + nums[j] == target :
                return list((i,j))

# Do chỉ có 1 giải pháp nên nếu có 2 chỉ số i, j (i!=j) mà nums[i] = nums[j]
# thì [i,j] là đáp án. Nếu điều này sai thì còn chỉ số k khác i,j mà nums[i]+num[k] = target
# như vậy thì [i,k] là đáp án, nhưng lúc này nums[j] + nums[k] = target =>
# [j,k] cũng là đáp án, nó mâu thuẫn với giả thiết chỉ có 1 đáp án như bài cho
#
# Do đó, ta lập 1 dictionary lưu giữ các cặp nums[i],i vào, duyệt các phần từ của mảng
# nums bổ sung vào dic này, nếu đã tồn tại nums[i] => chính là trường hợp bằng nhau vừa xét
# không thì ta tìm, bổ sung index của target-nums[i]
def twoSum2(nums, target) :
    seen = {}
    n = len(nums)
    for i in range(n):
        diff = target - nums[i]
        if diff in seen :
            return [seen[diff], i]
        else:
            seen[nums[i]] = i

nums = [2,7,11,15]
target = 9
print(twoSum2(nums, target))
