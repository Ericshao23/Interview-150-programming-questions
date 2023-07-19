#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # length = len(nums)
        # ans = []
        # current = 0
        # for i in range(length - 2):
        #     for j in range(i + 1, length - 1):
        #         for k in range(j + 1, length):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 temp = []
        #                 temp.append(nums[i])
        #                 temp.append(nums[j])
        #                 temp.append(nums[k])
        #                 ans.append(temp)
        # print(ans)
        # return ans
        # 思考一下输出的重复结果如何解决，因为题目说了不考虑顺序   
        # example
        # Testcase： [-1,0,1,2,-1,-4]
        # Except answer：[[-1,-1,2],[-1,0,1]]
        # My answer： [[-1,0,1],[-1,2,-1],[0,1,-1]]
        ###############


        nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):
            if nums [k] > 0:
                break
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            l, r = k + 1, len(nums) - 1
            while l < r:
                sum = nums[k] + nums[r] + nums[l]
                if sum < 0:
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif sum > 0:
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                else:
                    res.append([nums[k], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return res
# @lc code=end

