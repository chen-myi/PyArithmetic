# 选择排序
def selection_sort(arr):
    for left in range(len(arr)):
        for i in range(left+1, len(arr)):
            if arr[i] < arr[left]:
                arr[i], arr[left] = arr[left], arr[i]
