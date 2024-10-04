"""
Leetcode-162. Find Peak Element:

A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.
You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
"""

# Time Complexity: O(log N)
# Auxiliary Space: O(1)


def findPeakElement(nums):
    n = len(nums)
    low, high = 0, n - 1

    while low <= high:

        # Calculate the mid index
        mid = low + ((high - low) // 2)

        # Check if the mid element is less than the previous element
        if mid > 0 and nums[mid] < nums[mid - 1]:
            high = mid - 1

        # Check if the mid element is less than the next element
        elif mid < n - 1 and nums[mid] < nums[mid + 1]:
            low = mid + 1

        else:
            return mid


nums = [1, 2, 1, 3, 5, 6, 4]
print(findPeakElement(nums))
