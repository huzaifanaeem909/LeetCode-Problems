"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. 
Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A". 

Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0
"""

# Method-1 (Brute-Force)
def numJewelsInStones(jewels, stones):
  count = 0
  for stone in stones:
    if stone in jewels:
      count+=1
  return count

jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))

#Method-2 (Optimal)
def numJewelsInStones(jewels, stones):
  jewelset = set(jewels)  # Using a Set for Faster Lookup
  print(jewelset)  # jewelSet = {'a', 'A'}
  count = 0
  for stone in stones:
    if stone in jewelset:
      count+=1
  return count

jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))
