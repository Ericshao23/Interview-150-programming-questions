#
# @lc app=leetcode.cn id=1859 lang=python3
#
# [1859] 将句子排序
#

# @lc code=start
class Solution:
    def sortSentence(self, s: str) -> str:
        ans = []
        reg = re.compile(r"([a-zA-Z]+)(\d+)")
        arr = s.split()
    
        for s in arr:
            matcher = reg.search(s)
    
            if matcher is None:
                continue
    
            content = matcher.group(1)
            i = int(matcher.group(2)) - 1
    
            ans.append([i, content])
    
        ans.sort(key=lambda x: x[0])
    
        return " ".join(map(lambda x: x[1], ans))
import re