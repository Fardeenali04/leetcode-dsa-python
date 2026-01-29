"""
LeetCode 88 — Merge Sorted Array

Approach:
1. Remove extra zeros from nums1 after index m.
2. Append all elements of nums2 to nums1.
3. Sort the final array.

Algorithm:
- del nums1[m:]
- nums1.extend(nums2)
- nums1.sort()

Time Complexity:
- O((m + n) log(m + n))

Space Complexity:
- O(1)  # in-place
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        del nums1[m:]
        nums1.extend(nums2)
        nums1.sort()
