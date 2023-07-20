# -*- coding: UTF-8 -*-

# 冒泡排序
# 通过相邻元素的比较和交换，使得每一趟循环都能找到未有序数组的最大值或最小值。
def bubble_sort(lists):
    count = len(lists)
    for i in range(0, count - 1):
        for j in range(0, count - i - 1):
            if lists[j] > lists[j + 1]:
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
    return lists

def optimize_bubble_sort(lists):
    count = len(lists)
    for i in range(0, count - 1):
        flag = False
        for j in range(0, count - i - 1):
            if lists[j] > lists[j + 1]:
                flag = True
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
        if flag == False:
            break
    return lists

if __name__ == "__main__":
    test = [2, 5, 4, 6, 7, 3, 2, 10, 2, 3, 1]
    print(bubble_sort(test))