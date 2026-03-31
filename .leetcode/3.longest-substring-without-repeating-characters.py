#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ss = set()
        left = 0
        max_length = 0
        
        for t in range(len(s)):
            while s[t] in ss:
                ss.remove(s[left])
                left += 1
            ss.add(s[t])
            max_length = max(max_length, t - left + 1)
        return max_length
        
# @lc code=end

