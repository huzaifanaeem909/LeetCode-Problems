"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

Example 1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9, so the indices [0, 1] are returned.

Example 2:
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
Explanation: nums[1] + nums[2] = 2 + 4 = 6.
"""

# Time Complexity: O(n)
# Auxiliary Space: O(n)

def twoSum(nums, target):
    dict = {}
    
    for i, num in enumerate(nums):
        diff = target - num
        if diff in dict:
            return [dict[diff], i]
        dict[num] = i

nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums,target))
