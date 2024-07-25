# 冒泡排序
class BubbleSort:
    def bubble_sort(self, array):
        if len(array) <= 1:
            return array
        n = len(array)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]

#
# arr = [64, 34, 25, 12, 22, 11, 90]
# 
# s = BubbleSort()
# s.bubble_sort(arr)
#
# print("排序后的数组:")
# for i in range(len(arr)):
#     print("%d" % arr[i]),