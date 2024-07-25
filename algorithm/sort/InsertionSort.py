# 插入排序

def insertion_sort(arr):
    if len(arr)<2:
        return arr
    for i in range(1, len(arr)):
        for j in range(i-1, -1, -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

