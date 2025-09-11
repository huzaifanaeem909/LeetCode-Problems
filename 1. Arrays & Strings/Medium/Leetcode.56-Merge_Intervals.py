"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Example 3:
Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.
"""


def merge_intervals(intervals):
  intervals.sort(key=lambda x:x[0])  # Sort intervals by their start value
  print(intervals)  # Output: [[1, 3], [2, 6], [8, 10], [15, 18]]
  merged = []
  
  for interval in intervals:
    if not merged or merged[-1][1] < interval[0]:
      merged.append(interval)
    else:
      merged[-1][1] = max(merged[-1][1], interval[1])
  return merged

intervals = [[8,10],[1,3],[2,6],[15,18]]  
print(merge_intervals(intervals))

# Time complexity: O(nlogn)
# Space complexity: O(n)
