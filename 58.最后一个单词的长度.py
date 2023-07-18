#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s = "   fly me   to   the moon  "
        split = s.split(' ')
        t = s.split()
        return len(t[-1])
        # for i in t:
        #     print (i)
        # for i in split:
        #     print(i)
        # for i in split[::-1]:
        #     if i !="":
        #         return len(i)
# @lc code=end

