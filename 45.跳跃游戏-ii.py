#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # size = len(nums)
        # dp = [float("inf") for _ in range(size)]
        # dp[0] = 0
        # j = 0
        # for i in range(1, size):
        #     while j + nums[j] < i:
        #         j += 1
        #     dp[i] = dp[j] + 1
        # return dp[size - 1]
        end, max_i = 0, 0
        steps = 0
        for i in range(len(nums) - 1):
            max_i = max(max_i, nums[i] + i)
            if i == end:
                end = max_i
                steps += 1
        return steps 
# @lc code=end

