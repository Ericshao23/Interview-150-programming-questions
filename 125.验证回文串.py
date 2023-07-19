#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        for str in s:
            if str.isalpha():
                temp.append(str.lower())
            elif str.isdigit():
                temp.append(str)
        print(temp)
        # 优化回文匹配
        return (res := ''.join(temp)) == res[::-1]
        # for i in range(len(temp)//2):
        #     if temp[i] != temp[len(temp) - i - 1]:
        #         return False
        # return True
# @lc code=end

