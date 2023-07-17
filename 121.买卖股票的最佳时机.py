#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_price = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         max_price = max(max_price, prices[j] - prices[i])
        # return max_price
        max_price = 0
        min_price = 100000
        for price in prices:
            max_price = max(price - min_price, max_price)
            min_price = min(price, min_price)
        return max_price
# @lc code=end

