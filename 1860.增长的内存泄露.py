#
# @lc app=leetcode.cn id=1860 lang=python3
#
# [1860] 增长的内存泄露
#

# @lc code=start
class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        t = 1
        while t <= max(memory1, memory2):   # 是否可分配
            if memory1 < memory2:   # 分配给 2
                memory2 -= t
            else:   # 分配给 1
                memory1 -= t
            t += 1
        return [t, memory1, memory2]


# @lc code=end

