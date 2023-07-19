#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        # ans, h1, h2 = 0, 0, 0
        # for i in range(len(height)):
        #     h1 = max(h1, height[i])
        #     h2 = max(h2, height[-i - 1])
        #     ans = ans + h1 + h2 - height[i]
        # return ans - len(height)*h1
        ans = 0
        current = 0
        stack = []
        while current < len(height):
            while len(stack) > 0 and height[current] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                distance = current - stack[-1] - 1;
                bounded_height = min(height[stack[-1]], height[current]) - height[top]
                ans += distance * bounded_height
            stack.append(current)
            current += 1
        return ans
# @lc code=end

