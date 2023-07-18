#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # citations.sort(reverse=True)
        # print (citations)
        # # citations = sorted(citations)
        # size = len(citations)
        # for i, h in enumerate(citations):
        #     if i >= h:
        #         return i
        # return size
        # dichotomy
        # x篇>=x,则一定x-1篇>=x-1
        # x篇>=x不符合,则一定x+1篇>=x+1不符合
        size = len(citations)
        l,r=1, size # 篇数取值范围
        def ck(x):
            if sum(c>=x for c in citations)>=x:
                return False
            else:
                return True
        while l<=r:
            mid=l+(r-l)//2
            if ck(mid):
                r=mid-1
            else:
                l=mid+1
        return l-1
# @lc code=end

