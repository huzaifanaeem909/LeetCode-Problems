"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer. 
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

# Time Complexity: O(n)
# Space Complexity: O(1)

def productArrayExceptSelf(arr):
    n = len(arr)
    res = [1] * n
    print(res)  # Output: [1, 1, 1, 1, 1]
    
    # Calculate products of all elements to the left of each index
    left = 1
    for i in range(n):
        res[i] = left
        left *= arr[i]

    # Multiply by products of all elements to the right of each index
    right = 1
    for i in range(n-1, -1, -1):
        res[i] *= right
        right *= arr[i]

    print(res)
    
arr = [10, 3, 5, 6, 2]
productArrayExceptSelf(arr)  # Output: [180, 600, 360, 300, 900]
