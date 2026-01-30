"""
LeetCode: Length of Last Word
Link: https://leetcode.com/problems/length-of-last-word/solutions/7537485/58-length-of-last-word-by-fardeenali04-sb0d/
Approach:
- Split the string using split().
- The last word will be at index -1.
- Return the length of that word.

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.split()[-1])      #Approach 2
      #Approach 1
      # words = s.split()
      # result = ""
      # for w in words[::-1]:
      #     result += w
      #     break
      # return len(result)
