"""
Given an array nums of size n, return the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

# Method 1:

# Time-Complexity: O(n)
# Space-Complexity: O(n)

def majorityElement(nums):
  n = len(nums)
  count = {}
  
  for num in nums:
    if num in count:
      count[num] += 1
    else:
      count[num] = 1

    if count[num]>n//2:
      return num

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))


# Method 2:

# Time-Complexity: O(n)
# Space-Complexity: O(1)

def majorityElement(nums):
  candidate = None
  count = 0
  for num in nums:
    if count==0:
      candidate = num
    count += (1 if num == candidate else -1)
  return candidate

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
