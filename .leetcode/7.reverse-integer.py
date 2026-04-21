#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        s = ""
        rs = str(x)[::-1]
        for c in rs:
            # マイナス考慮
            if c == "-":
                s = "-" + s
            else:
                # こっちは通常
                s = s + c
                
        # 32bit整数の範囲外なら0を返す
        if int(s) < -2**31 or int(s) > 2**31 - 1:
            return 0
        
        return int(s)
        
# @lc code=end

