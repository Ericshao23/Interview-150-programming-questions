#-*- coding: utf-8 -*-

# 依次找到剩余元素的最小值或者最大值，放置在末尾或者开头
def select_sort(lists):
    count = len(lists)
    for i in range(0, count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists

if __name__ == "__main__":
    test = [2, 5, 4, 6, 7, 3, 2, 10, 2, 3, 1]
    print(select_sort(test))