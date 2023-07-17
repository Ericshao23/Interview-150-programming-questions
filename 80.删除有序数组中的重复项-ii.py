#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = len(nums)
        for i in range(p-1,1,-1):
            if nums[i] == nums[i-1] and nums[i] == nums[i-2]:
                del nums[i]
        return len(nums)
:# @lc code=end