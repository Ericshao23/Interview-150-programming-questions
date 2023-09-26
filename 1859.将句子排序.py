#
# @lc app=leetcode.cn id=1859 lang=python3
#
# [1859] 将句子排序
#

# @lc code=start
# class Solution:
#     def sortSentence(self, s: str) -> str:
#         ans = []
#         reg = re.compile(r"([a-zA-Z]+)(\d+)")
#         arr = s.split()
    
#         for s in arr:
#             matcher = reg.search(s)
    
#             if matcher is None:
#                 continue
    
#             content = matcher.group(1)
#             i = int(matcher.group(2)) - 1
    
#             ans.append([i, content])
    
#         ans.sort(key=lambda x: x[0])
#         return " ".join(map(lambda x: x[1], ans))
class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        n = len(s)   # 单词数量
        arr = ["" for _ in range(n)]   # 单词数组
        for wd in s:
            # 计算位置索引对应的单词数组下标，并将单词放入对应位置
            # 数组下标为 0 开头，位置索引为 1 开头
            arr[int(wd[-1])-1] = wd[:-1]
        return " ".join(arr)
    
        