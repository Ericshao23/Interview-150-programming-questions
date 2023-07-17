#
# @lc app=leetcode.cn id=2679 lang=python3
#
# [2679] 矩阵中的和
#

# @lc code=start
class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for x in nums:
            x.sort()
        return sum(max(a) for a in zip(* nums))
# @lc code=end

