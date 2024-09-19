"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

"""

# Time Complexity: O(n)
# Space Complexity: O(1)

def isSubsequence(s, t):
    # Get the lengths of both strings s and t
    S = len(s)
    T = len(t)
    
    # If s is an empty string, it is trivially a subsequence of any string
    if S == 0: 
        return True
    
    # If s is longer than t, it can't be a subsequence of t
    if S > T: 
        return False

    # Initialize a pointer i to track the current index in string s
    i = 0
    
    # Iterate through each character in string t
    for j in range(T):
        # If the current character of s matches the current character of t
        if s[i] == t[j]:
            # If we've matched all characters in s, return True
            if i == S - 1:
                return True
            # Move to the next character in s
            i += 1

    # If the loop completes without matching the entire string s, return False
    return False

# Example usage:
s = "abc"
t = "ahbgdc"

# Print the result of checking if s is a subsequence of t
print(isSubsequence(s, t))
