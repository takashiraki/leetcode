#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [""] * numRows
        cur_row = 0
        going_down = True

        for c in s:
            rows[cur_row] += c
            
            if cur_row == numRows - 1:
                going_down = False
            elif cur_row == 0:
                going_down = True

            cur_row += 1 if going_down else -1

        return "".join(rows)
# @lc code=end

