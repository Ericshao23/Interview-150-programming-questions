#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, ans= 0, len(height) - 1, 0
        while l < r:
            if height[l] < height[r]:
                ans = max(height[l] * (r - l), ans)
                l += 1
            else:
                ans = max(height[r] * (r - l), ans)
                r -= 1
        return ans
# @lc code=end

