#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length = len(s)
        current = 0
        if s == '':
            return True
        for i in range(len(t)):
            if current < length and s[current] == t[i]:
                current += 1
            elif current >= length:
                break
        print(current)
        if current == length:
            return True
        else:
            return False
# @lc code=end

