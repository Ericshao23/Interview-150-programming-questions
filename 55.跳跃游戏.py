#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # max_num = 0
        # for i, jump in enumerate(nums):
        #     if max_num >= i and i + jump > max_num:
        #         max_num = i + jump
        # return max_num >= i

        # Violence
        n = len(nums)
        @cache
        def dfs(i):
            if i >= n - 1:
                return True
            if nums[i] == 0:
                return False
            for j in range(nums[i], 0, -1):
                if dfs(i + j):
                    return True
            return False
        return dfs(0)

# @lc code=end

