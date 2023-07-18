#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0] * length
        # answer[i] index i 左侧所有元素的乘积
        answer[0] = 1

        for i in range(1, length):
            answer[i] = nums[i-1] * answer[i-1]
        # 省去维护右侧数组
        R = 1
        for i in range(length-1,-1,-1):
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer


# @lc code=end

