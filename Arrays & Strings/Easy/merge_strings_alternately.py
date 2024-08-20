"""
You are given two strings word1 and word2.Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Example 2:
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
"""

# Time Complexity: O(n)
# Auxiliary Space Complexity: O(n) --> (Additional space is used to store the new ar.)

def mergeAlternately(word1, word2):
	#initialize the 2 pointers for word1 and word2
	pointer_for_word1 = 0
	pointer_for_word2 = 0

	#initialize the 2 lengths of word1 and word2
	length_of_word1 = len(word1)
	length_of_word2 = len(word2)

	#initialize result list
	result = []

	#we iterate each letter in word1 and word2 until we have exhausted one of them
	while(pointer_for_word1 < length_of_word1 and pointer_for_word2 < length_of_word2):

		#add a letter from word1, then a letter from word2
		result.append(word1[pointer_for_word1])
		result.append(word2[pointer_for_word2])

		#move the two pointers
		pointer_for_word1 += 1
		pointer_for_word2 += 1

	#if word1 is not exhausted, add its remaining letters to result
	while(pointer_for_word1 < length_of_word1):
		result.append(word1[pointer_for_word1])
		pointer_for_word1 += 1

	#if word2 is not exhausted, add its remaining letters to result
	while(pointer_for_word2 < length_of_word2):
		result.append(word2[pointer_for_word2])
		pointer_for_word2 += 1

	#return the string of the result list
	return "".join(result)


word1 = "abcdefg"
word2 = "pqrs"

print(mergeAlternately(word1, word2))