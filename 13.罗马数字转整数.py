#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        symbolValue = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        length = len(s)
        ans = 0
        max = -1
        for i in range(length - 1, -1, -1):
            value = symbolValue[s[i]]
            if max <= value:
                ans += value
                max = value
            else:
                ans -= value
        return ans


# @lc code=end

