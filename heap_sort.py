from collections import deque

def swamp(lists, i, j):
    lists[i], lists[j] = lists[j], lists[i]
    return lists

def heap_adjust(lists, start, end):
    temp = lists[start]

    i = start
    j = 2 * i

    while j <= end:
        if (j < end) and (lists[j] < lists[j + 1]):
            j += 1
        if temp < lists[j]:
            lists[i] = lists[j]
            i = j
            j = 2 * i
        else:
            break
    lists[i] = temp

def heap_sort(lists):
    length = len(lists) - 1
    first_sort_count = length // 2
    for i in range(first_sort_count):
        heap_adjust(lists, first_sort_count - i, length)

    for i in range(length - 1):
        lists = swamp(lists, 1, length -i)
        heap_adjust(lists, 1, length - i -1)
    return [lists[i] for i in range(1, len(lists))]



if __name__ == '__main__':
    lists = deque([50, 16, 30, 10, 60,  90,  2, 80, 70])
    # lists = [50, 16, 30, 10, 60,  90,  2, 80, 70]
    lists.appendleft(0)
    print(heap_sort(lists))
