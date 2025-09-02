"""
You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
"""

# Time Complexity: O(n)
# Space Complexity: O(n)

def summaryRanges(nums):
  ans = []
  i = 0
  
  while i < len(nums):
    start = nums[i]

    while i < len(nums)-1 and nums[i]+1 == nums[i+1]:
      i+=1
    
    if start != nums[i]:
      ans.append(str(start) + "->" + str(nums[i]))
    else:
      ans.append(str(nums[i]))

    i+=1
  return ansT
  
nums = [0,1,2,4,5,7]
print(summaryRanges(nums))
