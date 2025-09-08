"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation: The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4] 
Output: false 
Explanation: All elements are distinct.

Example 3: 
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

# Solution 1:
def containsDuplicate(nums):
  freq = {}
  for num in nums:
    if num in freq:
      return True
    else:
      freq[num] = 1
  return False

nums = [1,2,3,1]
containsDuplicate(nums)
# Time Complexity: O(n)
# Space Complexity: O(n)

# Solution 2:
def containsDuplicate(nums):
  seen = set()  # Empty set to store numbers
  for num in nums:
    if num in seen:
      return True
    else:
      seen.add(num)
  return False

nums = [1,2,3,1]
containsDuplicate(nums)
# Time Complexity: O(n)
# Space Complexity: O(n)
