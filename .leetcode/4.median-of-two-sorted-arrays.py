#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a1 = nums1
        a1.extend(nums2)
        a1.sort()
        n = len(a1)
        
        if n % 2 == 0:
            return float((a1[n//2 - 1] + a1[n//2])/2)
        else:
            return float(a1[n//2])
# @lc code=end

