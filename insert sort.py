# -*- coding: UTF-8 -*-

# insert sort
# 以第一个元素为有序数组，其后的元素通过再这个已有序的数组中找到合适的元素并插入
def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists

def optimize_insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        if lists[i] < lists[i - 1]:
            temp = lists[i]
            low = 0
            high = i - 1
            # 寻找插入位置时，二分，提速
            while low < high:
                mid = (high + low) // 2
                if temp > lists[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            j = i - 1
            while j > low:
                lists[j + 1] = lists[j]
                j -= 1
            lists[j] = temp
    return lists



if __name__ == '__main__':
    test = [2,3,9,1,3,5,4,2,7,6]
    print(insert_sort(test))
    print(optimize_insert_sort(test))