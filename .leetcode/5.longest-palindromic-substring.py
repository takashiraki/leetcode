#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        r = ""
        for i in range(len(s)):
            left, right = i, i
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                
            if right - left - 1 > len(r):
                r = s[left + 1:right]
                
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > len(r):
                r = s[left + 1:right]
        return r
# @lc code=end

