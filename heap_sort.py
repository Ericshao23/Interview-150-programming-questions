class Solution(object):

    def build_heap(self, i, l):
        '''
        构建大顶堆
        即每个节点的值都大于等于其叶子的值
        '''
        arr = self.arr
        left, right = 2 * i + 1, 2 * i + 2 # 左右子节点下标
        large_index = i
        if left <= l and arr[i] < arr[left]:
            large_index = left
        if right <= l and arr[left] < arr[right]:
            large_index = right
        if large_index != i: # 如果三元素最大值不是父节点下标，则交换后需要调整大顶堆
            arr[i], arr[large_index] = arr[large_index], arr[i]
            self.build_heap(large_index, l)

    def heap_sort(self, arr):
        """
        堆排序，基于完全二叉树结构的一种排序
        通过构建大顶堆（即每个节点的值都大于等于其叶子的值），完成升序排列
        """
        i, l = 0, len(arr)
        self.arr = arr
        for i in range(l // 2 - 1, -1, -1): # 构建大顶堆，从最后一个非叶子节点开始
            self.build_heap(i, l - 1)
        for j in range(l - 1, -1, -1): # 根节点和最后一个元素交换，然后调整大顶堆
            arr[0], arr[j] = arr[j], arr[0]
            self.build_heap(0, j - 1)
        return arr


test_list = [4, 2, 1, 23, 5, 12, 13, 14, 15, 9, 2, 3]
test_sort = Solution()
print(test_sort.heap_sort(test_list))