# 归并排序
def merge_sort(arr, left, right):
    if left == right:
        return

    mid = left + (right - left) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid+1, right)
    merge(arr, left, mid, right)
def merge(arr, left, mid, right):
    l1 = left
    l2 = mid + 1
    help = []
    while l1 <= mid and l2 <= right:
        if arr[l1] <= arr[l2]:
            help.append(arr[l1])
            l1 = l1 + 1
        else:
            help.append(arr[l2])
            l2 = l2 + 1
    while l1 <= mid:
        help.append(arr[l1])
        l1 = l1 + 1
    while l2 <= right:
        help.append(arr[l2])
        l2 = l2 + 1
    for i in range(len(help)):
        arr[left+i] = help[i]

arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr, 0, len(arr)-1)
print(arr)
