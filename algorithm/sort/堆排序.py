# 堆排序

def heapify(arr, index, heap_size):
    left = index*2 + 1
    while left < heap_size:
        largest = left + 1 if left+1 < heap_size and arr[left+1] > arr[left] else left

        largest = largest if arr[largest] > arr[index] else index
        if largest == index:
            break
        arr[largest], arr[index] = arr[index], arr[largest]
        index = largest
        left = index*2 + 1


def heap_insert(arr, index):
    while arr[index] > arr[int((index-1) / 2)]:
        arr[index], arr[int((index-1) / 2)] = arr[int((index-1) / 2)], arr[index]
        index = int((index-1) / 2)


def heapsort(arr):
    if len(arr) <= 1 or arr == None:
        return arr

    for i in range(len(arr)):
        heap_insert(arr, i)
    heap_size = len(arr)
    while heap_size > 0:
        heap_size -= 1
        arr[0], arr[heap_size] = arr[heap_size], arr[0]
        heapify(arr, 0, heap_size)


# arr = [2, 3, 4, 5, 1, 6, 8, 3]
arr = [6,5,4,3,2,1,7,6,5,4,3,2,1,8,7,6,5]
heapsort(arr)
print(arr)

