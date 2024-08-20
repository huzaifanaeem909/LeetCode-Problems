"""
LeetCode-2239: Given an integer array nums of size n, return the number with the value closest to 0 in nums.
If there are multiple answers, return the number with the largest value.
"""

# Time Complexity: O(n)
# Auxiliary Space: O(1)

def findClosestNumber(arr):
    # Initialize closest_number with the first element of the array
    closest_number = arr[0]
    
    # Iterate through the array to find the number closest to zero
    for i in arr:
        # Update closest_number if the current number is closer to zero
        if abs(i) < abs(closest_number):
            closest_number = i
        # If two numbers are equally close to zero, prefer the positive one
        elif abs(i) == abs(closest_number) and i > closest_number:
            closest_number = i
    
    # Return the closest number found
    return closest_number

arr = [-4, -2, -1, 1, 4, 8]
print("Closest number to Zero:", findClosestNumber(arr))

# Another Solution:

def findClosestNumber(arr):
    # Initialize closest_number with the first element of the array
    closest_number = arr[0]
    
    # Iterate through the array to find the number closest to zero
    for i in arr:
        # Update closest_number if the current number is closer to zero
        if abs(i) < abs(closest_number):
            closest_number = i
    # Return the absolute value if the closest number is negative and its absolute value is also present in the Array
    if closest_number < 0 and abs(closest_number) in arr:
        return abs(closest_number)
    
    # Return the closest number found
    return closest_number

arr = [-34, -22, -8, 10, 12, 8]
print("Closest number to Zero:", findClosestNumber(arr))
