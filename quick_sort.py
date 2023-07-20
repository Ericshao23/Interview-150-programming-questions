#-*- coding: utf-8 -*-

# 选择一个元素作为基数（通常是第一个元素），把比基数小的元素放到它左边，比基数大的元素放到它右边（相当于二分），再不断递归基数左右两边的序列
def quick_sort(lists, left, right):
    if left > right: 
        return lists
    temp = lists[left]
    i, j = left, right
    while i != j:
        while lists[j] >= temp and j > i:
            j -= 1
        while lists[i] <= temp and j > i:
            i += 1
        if j > i:
            lists[i], lists[j] = lists[j], lists[i]
    lists[left], lists[i] = lists[i], temp
    quick_sort(lists, left, i - 1)
    quick_sort(lists, i + 1, right)
    return lists


if __name__ == "__main__":
    test = [2, 5, 4, 6, 7, 3, 2, 10, 2, 3, 1]
    print(quick_sort(test,0, len(test) - 1))

