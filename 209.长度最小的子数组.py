#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 暴力
        # if sum(nums) < target:
        #     return 0
        # ans = inf
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return 1
        #     total = nums[i]
        #     for j in range(i + 1, len(nums)):
        #         print(total)
        #         if total + nums[j] < target:
        #             total += nums[j]
        #         elif total + nums[j] > target:
        #             break
        #         else:
        #             ans = min(ans, j - i + 1)
        # return ans
        # 滑动窗口
        if not nums or sum(nums) < target:
            return 0
        length = len(nums)
        l, r = 0, 0
        total = 0
        min_len = float('inf')

        while r < length:
            total += nums[r]
            while total >= target:
                min_len = min(min_len, r - l + 1)
                total -= nums[l]
                l += 1
            r += 1
        
        if min_len == float('inf'):
            return 0
        else:
            return min_len


# @lc code=end

