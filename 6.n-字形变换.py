#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] N 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # if numRows < 2:
        #     return s
        # res = ["" for _ in range(numRows)]
        # print(res)
        # i, flag = 0, -1
        # for c in s:
        #     res[i] += c
        #     if i == 0 or i == numRows - 1:
        #         flag = -flag
        #     i += flag
        # print(res)
        # return "".join(res)
        n, r = len(s), numRows
        if r == 1 or r >= n:
            return s
        t = r * 2 -2;
        ans = []
        for i in range(r):
            for j in range(0, n - i, t):
                ans.append(s[j + i])
                if 0 < i < r - 1 and j + t - i < n:
                    ans.append(s[j + t - i])
        return "".join(ans)
# @lc code=end

