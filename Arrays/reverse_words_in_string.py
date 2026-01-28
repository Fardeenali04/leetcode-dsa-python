"""
LeetCode: Reverse Words in a String
Link: https://leetcode.com/problems/reverse-words-in-a-string/

Approach 1: Basic
- Split string into words
- Reverse list
- Join words

Time: O(n)
Space: O(n)
"""

class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        result = ""
        for word in words[::-1]:
            result += word + " "
        return result.strip()


"""
Approach 2: Optimized Pythonic
- Use split + reverse + join
"""

class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])
