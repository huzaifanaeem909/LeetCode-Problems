"""
LeetCode 14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

# Time Complexity: O(n)
# Space Complexity: O(1)


# Method-1:
def longestCommonPrefix(strs):
    result = ""
    # Iterate over each character index of the first string
    for i in range(len(strs[0])):
        for string in strs:
            # If index i is out of bounds for any string or characters do not match, return the result
            if i == len(string) or string[i] != strs[0][i]:
                return result
        # If all characters match at index i, add the character to the result
        result += strs[0][i]

    # Return the common prefix found
    return result


strs = ["flower", "flow", "flight"]
print("Output:", longestCommonPrefix(strs))


# Method-2:
def longestCommonPrefix(strs):
    # Initialize min_length to infinity to find the shortest string length
    min_length = float("inf")

    # Find the length of the shortest string in the list
    for string in strs:
        if min_length > len(string):
            min_length = len(string)

    i = 0
    # Iterate over each character index up to the length of the shortest string
    while i < min_length:
        for string in strs:
            # If characters at index i do not match, return the common prefix up to this point
            if string[i] != strs[0][i]:
                return string[:i]
        i += 1

    # If all characters match up to the length of the shortest string, return the common prefix
    return string[:i]


strs = ["flower", "flow", "flight"]
print("Output:", longestCommonPrefix(strs))
