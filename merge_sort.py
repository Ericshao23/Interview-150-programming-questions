#-*- coding: utf-8 -*-

# 归并排序：递归将数组分为两个序列，有序合并这两个序列。
def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    
    num = int(len(lists) / 2)
    left_lists = merge_sort(lists[:num])
    right_lists = merge_sort(lists[num:])
    return merge(left_lists, right_lists)

def merge(left_lists, right_lists):
    left, right = 0, 0
    result = []

    while left < len(left_lists) and right < len(right_lists):
        if left_lists[left] < right_lists[right]:
            result.append(left_lists[left])
            left += 1
        else:
            result.append(right_lists[right])
            right += 1
    result += left_lists[left:]
    result += right_lists[right:]

    return result

if __name__ == "__main__":
    test = [2, 5, 4, 6, 7, 3, 2]
    print(merge_sort(test))
