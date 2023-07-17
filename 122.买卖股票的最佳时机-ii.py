#
# @lc app=leetcode.cn id=122 lang=python3
# 每天都卖，价格涨交易， 价格跌不交易
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            temp = prices[i] - prices[i-1]
            if temp > 0:
                profit += temp
        return profit
        # n  = len(prices)
        # dp = [][2]
        # dp[0][1] = - prices[0]
        # for i in range(1, n):
        #     dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        #     dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        # return dp[n - 1][0]
# @lc code=end

