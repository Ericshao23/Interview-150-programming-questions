#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        length = len(gas)
        # bottom is the lowest gas quantity, sum is the current gas quantity
        bottom, sum = 0, 0 
        start = -1
        for i in range(length):
            sum += gas[i]-cost[i]
            if sum < bottom:
                bottom = sum
                start = i
        if sum < 0:
            return -1
        return start + 1


# @lc code=end

