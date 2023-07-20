# -*- coding: UTF-8 -*-

# shell sort
# 通过某个增量 gap，将整个序列分给若干组，从后往前进行组内成员的比较和交换，随后逐步缩小增量至
def shell_sort(lists):
    count = len(lists)
    # 初始步数
    gap = int(count / 2)
    while gap > 0:
        # 从第gap个开始遍历
        for i in range(gap, count):
            # 逐步和前边其他组成员比较和交换
            j = i - gap
            while j >= 0:
                if lists[j] > lists[j + gap]:
                    lists[j], lists[j + gap] = lists[j + gap], lists[j]
                j -= gap
        gap = int(gap / 2) 
    return lists

if __name__ == "__main__":
    test = [2, 5, 4, 6, 7, 3, 2]
    print(shell_sort(test))