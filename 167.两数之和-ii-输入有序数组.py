#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1, idx2 = 0, len(numbers) - 1
        while idx1 < idx2:
            # 通过引入mid 来提速，减少便利次数
            mid = (idx1 + idx2) // 2
            sum = numbers[idx1] + numbers[idx2]
            if sum == target:
                break
            elif sum < target:
                if numbers[mid] + numbers[idx2] < target:
                    idx1 = mid
                else:
                    idx1 += 1
            else:
                if numbers[mid] + numbers[idx1] > target:
                    idx2 = mid
                else:
                    idx2 -= 1
        return [idx1 + 1, idx2 + 1]

# @lc code=end

