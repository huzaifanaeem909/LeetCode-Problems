"""
Leetcode-912. Sort an Array
Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
"""

# Time Complexity: O(nlog(n))
# Space Complexity: O(n)


def sortArray(nums):

    def merge(arr, left, mid, right):
        left_half = arr[left : mid + 1]
        right_half = arr[mid + 1 : right + 1]

        i, j = 0, 0
        k = left

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    def mergeSort(arr, left, right):
        if left >= right:
            return arr
        mid = left + ((right - left) // 2)
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)
        return arr

    return mergeSort(nums, 0, len(nums) - 1)


nums = [5, 2, 3, 1]
print("Sorted Array:", sortArray(nums))
