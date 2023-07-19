#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        if length < 2:
            return length
        nums = [1 for _ in range(length)]
        for i in range(1, length):
            if ratings[i] > ratings[i - 1]:
                nums[i] = nums[i - 1] + 1
        for i in range(length - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                nums[i - 1] = max(nums[i - 1], nums[i] + 1)
        return sum(nums)        


# @lc code=end

