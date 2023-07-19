#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1
        #     flag = 1
        #     for j in range(len(needle)):
        #         if haystack[i + j] != needle[j]:
        #             flag = -1
        #             break
        #     if flag == 1:
        #         return i
        # return -1
# @lc code=end

